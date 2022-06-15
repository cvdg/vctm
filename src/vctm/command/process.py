from vctm.chain import Command
from vctm.models import Base, Directory
from vctm.models import Organisation
from vctm.models import Project


class DatabaseCreateCommand(Command):
    def execute(self, context: hash) -> bool:
        """Creates the database schema"""
        engine = context["db_engine"]

        Base.metadata.create_all(engine)

        context["message"] = f"Create DB"

        return Command.SUCCESS


class OrganisationAddCommand(Command):
    def execute(self, context: hash) -> bool:
        """Adds a new organisation"""
        session = context["db_session"]
        organisation_name = context["organisation_name"]

        organisation = Organisation(organisation_name=organisation_name)
        session.add(organisation)

        context["message"] = f"Add Organisation: {organisation_name}"

        return Command.SUCCESS


class OrganisationDeleteCommand(Command):
    def execute(self, context: hash) -> bool:
        """Deletes an organisation"""
        session = context["db_session"]
        organisation_name = context["organisation_name"]

        organisation = (
            session.query(Organisation)
            .filter(Organisation.organisation_name == organisation_name)
            .one()
        )
        session.delete(organisation)

        context["message"] = f"Delete Organisation: {organisation_name}"

        return Command.SUCCESS


class OrganisationListCommand(Command):
    def execute(self, context: hash) -> bool:
        """Lists all organisations"""
        session = context["db_session"]

        organisations = session.query(Organisation).all()
        context["organisations"] = organisations

        return Command.SUCCESS


class ProjectAddCommand(Command):
    def execute(self, context: hash) -> bool:
        """Adds a new project for an organisation"""
        session = context["db_session"]
        organisation_name = context["organisation_name"]
        project_name = context["project_name"]

        organisation = (
            session.query(Organisation)
            .filter(Organisation.organisation_name == organisation_name)
            .one()
        )
        project = Project(project_name=project_name, organisation=organisation)
        session.add(project)

        context["message"] = f"Add Project: {organisation_name}/{project_name}"

        return Command.SUCCESS


class ProjectDeleteCommand(Command):
    def execute(self, context: hash) -> bool:
        """Deletes a project from an organisation"""
        session = context["db_session"]
        organisation_name = context["organisation_name"]
        project_name = context["project_name"]

        organisation = (
            session.query(Organisation)
            .filter(Organisation.organisation_name == organisation_name)
            .one()
        )
        project = (
            session.query(Project)
            .filter(
                Project.name == project_name,
                Project.organisation_id == organisation.organisation_id,
            )
            .one()
        )
        session.delete(project)

        context["message"] = f"Delete Project: {organisation_name}/{project_name}"

        return Command.SUCCESS


class ProjectListCommand(Command):
    def execute(self, context: hash) -> bool:
        """Lists all projects, optional lists all projects for an organisation"""
        session = context["db_session"]

        if "organisation_name" in context:
            organisation_name = context["organisation_name"]
            organisation = (
                session.query(Organisation)
                .filter(Organisation.organisation_name == organisation_name)
                .one()
            )
            projects = (
                session.query(Project)
                .filter(Project.organisation_id == organisation.organisation_id)
                .all()
            )
        else:
            projects = session.query(Project).all()

        context["projects"] = projects

        return Command.SUCCESS


class DirectoryAddCommand(Command):
    def execute(self, context: hash) -> bool:
        """Adds the current directory to an organisation and project"""
        session = context["db_session"]
        organisation_name = context["organisation_name"]
        project_name = context["project_name"]
        directory_name = context["directory_name"]

        organisation = (
            session.query(Organisation)
            .filter(Organisation.organisation_name == organisation_name)
            .one()
        )
        project = (
            session.query(Project)
            .filter(
                Project.project_name == project_name,
                Project.organisation == organisation,
            )
            .one()
        )
        directory = Directory(directory_name=directory_name, project=project)
        session.add(directory)

        context[
            "message"
        ] = f"Add Directory: {organisation_name}/{project_name}: {directory_name}"

        return Command.SUCCESS


class DirectoryInfoCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context["db_session"]
        directory_name = context["directory_name"]

        directory = session.query(Directory).filter(Directory.directory_name == directory_name).one()

        context["directory"] = directory

        return Command.SUCCESS
