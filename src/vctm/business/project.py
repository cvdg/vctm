
from vctm.chain import Executor

from vctm.command.initialize import DatabaseCommand
from vctm.command.initialize import DirectoryCommand
from vctm.command.initialize import LoggingCommand

from vctm.command.validate import ProjectExistCommand
from vctm.command.validate import ProjectNotExistCommand

from vctm.command.process import ProjectAddCommand
from vctm.command.process import ProjectClearCommand
from vctm.command.process import ProjectDeleteCommand
from vctm.command.process import ProjectListCommand

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


class ProjectAddExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_validate(ProjectNotExistCommand())

        self.add_process(ProjectAddCommand())


class ProjectDeleteExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_validate(ProjectExistCommand())

        self.add_process(ProjectDeleteCommand())


class ProjectListExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_process(ProjectListCommand())
