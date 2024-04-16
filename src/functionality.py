import click
import pickle
import threading
import pandas as pd
import os


class cli:
    def __init__(self, node) -> None:
        self.node = node

    def set_me(self):

        filename = "./saved_path.pickle"

        if os.path.exists(filename):
            try:
                with open(filename, "rb") as f:
                    dict = pickle.load(f)
            except EOFError:
                dict = {}
        else:
            dict = {}

        try:
            with open(filename, "wb") as f:
                if "me" not in dict:
                    me = input("Set your name please: ")
                    dict["me"] = me
                    pickle.dump(dict, f)

        except Exception as e:
            print(f"Oops something went wrong: {e}")

    def set_configs(self):
        with open("./saved_path.pickle", "wb") as f:
            save = input("Input your save file path:")
            print("--------")
            n_peers = input("how many peers: ")
            peers = {}
            for i in range(n_peers):
                user = input("user: ")
                ip = input("ip: ")
                peers[user] = ip

            data = {"path": save, "ip": peers}
            pickle.dump(data, f)

    def load_path(self):
        with open("./saved_path.pickle", "rb") as f:
            my_load = pickle.load(f)

            if "me" in my_load:
                df1 = pd.DataFrame({"me", my_load["me"]})
                df1.style.format(precision=3, thousands=".", decimal=",").format_index(
                    str.upper, axis=1
                )

            if "ip" in my_load:
                my_load_t = pd.DataFrame.from_dict(my_load["ip"]).T
                df2 = pd.DataFrame.from_dict(my_load_t, columns=["users", "ips"])
                df2.style.format(precision=3, thousands=".", decimal=",").format_index(
                    str.upper, axis=1
                )
            if "path" in my_load:
                df3 = pd.DataFrame.from_dict([my_load["path"]], columns=["Path"])
                df3.style.format(precision=3, thousands=".", decimal=",").format_index(
                    str.upper, axis=1
                )

    def connect(self, user):
        with open("./saved_path.pickle", "rb") as f:
            my_load = pickle.load(f)
            try:
                if user in my_load["ip"]:
                    self.node.connect_to(host=my_load["ip"][user])
                    print("Connection succeeded")

                else:
                    print("User not found: either doesnt exist or check your syntax")
                print("\n")
            except Exception as e:
                print(f"Something went wrong: {e}")

    def send_message(self, user, msg):
        try:
            with open("./saved_path.pickle", "rb") as f:
                my_load = pickle.load(f)
                them_ips = my_load["ip"]

                if user in them_ips:

                    for a in self.node.nodes_connected:
                        if them_ips[user] == a.ip:
                            msg_from = f"{self.me}> {msg}"
                            self.node.send_message(msg_from, a.id)
                else:
                    print("User not found: either doesnt exist or check your syntax")

                print("message has been sent")
                print("-------------")
                print("\n")

        except Exception as e:
            print(e)

    def start(self):
        try:
            self.node.start()
            print("\n")
        except Exception as e:
            print(e)

    def stop(self):
        try:
            self.node.stop()
        except Exception as e:
            print(e)
