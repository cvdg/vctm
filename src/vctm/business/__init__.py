from vctm.chain import Executor

from vctm.command.initialize import DatabaseCommand
from vctm.command.initialize import DirectoryCommand
from vctm.command.initialize import ExecutorCommand
from vctm.command.initialize import LoggingCommand

from vctm.command.authenticate import AuthenticateCommand

from vctm.command.report import ReportCommand
from vctm.command.report import DumpContextCommand


class BusinessLogic(Executor):
    def __init__(self, executor_name: str):
        super().__init__()

        self.add_initialize(ExecutorCommand(executor_name))
        self.add_initialize(DirectoryCommand())
        self.add_initialize(LoggingCommand())
        self.add_initialize(DatabaseCommand())

        self.add_authentication(AuthenticateCommand())

        self.add_report(ReportCommand())
        # self.add_report(DumpContextCommand())
