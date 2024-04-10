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
            click.echo(f"your path: {my_load}")

    def set_p2p(self):

        self.node.start()
        try: 
            with open("./saved_path.pickle", "rb") as f:
                my_load = pickle.load(f)
                try:

                    self.node.connect_to(host=my_load["ip"])
                    click.echo("Attempting to connect")
                    data = "waddup brotha"
                    self.node.send_message(data)

                    self.node.on_message(data, self.node.id,True)
                    click.echo("Connection succeeded")

                except Exception as e:
                    click.echo(f"Something went wrong: {e}")
        except Exception as err:
                click.echo(f"Failed fo perform: {err}")