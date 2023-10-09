import click
from clients.services import ClientService
from clients.models import Client


@click.group
def clients():
    """Manages the client lifecycle"""
    pass


@clients.command()
@click.option(
    '-n', '--name',
    type = str,
    prompt = True,
    help = "Client's name")
@click.option(
    '-a', '--address',
    type = str,
    prompt = True,
    help = "Client's address")
@click.option(
    '-e', '--email',
    type = str,
    prompt = True,
    help = "Client's email")
@click.option(
    '-p', '--number',
    type = str,
    prompt = True,
    help = "Client's number")
@click.pass_context
def create(ctx, name, address, email, number):
    """Creates a new client"""
    client = Client(name, address, email, number)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)


@clients.command()
@click.pass_context
def read_list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()

    click.echo(f'|        id        |  NAME  |  ADDRESS  |  EMAIL  | NUMBER')
    click.echo('-' * 60)

    for client in clients_list:
        click.echo('{uid} | {name} | {address} | {email} | {number}'.format(
            uid = client['uid'],
            name = client['name'],
            address = client['address'],
            email = client['email'],
            number = client['number']))


@clients.command()
@click.option('-u', 'uid',
    type = str,
    prompt = True,
    help = "Client's uid")
@click.pass_context
def update(ctx, uid:str):
    """Updates a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    client = [client for client in client_list if client['uid'] == uid]

    if client:
        client = _updated_client_flow(Client(**client[0]))
        client_service.update_client(client)
        click.echo('Client updated')
    else:
        click.echo('Client not found')


def _updated_client_flow(client):
    click.echo('Leave empty if you dont want to modify values')
    client.name = click.prompt('New Name', type = str, default = client.name)
    client.address = click.prompt('New Address', type = str, default = client.address)
    client.email = click.prompt('New Email', type = str, default = client.email)
    client.number = click.prompt('New Number', type = str, default = client.number)

    return client


@clients.command()
@click.option('-u', 'uid',
    type = str,
    prompt = True,
    help = "Client's uid")
@click.pass_context
def delete(ctx, uid:str):
    """Delete a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    client = [client for client in client_list if client['uid'] == uid]
    
    if client:
        client = Client(**client[0])
        client = client_service.delete_client(client)
        click.echo('Client has been deleted')
    else:
        click.echo('Client not found')


all = clients
