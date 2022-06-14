
import click

from vctm.business.database import DatabaseCreateExecutor

from vctm.business.organisation import OrganisationAddExecutor
from vctm.business.organisation import OrganisationDeleteExecutor
from vctm.business.organisation import OrganisationListExecutor

from vctm.business.project import ProjectAddExecutor
from vctm.business.project import ProjectDeleteExecutor
from vctm.business.project import ProjectListExecutor


@click.group()
def cli() -> None:
    pass


@cli.group()
def database() -> None:
    """ Database commands """
    pass


@database.command('create')
def database_create() -> None:
    """ Create a new database. """
    executor = DatabaseCreateExecutor()
    context = executor.get_context()

    executor.execute(context)


@cli.group()
def organisation() -> None:
    """ Organisation commands """
    pass


@organisation.command('add')
@click.argument('name')
def organisation_add(name: str) -> None:
    """ Add a new organisation. """
    executor = OrganisationAddExecutor()
    context = executor.get_context()
    context['organisation_name'] = name

    executor.execute(context)

@organisation.command('delete')
@click.argument('name')
def organisation_delete(name: str) -> None:
    """ Delete a organisation. """
    executor = OrganisationDeleteExecutor()
    context = executor.get_context()
    context['organisation_name'] = name

    executor.execute(context)


@organisation.command('list')
def project_list() -> None:
    """ List all organisation. """
    executor = OrganisationListExecutor()
    context = executor.get_context()

    executor.execute(context)

    for organisation in context['organisations']:
        print(f'{organisation.organisation_id:3d}: {organisation.name}')


@cli.group()
def project() -> None:
    """ Project commands """
    pass


@project.command('add')
@click.argument('organisation')
@click.argument('name')
def project_add(organisation: str, name: str) -> None:
    """ Add a new project. """
    executor = ProjectAddExecutor()
    context = executor.get_context()
    context['organisation_name'] = organisation
    context['project_name'] = name

    executor.execute(context)


@project.command('delete')
@click.argument('organisation')
@click.argument('name')
def project_delete(organisation: str, name: str) -> None:
    """ Delete a project. """
    executor = ProjectDeleteExecutor()
    context = executor.get_context()
    context['organisation_name'] = organisation
    context['project_name'] = name

    executor.execute(context)


@project.command('list')
@click.option('-o', '--organisation', help='name of the organisation')
def project_list(organisation: str) -> None:
    """ List all projects. """
    executor = ProjectListExecutor()
    context = executor.get_context()

    if organisation:
        context['organisation_name'] = organisation

    executor.execute(context)

    print('| ' + 'id'.rjust(3) + ' | ' + 'organisation'.rjust(12) + ' | ' + 'project'.ljust(12) + ' |')
    print('| ' + '-' * 3 + ' | ' + '-' * 12 + ' | ' + '-' * 12 + ' |' )
    for project in context['projects']:
        print(f'| {project.project_id:3d} | {project.organisation.name: >12} | {project.name: <12} |')


if __name__ == '__main__':
    cli()
