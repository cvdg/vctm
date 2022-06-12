
import click


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--name', '-n', default='World')
def hello(name) -> None:
    click.echo(f'Hello, {name}!')


if __name__ == '__main__':
    cli()
