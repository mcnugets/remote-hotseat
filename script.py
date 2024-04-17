import json
import asyncio
import socket
import threading
import click
from src.p2p import local_node
from src.functionality import cli
import time


# Example usage


def main():
    try:

        node = local_node()

        cmds = cli(node)

        
        cmds.set_me()
        print("--------------------------")
        print("WELCOME TO WHATEVER THIS IS")
        print("--------------------------")
        print(
            "to familiarize yourself with comamnds for the program you can type: help"
        )
        print("\n")

        while True:
            input_cmd = input("hotseat>")

            cmd = input_cmd.split()

            if cmd[0] == "start":
                cmds.start()

            if cmd[0] == "connect":
                if len(cmd) > 1:
                    cmds.connect(user=cmd[1])
                else:
                    print(
                        "you forgot who you wanna connect to. for guidance refer to command 'help'"
                    )

            if cmd[0] == "send":
                if len(cmd) > 1:
                    msg = input("your message:")
                    cmds.send_message(user=cmd[1], msg=msg)
                else:
                    print("You forgot the name of the receiver")

            if cmd[0] == "set":
                cmds.set_configs()

            if cmd[0] == "peers":
                print("\n")
                for a in node.nodes_connected:
                    print(a.id)
                    print("----------")
                    print(a.host)
            if cmd[0] == "load":
                cmds.load_path()

            if cmd[0] == "q":
                cmds.stop()
                break
            print("\n")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
