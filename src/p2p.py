from pythonp2p.node import PORT
from pythonp2p import Node


class local_node(Node):
    def __init__(self, host="", port=65432, file_port=65433):
        super().__init__(host, port, file_port)

    def send_message(self, data, reciever=None):
        return super().send_message(data, reciever)

    def start(self) -> None:
        return super().start()

    def on_message(self, data, sender, private):
        return super().on_message(data, sender, private)

    def connect_to(self, host, port=65432):
        return super().connect_to(host, port)

    def stop(self):
        return super().stop()
