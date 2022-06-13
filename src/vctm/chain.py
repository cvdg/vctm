"""
Chain of Command pattern.
"""

from calendar import c
from multiprocessing import AuthenticationError


class Command:
    SUCCESS = True
    FAILURE = False

    def execute(self, context: hash) -> bool:
        """ execute is called if previus commands where all a success. """
        return Command.SUCCESS

    def post_execute(self, context: hash, success: bool, error: Exception) -> None:
        """ post_execute is always called, even on an exception. """
        pass


class Chain(Command):
    def __init__(self):
        self.commands = []

    def add(self, command: Command):
        self.commands.append(command)

    def execute(self, context: hash) -> bool:
        success = Command.SUCCESS

        for command in self.commands:
            success = command.execute(context)
            if not success:
                break

        return success

    def post_execute(self, context: hash, success: bool, error: Exception) -> None:
        for command in self.commands[::-1]:
            command.post_execute(context, success, error)


class Executor(Chain):
    """
    Order of executions of chains:
      1: initialize
      2: authentication
      3: authorize
      4: validate
      5: process
      6: audit
      7: report
    """

    def __init__(self):
        super().__init__()

        self.initialize = Chain()
        self.authentication = Chain()
        self.authorize = Chain()
        self.validate = Chain()
        self.process = Chain()
        self.audit = Chain()
        self.report = Chain()

        self.commands.append(self.initialize)
        self.commands.append(self.authentication)
        self.commands.append(self.authorize)
        self.commands.append(self.validate)
        self.commands.append(self.process)
        self.commands.append(self.audit)
        self.commands.append(self.report)

    def execute(self, context: hash) -> bool:
        success = Command.SUCCESS
        error = None

        try:
            for command in self.commands:
                success = command.execute(context)
                if not success:
                    break
        except Exception as exc:
            success = Command.FAILURE
            error = exc
        finally:
            for command in self.commands[::-1]:
                command.post_execute(context, success, error)

        if error:
            raise error

        return success

    def post_execute(self, context: hash, success: bool, error: Exception) -> None:
        pass

    def add_initialize(self, command: Command) -> None:
        self.initialize.add(command)

    def add_authentication(self, command: Command) -> None:
        self.authentication.add(command)

    def add_authorize(self, command: Command) -> None:
        self.authorize.add(command)

    def add_validate(self, command: Command) -> None:
        self.validate.add(command)

    def add_process(self, command: Command) -> None:
        self.process.add(command)

    def add_audit(self, command: Command) -> None:
        self.audit.add(command)

    def add_report(self, command: Command) -> None:
        self.report.add(command)
