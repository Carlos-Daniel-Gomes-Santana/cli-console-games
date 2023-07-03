"""
    Author: Carlos Daniel Gomes Santana
    Description: A CLI to execute the games
"""
import click


@click.group()
def app():
    """Group to CLI commands"""


@app.command()
def hello():
    """Say a hello world"""
    click.echo("Hello World")


if __name__ == "__main__":
    app()
