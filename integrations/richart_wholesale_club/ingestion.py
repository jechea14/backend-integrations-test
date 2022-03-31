import numpy as np
import pandas as pd


def process_csv_files():
    # Read csv files into separate dataframes
    prices_stock_df = pd.read_csv("PRICES-STOCK.csv", sep='|'  , engine='python')
    products_df = pd.read_csv("PRODUCTS.csv", sep='|'  , engine='python')
    
    # Select only MM and RHSM branches that have stock
    filt = ((prices_stock_df['BRANCH'] == 'MM') | (prices_stock_df['BRANCH'] == 'RHSM')) & (prices_stock_df['STOCK'] > 0)
    filt_prices_stock = prices_stock_df.loc[filt]
    
    # Clean text
    new_products = products_df['ITEM_DESCRIPTION'].str.replace("[<p>/]","", regex=True)
    products_df['ITEM_DESCRIPTION'] = new_products
    
    # Combine category, sub-category, and sub-sub-category into one category 
    # separated by a pipe symbol in lower case
    products_df['Category'] = products_df['CATEGORY'] + ' | ' + products_df['SUB_CATEGORY'] + ' | ' + products_df['SUB_SUB_CATEGORY']
    products_df['Category'] = products_df['Category'].str.lower()


if __name__ == "__main__":
    process_csv_files()
