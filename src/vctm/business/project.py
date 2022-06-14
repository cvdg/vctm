from vctm.command.validate import OrganisationExistCommand
from vctm.command.validate import ProjectExistCommand
from vctm.command.validate import ProjectNotExistCommand

from vctm.command.process import ProjectAddCommand
from vctm.command.process import ProjectClearCommand
from vctm.command.process import ProjectDeleteCommand
from vctm.command.process import ProjectListCommand

from vctm.business import BusinessLogic


class ProjectAddExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_validate(OrganisationExistCommand())
        self.add_validate(ProjectNotExistCommand())

        self.add_process(ProjectAddCommand())


class ProjectDeleteExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_validate(OrganisationExistCommand())
        self.add_validate(ProjectExistCommand())

        self.add_process(ProjectDeleteCommand())


class ProjectListExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_process(ProjectListCommand())
