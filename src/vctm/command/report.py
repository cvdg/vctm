import logging

from vctm.chain import Command


class ReportCommand(Command):
    logger = logging.getLogger(__name__)

    def post_execute(self, context: hash, success: bool, error: Exception) -> None:
        if "username" in context:
            username = context["username"]
        else:
            username = "Unknown"

        if "message" in context:
            message = context["message"]
        else:
            message = None

        if error:
            self.logger.exception(error)
        elif not success:
            if message:
                self.logger.warning(f"[{username}] Failure: {message}")
            else:
                self.logger.warning(f"[{username}] Failure")
        else:
            if message:
                self.logger.info(f"[{username}] Success: {message}")
            else:
                self.logger.info(f"[{username}] Success")
