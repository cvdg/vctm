from vctm.command.validate import OrganisationExistCommand
from vctm.command.validate import OrganisationNotExistCommand

from vctm.command.process import OrganisationAddCommand
from vctm.command.process import OrganisationDeleteCommand
from vctm.command.process import OrganisationListCommand

from vctm.business import BusinessLogic


class OrganisationAddExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_validate(OrganisationNotExistCommand())

        self.add_process(OrganisationAddCommand())


class OrganisationDeleteExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_validate(OrganisationExistCommand())

        self.add_process(OrganisationDeleteCommand())


class OrganisationListExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_process(OrganisationListCommand())
