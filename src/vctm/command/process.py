
from vctm.chain import Command
from vctm.models import JournalProject


class ProjectAddCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']
        name = context['project_name']

        project = JournalProject(name = name)
        session.add(project)

        context['message'] = f'- Add Project: {name}'

        return Command.SUCCESS


class ProjectClearCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']

        projects = session.query(JournalProject).all()

        for project in projects:
            session.delete(project)

        return Command.SUCCESS


class ProjectDeleteCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']
        name = context['project_name']

        project = session.query(JournalProject).filter(JournalProject.name == name).one()
        session.delete(project)

        context['message'] = f'Delete Project: {name}'

        return Command.SUCCESS


class ProjectListCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']

        projects = session.query(JournalProject).all()
        context['projects'] = projects

        return Command.SUCCESS
