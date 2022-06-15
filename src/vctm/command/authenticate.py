from vctm.chain import Command


class AuthenticateCommand(Command):
    """Authentication is done by the application"""

    def execute(self, context: hash) -> bool:
        """Check if a username is available"""
        if "username" in context:
            return Command.SUCCESS
        else:
            context["message"] = "User is unknown"
            return Command.FAILURE
