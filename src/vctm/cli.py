
import logging

import click

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from vctm.models import Base, JournalProject
from vctm.setup import initialize, config

initialize()

_logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--name', '-n', default='World')
def hello(name) -> None:
    """ Say Hello. """
    _logger.info(f'Hello, {name}!')


@cli.command()
def db_init() -> None:
    """ Init DB schema """

    engine = create_engine(
        f'sqlite:///{config["db_name"]}', echo=True, future=True)
    Base.metadata.create_all(engine)

    _logger.info(f'Init DB: {config["db_name"]}')


@cli.group()
def project() -> None:
    """ Project commands. """
    pass


@project.command('add')
@click.argument('name')
def project_add(name: str) -> None:
    """ Add a new project. """

    engine = create_engine(f'sqlite:///{config["db_name"]}', future=True)

    with Session(engine) as session:
        prj = JournalProject(name=name)
        session.add(prj)
        session.commit()

    _logger.info(f'Project add: {name}')


@project.command('delete')
@click.argument('name')
def project_delete(name: str) -> None:
    """ Delete a project. """

    engine = create_engine(f'sqlite:///{config["db_name"]}', future=True)

    with Session(engine) as session:
        result = session.query(JournalProject).filter(
            JournalProject.name == name).one()
        session.delete(result)
        session.commit()

    _logger.info(f'Project delete: {name}')


@project.command('list')
def project_list() -> None:
    """ List all projects. """

    engine = create_engine(f'sqlite:///{config["db_name"]}', future=True)

    with Session(engine) as session:
        result = session.query(JournalProject).order_by(
            JournalProject.name).all()
        for prj in result:
            print(f'{prj.id:3d}: {prj.name}')

        session.commit()


if __name__ == '__main__':
    cli()
