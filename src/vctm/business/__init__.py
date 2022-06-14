from vctm.chain import Executor

from vctm.command.initialize import DatabaseCommand
from vctm.command.initialize import DirectoryCommand
from vctm.command.initialize import LoggingCommand


from vctm.command.report import ReportCommand


class BusinessLogic(Executor):
    def __init__(self):
        super().__init__()

        self.add_initialize(DirectoryCommand())
        self.add_initialize(LoggingCommand())
        self.add_initialize(DatabaseCommand())

        self.add_report(ReportCommand())

        self.context = {}

    def get_context(self) -> hash:
        return self.context
