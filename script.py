import click
import pickle
import json
import asyncio
import socket
from pythonp2p import Node
import threading

from pythonp2p.node import PORT


class local_node(Node):
    def __init__(self, host="", port=65432, file_port=65433):
        super().__init__(host, port, file_port)

    def send_message(self, data, reciever=None):
        return super().send_message(data, reciever)

    def start(self) -> None:
        return super().start()

    def on_message(self, data, sender, private):
        return super().on_message(data, sender, private)

    def connect_to(self, host, port=...):
        return super().connect_to(host, port)

    def stop(self):
        return super().stop()


# click based class
class cli(click.Group):
    def __init__(self, node) -> None:
        self.node = node

    @click.command()
    def set_configs(self):
        with open("saved_path.pickle", "wb") as f:
            save = input("Input your save file path:")
            ip = input("Now input your ip to connect to:")
            data = {"path": save, "ip": ip}
            pickle.dump(data, f)

    @click.command()
    def load_path(self):
        with open("saved_path.pickle", "rb") as f:
            my_load = pickle.load(f)
            click.echo(f"your path: {my_load}")

    @click.command()
    def set_p2p(self):
        ln = local_node()
        ln.start()
        with open("saved_path.pickle", "rb") as f:
            my_load = pickle.load(f)
            try:

                ln.connect_to(host=my_load["ip"])
                ln.send_message(data="WADUP BROTHA")

                ln.on_message()
                click.echo("Connection succeeded")

            except Exception as e:
                click.echo(f"Something went wrong: {e}")

    def get_context(self):
        ctx = click.get_current_context()
        if not ctx:
            raise click.ClickException("Not called from a Click context")
        return ctx


if __name__ == "__main__":
    ln = local_node()
    clis = cli(ln)
    while True:
        user_input = input("Enter your cli command: ")
        if user_input == "exit":
            ln.stop()
            break
        clis()
