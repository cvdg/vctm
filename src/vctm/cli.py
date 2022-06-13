
import click

from vctm.business.project import ProjectAddExecutor
from vctm.business.project import ProjectDeleteExecutor
from vctm.business.project import ProjectListExecutor


@click.group()
def cli() -> None:
    pass


@cli.group()
def project() -> None:
    """ Project commands """
    pass


@project.command('add')
@click.argument('name')
def project_add(name: str) -> None:
    """ Add a new project. """
    executor = ProjectAddExecutor()
    context = executor.get_context()
    context['project_name'] = name

    executor.execute(context)


@project.command('delete')
@click.argument('name')
def project_delete(name: str) -> None:
    """ Delete a project. """
    executor = ProjectDeleteExecutor()
    context = executor.get_context()
    context['project_name'] = name

    executor.execute(context)


@project.command('list')
def project_list() -> None:
    """ List all projects. """
    executor = ProjectListExecutor()
    context = executor.get_context()

    executor.execute(context)

    for project in context['projects']:
        print(f'{project.id:3d}: {project.name}')


if __name__ == '__main__':
    cli()
