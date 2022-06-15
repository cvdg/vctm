from vctm.chain import Command
from vctm.models import Organisation
from vctm.models import Project


class OrganisationExistCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context["db_session"]
        organisation_name = context["organisation_name"]

        exist = bool(
            session.query(Organisation)
            .filter(Organisation.organisation_name == organisation_name)
            .first()
        )

        if not exist:
            context["message"] = f"Organisation {organisation_name} does not exist"
            return Command.FAILURE

        return Command.SUCCESS


class OrganisationNotExistCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context["db_session"]
        organisation_name = context["organisation_name"]

        exist = bool(
            session.query(Organisation)
            .filter(Organisation.organisation_name == organisation_name)
            .first()
        )

        if exist:
            context["message"] = f"Organisation {organisation_name} exist"
            return Command.FAILURE

        return Command.SUCCESS


class ProjectExistCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context["db_session"]
        organisation_name = context["organisation_name"]
        project_name = context["project_name"]

        organisation = (
            session.query(Organisation)
            .filter(Organisation.organisation_name == organisation_name)
            .one()
        )
        exist = bool(
            session.query(Project)
            .filter(
                Project.project_name == project_name,
                Project.organisation_id == organisation.organisation_id,
            )
            .first()
        )

        if not exist:
            context[
                "message"
            ] = f"Project {organisation_name}/{project_name} does not exist"
            return Command.FAILURE

        return Command.SUCCESS


class ProjectNotExistCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context["db_session"]
        organisation_name = context["organisation_name"]
        project_name = context["project_name"]

        organisation = (
            session.query(Organisation)
            .filter(Organisation.organisation_name == organisation_name)
            .one()
        )
        exist = bool(
            session.query(Project)
            .filter(
                Project.project_name == project_name,
                Project.organisation_id == organisation.organisation_id,
            )
            .first()
        )

        if exist:
            context["message"] = f"Project {organisation_name}/{project_name} exist"
            return Command.FAILURE

        return Command.SUCCESS
