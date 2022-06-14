from vctm.chain import Command
from vctm.models import Base
from vctm.models import Organisation
from vctm.models import Project


class DatabaseCreateCommand(Command):
    def execute(self, context: hash) -> bool:
        engine = context['db_engine']

        Base.metadata.create_all(engine)

        context['message'] = f'Create DB'

        return Command.SUCCESS


class OrganisationAddCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']
        name = context['organisation_name']

        organisation = Organisation(name=name)
        session.add(organisation)

        context['message'] = f'Add Organisation: {name}'

        return Command.SUCCESS


class OrganisationDeleteCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']
        name = context['organisation_name']

        organisation = session.query(Organisation).filter(
            Organisation.name == name).one()
        session.delete(organisation)

        context['message'] = f'Delete Organisation: {name}'

        return Command.SUCCESS


class OrganisationListCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']

        organisations = session.query(Organisation).all()
        context['organisations'] = organisations

        return Command.SUCCESS


class ProjectAddCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']
        organisation_name = context['organisation_name']
        name = context['project_name']

        organisation = session.query(Organisation).filter(
            Organisation.name == organisation_name).one()
        project = Project(name=name, organisation=organisation)
        session.add(project)

        context['message'] = f'Add Project: {organisation_name}/{name}'

        return Command.SUCCESS


class ProjectClearCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']

        projects = session.query(Project).all()

        for project in projects:
            session.delete(project)

        return Command.SUCCESS


class ProjectDeleteCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']
        organisation_name = context['organisation_name']
        name = context['project_name']

        organisation = session.query(Organisation).filter(
            Organisation.name == organisation_name).one()
        project = session.query(Project).filter(
            Project.name == name, Project.organisation_id == organisation.organisation_id).one()
        session.delete(project)

        context['message'] = f'Delete Project: {organisation_name}/{name}'

        return Command.SUCCESS


class ProjectListCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context['db_session']

        if 'organisation_name' in context:
            organisation_name = context['organisation_name']
            organisation = session.query(Organisation).filter(
                Organisation.name == organisation_name).one()
            projects = session.query(Project).filter(
                Project.organisation_id == organisation.organisation_id).all()
            context['projects'] = projects
        else:
            projects = session.query(Project).all()
            context['projects'] = projects

        return Command.SUCCESS
