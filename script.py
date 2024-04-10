import json
import asyncio
import socket
import threading
import click

from src.functionality import cli 
from src.p2p import local_node


@click.group()
def clis():
    pass


@clis.command(help="sets the main configuration to get started like: ip and path")
def c1():
    cmd.set_configs()


@clis.command(help="command for loading a path( for testing)")
def c2():
    cmd.load_path()


@clis.command(help="sets the p2p connection")
def c3():
    cmd.set_p2p()


if __name__ == "__main__":
    node = local_node()
    cmd = cli(node)
    clis()
