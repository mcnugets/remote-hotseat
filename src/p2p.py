from pythonp2p.node import *
from pythonp2p import Node
import click
import threading

from pythonp2p.node import FILE_PORT, PORT


class local_node(Node):
    def __init__(self, host="", port=PORT, file_port=FILE_PORT):
        super().__init__(host, port, file_port)

    def send_message(self, data, reciever):
        return super().send_message(data, reciever)

    def start(self) -> None:
        return super().start()

    def requestFile(self, fhash):
        return super().requestFile(fhash)

    def on_message(self, message, sender, private):
        try:
            type_ = message["type"]
            if type_ == "msg":
                msg = f"{message['me']}> {message['msg']}"
                return super().on_message(msg, sender, private)
            if type_ == "file":
                msg = f"{message['me']}> {message['filehash']}"
                self.requestFile(message["filehash"])
            return super().on_message(msg, sender, private)

        except Exception as e:
            print(e)

    def connect_to_ports(self, host, ports=[PORT, FILE_PORT]):
        return super().connect_to_ports(host, ports)

    def stop(self):
        return super().stop()
