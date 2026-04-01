import pandas as pd
import numpy as np
from pathlib import Path

data_file = Path(__file__).resolve().parents[1] / 'raw' / 'nepse.csv'
df = pd.read_csv(data_file)
print(df.head())