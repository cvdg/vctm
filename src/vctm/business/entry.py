from vctm.business import BusinessLogic

from vctm.command.validate import DirectoryExistCommand

from vctm.command.process import DirectoryInfoCommand

from vctm.command.process import EntryAddCommand
from vctm.command.process import EntryListCommand


class EntryAddExecutor(BusinessLogic):
    def __init__(self):
        super().__init__("EntryAddExecutor")

        self.add_validate(DirectoryExistCommand())

        self.add_process(DirectoryInfoCommand())
        self.add_process(EntryAddCommand())


class EntryListExecutor(BusinessLogic):
    def __init__(self):
        super().__init__("EntryListExecutor")

        self.add_process(EntryListCommand())
