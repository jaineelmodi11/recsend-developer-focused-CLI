import click
from recsend.commands.send import send_request_cmd

@click.group(help="recsend: CLI for testing your movie-rec backend")
def cli():
    pass

cli.add_command(send_request_cmd)

if __name__ == "__main__":
    cli()
