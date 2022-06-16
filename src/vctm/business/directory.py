from vctm.business import BusinessLogic

from vctm.command.validate import OrganisationExistCommand
from vctm.command.validate import ProjectExistCommand
from vctm.command.validate import DirectoryExistCommand
from vctm.command.validate import DirectoryNotExistCommand

from vctm.command.process import DirectoryAddCommand
from vctm.command.process import DirectoryDeleteCommand
from vctm.command.process import DirectoryInfoCommand
from vctm.command.process import DirectoryListCommand


class DirectoryAddExecutor(BusinessLogic):
    def __init__(self):
        super().__init__("DirectoryAddExecutor")

        self.add_validate(OrganisationExistCommand())
        self.add_validate(ProjectExistCommand())
        self.add_validate(DirectoryNotExistCommand())

        self.add_process(DirectoryAddCommand())


class DirectoryDeleteExecutor(BusinessLogic):
    def __init__(self):
        super().__init__("DirectoryDeleteExecutor")

        self.add_validate(DirectoryExistCommand())

        self.add_process(DirectoryDeleteCommand())


class DirectoryInfoExecutor(BusinessLogic):
    def __init__(self):
        super().__init__("DirectoryInfoExecutor")

        self.add_validate(DirectoryExistCommand())

        self.add_process(DirectoryInfoCommand())


class DirectoryListExecutor(BusinessLogic):
    def __init__(self):
        super().__init__("DirectoryListExecutor")

        self.add_process(DirectoryListCommand())
