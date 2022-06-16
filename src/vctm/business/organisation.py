from vctm.business import BusinessLogic

from vctm.command.validate import OrganisationExistCommand
from vctm.command.validate import OrganisationNotExistCommand

from vctm.command.process import OrganisationAddCommand
from vctm.command.process import OrganisationDeleteCommand
from vctm.command.process import OrganisationListCommand


class OrganisationAddExecutor(BusinessLogic):
    def __init__(self):
        super().__init__("OrganisationAddExecutor")

        self.add_validate(OrganisationNotExistCommand())

        self.add_process(OrganisationAddCommand())


class OrganisationDeleteExecutor(BusinessLogic):
    def __init__(self):
        super().__init__("OrganisationDeleteExecutor")

        self.add_validate(OrganisationExistCommand())

        self.add_process(OrganisationDeleteCommand())


class OrganisationListExecutor(BusinessLogic):
    def __init__(self):
        super().__init__("OrganisationListExecutor")

        self.add_process(OrganisationListCommand())
