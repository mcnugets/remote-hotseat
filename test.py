import pandas as pd
import pickle
from tabulate import tabulate

with open("./saved_path.pickle", "rb") as f:
    my_load = pickle.load(f)

    if "me" in my_load:
        df1 = pd.DataFrame({"me", my_load["me"]})

        print(tabulate(df1, headers=df1.columns[1:], tablefmt="grid"))

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