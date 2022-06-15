from vctm.business import BusinessLogic

from vctm.command.validate import OrganisationExistCommand
from vctm.command.validate import ProjectExistCommand
from vctm.command.validate import DirectoryExistCommand
from vctm.command.validate import DirectoryNotExistCommand

from vctm.command.process import DirectoryAddCommand
from vctm.command.process import DirectoryInfoCommand


class DirectoryAddExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_validate(OrganisationExistCommand())
        self.add_validate(ProjectExistCommand())
        self.add_validate(DirectoryNotExistCommand())

        self.add_process(DirectoryAddCommand())


class DirectoryInfoExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_validate(DirectoryExistCommand())

        self.add_process(DirectoryInfoCommand())
