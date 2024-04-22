import pandas as pd
import pickle
from tabulate import tabulate
import click
from src.p2p import local_node
from src.functionality import cli

n = local_node()
c = cli(n)
c.start()

n.setfiledir("D:/vscode_projects/python based projects")
filehash = n.addfile("C:/Users/sulta/OneDrive/Desktop/sss.png")
try:
    n.requestFile(filehash)
    print(filehash)
except Exception as e:
    print(e)

n.stop()

# with open("./saved_path.pickle", "rb") as f:
#     my_load = pickle.load(f)

#     if "me" in my_load:
#         df1 = pd.DataFrame({"me", my_load["me"]})

#         print(tabulate(df1, headers=df1.columns[1:], tablefmt="grid"))

#     if "ip" in my_load:
#         my_load_t = pd.DataFrame.from_dict(my_load["ip"]).T
#         df2 = pd.DataFrame.from_dict(my_load_t, columns=["users", "ips"])
#         df2.style.format(precision=3, thousands=".", decimal=",").format_index(
#             str.upper, axis=1
#         )
#     if "path" in my_load:
#         df3 = pd.DataFrame.from_dict([my_load["path"]], columns=["Path"])
#         df3.style.format(precision=3, thousands=".", decimal=",").format_index(
#             str.upper, axis=1
#         )
