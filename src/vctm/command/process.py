from vctm.chain import Command

from vctm.models import Base
from vctm.models import Directory
from vctm.models import Organisation
from vctm.models import Project
from vctm.models import Entry


class DatabaseCreateCommand(Command):
    def execute(self, context: hash) -> bool:
        """Create the database schema"""
        engine = context["db_engine"]

        Base.metadata.create_all(engine)

        context["message"] = f"Create DB"

        return Command.SUCCESS


class OrganisationAddCommand(Command):
    def execute(self, context: hash) -> bool:
        """Add a new organisation"""
        session = context["db_session"]
        organisation_name = context["organisation_name"]

        organisation = Organisation(organisation_name=organisation_name)
        session.add(organisation)

        context["message"] = f"Add Organisation: {organisation_name}"

        return Command.SUCCESS


class OrganisationDeleteCommand(Command):
    def execute(self, context: hash) -> bool:
        """Delete an organisation"""
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
        """List all organisations"""
        session = context["db_session"]

        organisations = session.query(Organisation).all()
        context["organisations"] = organisations

        return Command.SUCCESS


class ProjectAddCommand(Command):
    def execute(self, context: hash) -> bool:
        """Add a new project for an organisation"""
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
        """Delete a project from an organisation"""
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
        """List all projects"""
        session = context["db_session"]

        projects = session.query(Project).all()

        context["projects"] = projects

        return Command.SUCCESS


class ProjectListByOrganisationCommand(Command):
    def execute(self, context: hash) -> bool:
        """List all projects for an organisation"""
        session = context["db_session"]
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

        context["projects"] = projects

        return Command.SUCCESS


class DirectoryAddCommand(Command):
    def execute(self, context: hash) -> bool:
        """Add the current directory to an organisation and project"""
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

        context["message"] = f"Add Directory: {directory_name}"

        return Command.SUCCESS


class DirectoryDeleteCommand(Command):
    def execute(self, context: hash) -> bool:
        """Delete a directory"""
        session = context["db_session"]
        directory_name = context["directory_name"]

        directory = (
            session.query(Directory)
            .filter(Directory.directory_name == directory_name)
            .one()
        )

        session.delete(directory)

        context["message"] = f"Delete Directory: {directory_name}"

        return Command.SUCCESS


class DirectoryInfoCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context["db_session"]
        directory_name = context["directory_name"]

        directory = (
            session.query(Directory)
            .filter(Directory.directory_name == directory_name)
            .one()
        )

        context["directory"] = directory
        context["organisation_name"] = directory.project.organisation.organisation_name
        context["project_name"] = directory.project.project_name

        return Command.SUCCESS


class DirectoryListCommand(Command):
    def execute(self, context: hash) -> bool:
        """List all directories"""
        session = context["db_session"]

        directories = session.query(Directory).all()
        context["directories"] = directories

        return Command.SUCCESS


class EntryAddCommand(Command):
    def execute(self, context: hash) -> bool:
        """Add the entry to an organisation and project"""
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
                Project.project_name == project_name,
                Project.organisation == organisation,
            )
            .one()
        )

        entry = Entry(project=project)
        session.add(entry)
        context["entry"] = entry

        context["message"] = f"Add Entry: {entry.entry_id}"

        return Command.SUCCESS


class EntryDeleteCommand(Command):
    def execute(self, context: hash) -> bool:
        """Delete an entry"""
        session = context["db_session"]
        entry_id = context["entry_id"]

        entry = session.query(Entry).filter(Entry.entry_id == entry_id).one()
        session.delete(entry)

        context["message"] = f"Delete Entry: {entry_id}"

        return Command.SUCCESS


class EntryListCommand(Command):
    def execute(self, context: hash) -> bool:
        """List all entries"""
        session = context["db_session"]

        entries = session.query(Entry).all()
        context["entries"] = entries

        return Command.SUCCESS
