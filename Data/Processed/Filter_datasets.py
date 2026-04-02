import pandas as pd
import numpy as np
from pathlib import Path

data_file = Path(__file__).resolve().parents[1] / 'raw' / 'nepse.csv'
df = pd.read_csv(
	data_file,
	header=None,
	names=['Serial_no', 'Contract_no', 'Stock_symbol', 'Buyer', 'Seller', 'Quantity', 'Rate', 'Amount']
)
print(df.head())