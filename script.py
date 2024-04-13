import json
import asyncio
import socket
import threading
import click
from src.p2p import local_node
from src.functionality import cli
import sys


def clear_terminal():
    # Clear command for Windows ('cls') and UNIX ('clear')
    os.system("cls" if os.name == "nt" else "clear")


# Example usage

if __name__ == "__main__":
    try:
        node = local_node()
        cmds = cli(node)

        while True:
            cmd = input("hotseat>")

            if cmd == "start":
                cmds.start()

            if cmd == "connect":
                cmds.connect()

            if cmd == "send":
                msg = input("your message:")
                cmds.send_message(msg=msg)
            if cmd == "set":
                cmds.set_configs()

            if cmd == "load":
                cmds.load_path()

            if cmd == "exit":
                cmds.stop()
                break

    except Exception as e:
        print(e)
