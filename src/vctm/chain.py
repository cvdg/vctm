"""
Chain of Command pattern.
"""

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
