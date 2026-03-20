import click, requests
@click.group()
def cli():
    """Registry for AI agents and skills."""
    pass
@cli.command()
@click.argument('query')
def search(query):
    click.echo(f"Searching for {query}...")
    click.echo("TODO: Query registry API")
@cli.command()
@click.argument('package')
def install(package):
    click.echo(f"Installing {package}...")
    click.echo("TODO: Download and install package")
if __name__ == "__main__":
    cli()
