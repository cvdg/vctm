from vctm.command.process import DatabaseCreateCommand

from vctm.business import BusinessLogic


class DatabaseCreateExecutor(BusinessLogic):
    def __init__(self):
        super().__init__()

        self.add_process(DatabaseCreateCommand())
