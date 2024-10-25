# Description: This file contains the utility functions that are used in the main file.
import pandas as pd

def get_data(PATH):
    df = pd.read_csv(PATH)
    df.rename(columns={"item_price": "order_price"}, inplace=True)
    df.drop(columns=["order_id"], inplace=True)
    df["order_price"] = df["order_price"].replace("[\$,]", "", regex=True).astype(float)
    bestsellers = df.groupby("item_name")[["order_price"]].sum()
    # reset the index to make the item_name a column again
    bestsellers.reset_index(inplace=True)
    bestsellers.sort_values(by="order_price", ascending=False, inplace=True)
    top_five = bestsellers.iloc[:5]
    # return the variables to be used in the main file
    return top_five

