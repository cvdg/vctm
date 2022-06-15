from vctm.chain import Command


class AuthenticateCommand(Command):
    def execute(self, context: hash) -> bool:
        if "username" in context:
            return Command.SUCCESS
        else:
            context["message"] = "User is unknown"
            return Command.FAILURE
