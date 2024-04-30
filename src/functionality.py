import click
import pickle
import threading
import pandas as pd
import os
from tabulate import tabulate


# general purpose decorator
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before calling the function")
#         result = func(*args, **kwargs)
#         print("After calling the function")
#         return result
#     return wrapper
# Sets your name


def dec_openf(func):
    def wrapper(*args, **kwargs):
        try:
            with open("./saved_path.pickle", "rb") as f:
                data = pickle.load(f)
                result = func(*args, data=data, **kwargs)
                return result

        except FileNotFoundError:
            print("No such file")
        except pickle.UnpicklingError:
            print("Unable unpickle")
        except Exception as e:
            print(f"An error occurred: {e}")

    return wrapper


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

    # set the main configs for the program to use
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

    # Display the content of the data file
    @dec_openf
    def load_path(self, data):
        if "me" in data:
            df1 = pd.DataFrame({"me", data["me"]})

            print(tabulate(df1, headers=df1.columns[1:], tablefmt="grid"))

        if "ip" in data:

            tup_ips = [(key, value) for key, value in data["ip"].items()]
            df2 = pd.DataFrame(tup_ips, columns=["users", "ips"])

            print(tabulate(df2, headers=df2.columns, tablefmt="grid"))

        if "path" in data:
            df3 = pd.DataFrame({"Path": [data["path"]]})
            print(tabulate(df3, headers=df3.columns, tablefmt="grid"))

    # Perform connection to the certain user/peer
    @dec_openf
    def connect(self, user, data):
        if user in data["ip"]:
            self.node.connect_to(host=data["ip"][user])
            print("Connection succeeded")

        else:
            print("User not found: either doesnt exist or check your syntax")
        print("\n")

    # Sends content to the other peer
    def send(self, user, type=""):
        if len(self.node.nodes_connected) == 0:
            print("Youre not connected. Connect first")
            return

        @dec_openf
        def open_file(data):
            them_ips = data["ip"]
            if user in them_ips:
                for a in self.node.nodes_connected:

                    if them_ips[user] == a.host:
                        data = {"me": data["me"], "type": type}
                        if type == "msg":

                            msg = input("Please input your message: ")
                            data["msg"] = msg
                            self.node.send_message(data, a.id)
                            print("message has been sent")
                            print("-------------")
                            print("\n")
                            break
                        elif type == "file":
                            filehash = self.share_file(data)
                            data["filehash"] = filehash
                            self.node.send_message(data, a.id)
                            print("file has been sent")
                            print("-------------")
                            break
                        else:
                            print(
                                "One of the commands do not exist: input help for guidance"
                            )
                            break

            else:
                print("User not found: either doesnt exist or check your syntax")

        open_file()

    @dec_openf
    def set_path(self, data):
        self.node.setfiledir(f"{data['path']}")
        print("the directory was set!")

    def share_file(self, f):
        try:
            return self.node.addfile(f"C:/Users/sulta/OneDrive/Desktop/sss.png")

        except FileNotFoundError:
            print("No such file")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

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
