import numpy as np
import pandas as pd

def warn(*args,**kwargs):
    pass

import warnings

warnings.warn = warn
warnings.filterwarnings('ignore')
URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
# Reading the Html File
tables = pd.read_html(URL)
# Selecting the 3rd Table
df = tables[3]

#Replacing coulumn headers with numbers
df.columns = range(df.shape[1])
# Selecting the first 3 columns
df = df[[0,2]]
# Getting the top ten Countries
df =df.iloc[1:11,:]
# Renaming the Column names
df.columns = ["Country","GDP (Million USD)"]

# Changing the data type

df["GDP (Million USD)"] = df["GDP (Million USD)"].astype(int)

# Coversion to billions

df["GDP (Million USD)"] = df["GDP (Million USD)"]/1000

# Rounding off to 2 decimal places

df["GDP (Million USD)"] = np.round(df[["GDP (Million USD)"]],2)

# Renaming The column names

df.columns = ["Country","GDP (Billion USD)"]

df.to_csv("Largest_economies.csv")
