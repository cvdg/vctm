import logging

from vctm.chain import Command


class ReportCommand(Command):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def post_execute(self, context: hash, success: bool, error: Exception) -> None:
        executor = context["executor"]
        if "username" in context:
            username = context["username"]
        else:
            username = "???"

        if "message" in context:
            message = context["message"]
        else:
            message = None

        if error:
            self.logger.exception(error)
        elif not success:
            if message:
                self.logger.warning(f"[{username}] {executor} Failure: {message}")
            else:
                self.logger.warning(f"[{username}] {executor} Failure")
        else:
            if message:
                self.logger.info(f"[{username}] {executor} Success: {message}")
            else:
                self.logger.info(f"[{username}] {executor} Success")


class DumpContextCommand(Command):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def post_execute(self, context: hash, success: bool, error: Exception) -> None:
        for key in context:
            value = context[key]
            self.logger.info(f"Key: {key}, Value: {value}")
