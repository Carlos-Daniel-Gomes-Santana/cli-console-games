import click


@click.group()
def app(): ...


@app.command()
def hello():
    """say a hello world"""
    click.echo("Hello World")


if __name__ == "__main__":
    app()
