import numpy as np
import pandas as pd
import re

PRICES_STOCK_CSV = "PRICES-STOCK.csv"
PRODUCTS_CSV = "PRODUCTS.csv"

def process_csv_files(csv1, csv2):
    # Read csv files into separate dataframes
    prices_stock_df = pd.read_csv(csv1, sep='|'  , engine='python')
    products_df = pd.read_csv(csv2, sep='|'  , engine='python')
    
    # Join the prices/stock dataframe and products dataframe
    df_merge = pd.merge(products_df, prices_stock_df, how='right')
    return df_merge

def data_cleaning(dataframe):
    # Clean text
    new_products = dataframe['ITEM_DESCRIPTION'].str.replace("[<p>/]","", regex=True)
    dataframe['ITEM_DESCRIPTION'] = new_products

    # Combine category, sub-category, and sub-sub-category into one category 
    # separated by a pipe symbol in lower case
    dataframe['Category'] = dataframe['CATEGORY'] + ' | ' + dataframe['SUB_CATEGORY'] + ' | ' + dataframe['SUB_SUB_CATEGORY']
    
    # Extract package from item description
    pattern = re.compile(r'(\d+(?!.*\d).*)')
    s = dataframe['ITEM_DESCRIPTION'].str.extract(pattern, expand=True)
    dataframe['Package'] = s
    
    # Format data
    dataframe['Category'] = dataframe['Category'].str.title()
    dataframe['ITEM_NAME'] = dataframe['ITEM_NAME'].str.title()
    dataframe['ITEM_DESCRIPTION'] = dataframe['ITEM_DESCRIPTION'].str.title()
    dataframe['BRAND_NAME'] = dataframe['BRAND_NAME'].str.title()
    
    return dataframe

def select_branch(dataframe, branch1, branch2):
    # Select only MM and RHSM branches that have stock
    filt = ((dataframe['BRANCH'] == branch1) | (dataframe['BRANCH'] == branch2)) & (dataframe['STOCK'] > 0)
    filt_branch_stock = dataframe.loc[filt]
    
    # Create new dataframe with necessary columns for api
    final_df = filt_branch_stock[['EAN', 'BRANCH', 'PRICE', 'STOCK', 'BRAND_NAME', 'Category', 'ITEM_DESCRIPTION', 'ITEM_IMG', 'ITEM_NAME', 'Package', 'SKU']]
    
    return final_df

if __name__ == "__main__":
    merge_df = process_csv_files(PRICES_STOCK_CSV, PRODUCTS_CSV)
    clean_data = data_cleaning(merge_df)
    results = select_branch(clean_data, 'MM', 'RHSM')
    
    # Top 100 most expensive products from each branch
    top_mm_products = results.sort_values(['PRICE', 'BRANCH'], ascending=[0,1]).head(100)
    top_rhsm_products = results.sort_values(['PRICE', 'BRANCH'], ascending=[0,0]).head(100)
    # print(top_mm_products.head(10))
