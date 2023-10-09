import click
from clients import commands as clients_commands


CLIENTS_TABLE = '.clients.csv'


@click.group()    # entry point
@click.pass_context    # objeto con texto
def cli(ctx):
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(clients_commands.all)
