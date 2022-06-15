import random
import string

from sqlalchemy.orm import Session

from vctm.chain import Command, Executor
from vctm.command.initialize import DatabaseCommand, DirectoryCommand
from vctm.models import Project


class SuccessCommand(Command):
    def execute(self, context: hash) -> bool:
        return Command.SUCCESS


class FailureCommand(SuccessCommand):
    def execute(self, context: hash) -> bool:
        return Command.FAILURE


class ProjectCommand(Command):
    def execute(self, context: hash) -> bool:
        name = "".join(random.choice(string.ascii_letters) for i in range(16))
        prj = Project(name=name)

        session = context["db_session"]
        session.add(prj)

        context["project_name"] = name

        return Command.SUCCESS


def test_database_command00():
    executor = Executor()
    executor.add_initialize(DirectoryCommand())
    executor.add_initialize(DatabaseCommand())
    executor.add_process(SuccessCommand())

    context = {}

    assert executor.execute(context)
    assert "db_session" in context


def test_database_command01():
    executor = Executor()
    executor.add_initialize(DirectoryCommand())
    executor.add_initialize(DatabaseCommand())
    executor.add_process(FailureCommand())

    context = {}

    assert not executor.execute(context)
    assert "db_session" in context


def test_database_command02():
    executor = Executor()
    executor.add_initialize(DirectoryCommand())
    executor.add_initialize(DatabaseCommand())
    executor.add_process(ProjectCommand())
    executor.add_process(SuccessCommand())

    context = {}

    assert executor.execute(context)
    assert "db_engine" in context
    assert "db_session" in context
    assert "project_name" in context

    engine = context["db_engine"]
    name = context["project_name"]

    with Session(engine) as session:
        result = session.query(Project).filter(Project.name == name).one()
        assert result.name == name
        session.delete(result)
        session.commit()


def test_database_command03():
    executor = Executor()
    executor.add_initialize(DirectoryCommand())
    executor.add_initialize(DatabaseCommand())
    executor.add_process(ProjectCommand())
    executor.add_process(FailureCommand())

    context = {}

    assert not executor.execute(context)
    assert "db_engine" in context
    assert "db_session" in context
    assert "project_name" in context

    engine = context["db_engine"]
    name = context["project_name"]

    with Session(engine) as session:
        result = session.query(Project).filter(Project.name == name).first()
        assert result is None
        session.commit()
