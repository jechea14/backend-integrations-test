import numpy as np
import pandas as pd
import re
import unittest
from ingestion import *

class IngestionTest(unittest.TestCase):
    def test_process_csv_files(self):
        test_csv1 = "csv_1.csv"
        test_csv2 = "csv_2.csv"
        
        expected = pd.DataFrame({
            'SKU': [142308, 223240, 49514],
            'BUY_UNIT': ['NaN', 'UN', 'KG'],
            'DESCRIPTION_STATUS': ['A','B', 'CD'],
            'BRANCH': ['HRO', 'RHSM', 'RHSM'],
            'PRICE': [45.6, 15.3, 56.7],
            'STOCK': [3, 5, -2]
        })
        
        actual = process_csv_files(test_csv1, test_csv2)
        
        np.array_equal(expected, actual)    
    
    def test_data_cleaning(self):
        df = pd.DataFrame({
            'EAN': [7501035912854, 8410030007788, 33383653006, 40000658928, 780292000652],
            'BRANCH': ['MM', 'HRO', 'RHSM', 'MM', 'RHSM'],
            'PRICE': [15.3, 64.2, 79.5, 23.7, 47.1],
            'STOCK': [2, 4, 1, -2, 5],
            'BRAND_NAME': ['Studio Line', 'Microlab', 'Karcher', 'Altec Lansing', 'H2O'],
            'CATEGORY': ['Deli Meat & Cheese,',
                            'Hardlines',
                            'Bakery',
                            'Hardlines',
                            'Home'],
            'SUB_CATEGORY': ['Service Deli', 'Disposable And Birthday Party Supp', 'Bakery', 'Stationary & Party Goods', 'Domestic Goods'],
            'SUB_SUB_CATEGORY': ['Com Prepar', 'Supplies', 'Cake', 'Cuadernos', 'Toallas Baño'],
            'ITEM_DESCRIPTION': ['<p>Cepillo Dental Infantil Tarzan 0 PZA</p>',
                                '<p>Vino Tinto Maruqes De Penamonte 750 ML.</p>',
                                '<p>Corazon De Apio 1 PZA</p>',
                                '<p>Calcetin Dep Bgn3739 1UN</p>',
                                '<p>Q Crema Unt Nat 100 100GR</p>'],
            'ITEM_IMG': ['img1', 'img2', 'img3', 'img4', 'img5'],
            'ITEM_NAME': ['item1', 'item2', 'item3', 'item4', 'item5'],
            'SKU': [21234, 15446, 45754, 865476, 867905]
        })
        
        expected = pd.DataFrame({
            'EAN': [7501035912854, 8410030007788, 33383653006, 40000658928, 780292000652],
            'BRANCH': ['MM', 'HRO', 'RHSM', 'MM', 'RHSM'],
            'PRICE': [15.3, 64.2, 79.5, 23.7, 47.1],
            'STOCK': [2, 4, 1, -2, 5],
            'BRAND_NAME': ['Studio Line', 'Microlab', 'Karcher', 'Altec Lansing', 'H2O'],
            'Category': ['Deli Meat & Cheese | Service Deli | Com Prepar',
                         'Hardlines | Disposable And Birthday Party Supp | Supplies',
                         'Bakery | Bakery | Cakes - In Store | Cake',
                         'Hardlines | Stationary & Party Goods | Cuadernos',
                         'Home | Domestic Goods | Toallas Baño'],
            'ITEM_DESCRIPTION': ['Cepillo Dental Infantil Tarzan 0 Pza',
                                'Vino Tinto Maruqes De Penamonte 750 Ml.',
                                'Corazon De Apio 1 Pza',
                                'Calcetin Dep Bgn3739 1Un',
                                'Q Crema Unt Nat 100 100Gr'],
            'ITEM_IMG': ['img1', 'img2', 'img3', 'img4', 'img5'],
            'ITEM_NAME': ['item1', 'item2', 'item3', 'item4', 'item5'],
            'Package': ['0 PZA', '750 ML.', '1 PZA', '1UN', '100GR'],
            'SKU': [21234, 15446, 45754, 865476, 867905]
        })
        
        actual = data_cleaning(df)
        
        np.array_equal(expected, actual)
    
    
    def test_select_branch(self):
        df = pd.DataFrame({
            'EAN': [7501035912854, 8410030007788, 33383653006, 40000658928, 780292000652],
            'BRANCH': ['MM', 'HRO', 'RHSM', 'MM', 'RHSM'],
            'PRICE': [15.3, 64.2, 79.5, 23.7, 47.1],
            'STOCK': [2, 4, 1, -2, 5],
            'BRAND_NAME': ['Studio Line', 'Microlab', 'Karcher', 'Altec Lansing', 'H2O'],
            'Category': ['Deli Meat & Cheese | Service Deli | Com Prepar',
                         'Hardlines | Disposable And Birthday Party Supp',
                         'Bakery | Bakery | Cakes - In Store',
                         'Hardlines | Stationary & Party Goods | Cuadernos',
                         'Home | Domestic Goods | Toallas Baño'],
            'ITEM_DESCRIPTION': ['Cepillo Dental Infantil Tarzan 0 Pza',
                                'Vino Tinto Maruqes De Penamonte 750 Ml.',
                                'Corazon De Apio 1 Pza',
                                'Calcetin Dep Bgn3739 1Un',
                                'Q Crema Unt Nat 100 100Gr'],
            'ITEM_IMG': ['img1', 'img2', 'img3', 'img4', 'img5'],
            'ITEM_NAME': ['item1', 'item2', 'item3', 'item4', 'item5'],
            'Package': ['0 PZA', '750 ML.', '1 PZA', '1UN', '100GR'],
            'SKU': [21234, 15446, 45754, 865476, 867905]
        })
        
        expected = pd.DataFrame({
            'EAN': [7501035912854, 33383653006, 780292000652],
            'BRANCH': ['MM', 'RHSM', 'RHSM'],
            'PRICE': [15.3, 79.5, 47.1],
            'STOCK': [2, 1, 5],
            'BRAND_NAME': ['Studio Line', 'Karcher', 'H2O'],
            'Category': ['Deli Meat & Cheese | Service Deli | Com Prepar',
                         'Bakery | Bakery | Cakes - In Store',
                         'Home | Domestic Goods | Toallas Baño'],
            'ITEM_DESCRIPTION': ['Cepillo Dental Infantil Tarzan 0 Pza',
                                'Corazon De Apio 1 Pza',
                                'Q Crema Unt Nat 100 100Gr'],
            'ITEM_IMG': ['img1', 'img3', 'img5'],
            'ITEM_NAME': ['item1', 'item3', 'item5'],
            'Package': ['0 PZA', '1 PZA', '100GR'],
            'SKU': [21234, 45754, 867905]            
        })
        
        actual = select_branch(df, 'MM', 'RHSM')
        
        np.array_equal(expected, actual)
        
if __name__ == '__main__':
    unittest.main()
