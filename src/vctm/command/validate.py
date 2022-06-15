from vctm.chain import Command
from vctm.models import Organisation
from vctm.models import Project


class OrganisationExistCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context["db_session"]
        name = context["organisation_name"]

        exist = bool(
            session.query(Organisation).filter(Organisation.name == name).first()
        )

        if not exist:
            context["message"] = f"Organisation {name} does not exist"
            return Command.FAILURE

        return Command.SUCCESS


class OrganisationNotExistCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context["db_session"]
        name = context["organisation_name"]

        exist = bool(
            session.query(Organisation).filter(Organisation.name == name).first()
        )

        if exist:
            context["message"] = f"Organisation {name} does exist"
            return Command.FAILURE

        return Command.SUCCESS


class ProjectExistCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context["db_session"]
        organisation_name = context["organisation_name"]
        name = context["project_name"]

        organisation = (
            session.query(Organisation)
            .filter(Organisation.name == organisation_name)
            .one()
        )
        exist = bool(
            session.query(Project)
            .filter(
                Project.name == name,
                Project.organisation_id == organisation.organisation_id,
            )
            .first()
        )

        if not exist:
            context["message"] = f"Project {organisation_name}/{name} does not exist"
            return Command.FAILURE

        return Command.SUCCESS


class ProjectNotExistCommand(Command):
    def execute(self, context: hash) -> bool:
        session = context["db_session"]
        organisation_name = context["organisation_name"]
        name = context["project_name"]

        organisation = (
            session.query(Organisation)
            .filter(Organisation.name == organisation_name)
            .one()
        )
        exist = bool(
            session.query(Project)
            .filter(
                Project.name == name,
                Project.organisation_id == organisation.organisation_id,
            )
            .first()
        )

        if exist:
            context["message"] = f"Project {organisation_name}/{name} exist"
            return Command.FAILURE

        return Command.SUCCESS
