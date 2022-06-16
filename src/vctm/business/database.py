from vctm.business import BusinessLogic

from vctm.command.process import DatabaseCreateCommand


class DatabaseCreateExecutor(BusinessLogic):
    def __init__(self):
        super().__init__("DatabaseCreateExecutor")

        self.add_process(DatabaseCreateCommand())
