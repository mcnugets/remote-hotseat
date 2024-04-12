import click
import pickle


class cli:
    def __init__(self, node) -> None:
        self.node = node

    def set_configs(self):
        with open("./saved_path.pickle", "wb") as f:
            save = input("Input your save file path:")
            ip = input("Now input your ip to connect to:")
            data = {"path": save, "ip": ip}
            pickle.dump(data, f)

    def load_path(self):
        with open("./saved_path.pickle", "rb") as f:
            my_load = pickle.load(f)
            print(f"your path: {my_load}")

    def connect(self):
        with open("./saved_path.pickle", "rb") as f:
            my_load = pickle.load(f)
            try:

                self.node.connect_to(host=my_load["ip"])
                print("Connection succeeded")

            except Exception as e:
                click.echo(f"Something went wrong: {e}")

    def send_message(self, msg):
        try:

            self.node.send_message(msg, self.node.id)
            print('message has been sent')
            print('-------------')
            
        except Exception as e:
            print(e)

    def start(self):
        try:
            self.node.start()
        except Exception as e:
            print(e)

    def stop(self):
        try:
            self.node.stop()
        except Exception as e:
            print(e)

    
