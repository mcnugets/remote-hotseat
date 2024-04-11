import json
import asyncio
import socket
import threading
import click
from pythonp2p import file_transfer
from pythonp2p.node import *

from src.functionality import cli


if __name__ == "__main__":
    node = Node("192.168.2.114", PORT, FILE_PORT)
    cmds = cli(node)
   