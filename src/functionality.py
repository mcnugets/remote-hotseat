import click
import pickle
import threading
import pandas as pd
import os
from tabulate import tabulate


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
            if "me" not in dict:
                with open(filename, "ab") as f:
                    me = input("Set your name please: ")
                    dict["me"] = me
                    pickle.dump(dict, f)

        except Exception as e:
            print(f"Oops something went wrong: {e}")

    def set_configs(self):

        filename = "./saved_path.pickle"

        if os.path.exists(filename):
            try:
                with open(filename, "rb") as f:
                    dict = pickle.load(f)
            except EOFError:
                dict = {}
        else:
            dict = {}
        with open(filename, "wb") as f:
            save = input("Input your save file path:")
            print("--------")
            n_peers = int(input("how many peers: "))
            if "ip" in dict:
                peers = dict["ip"]
            else:
                peers = {}
            try:
                for _ in range(n_peers):
                    user = input("user: ")
                    ip = input("ip: ")
                    if user in peers:
                        print("user already exists, were gonna skip that one")
                    else:
                        peers[user] = ip
                dict["path"] = save
                dict["ip"] = peers
                pickle.dump(dict, f)
            except Exception as e:
                print(f"the cause: {e}")

    def load_path(self):
        with open("./saved_path.pickle", "rb") as f:
            my_load = pickle.load(f)

            if "me" in my_load:
                df1 = pd.DataFrame({"me", my_load["me"]})

                print(tabulate(df1, headers=df1.columns[1:], tablefmt="grid"))

            if "ip" in my_load:

                tup_ips = [(key, value) for key, value in my_load["ip"].items()]
                df2 = pd.DataFrame(tup_ips, columns=["users", "ips"])

                print(tabulate(df2, headers=df2.columns, tablefmt="grid"))

            if "path" in my_load:
                df3 = pd.DataFrame({"Path": [my_load["path"]]})
                print(tabulate(df3, headers=df3.columns, tablefmt="grid"))

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
