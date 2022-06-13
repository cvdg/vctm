
from vctm.chain import Command
from vctm.models import JournalProject


class ProjectExistCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']
        name = context['project_name']

        exist = bool(session.query(JournalProject).filter(
            JournalProject.name == name).first())

        if not exist:
            context['message'] = f'Project {name} does not exist'
            return Command.FAILURE

        return Command.SUCCESS


class ProjectNotExistCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']
        name = context['project_name']

        exist = bool(session.query(JournalProject).filter(
            JournalProject.name == name).first())

        if exist:
            context['message'] = f'Project {name} does exist'
            return Command.FAILURE

        return Command.SUCCESS
