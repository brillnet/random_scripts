import pandas as pd
import numpy as np
import string
import warnings

c_edit = {"Republic of Korea": "South Korea", "United States of America": "United States", 
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom", 
"China, Hong Kong Special Administrative Region": "Hong Kong"}

column_names = ['Country','Petajoules','Gigajoules','%']

#  Opening 
df = pd.read_excel('assets/Energy Indicators.xls', 
                    skiprows=range(0,17),skipfooter=37)

#  Dropping first two columns
df = df.drop(df.columns[[0, 1]], axis=1)

#  Changing column names
df = df.rename(columns={'Unnamed: 2': 'Country', 
'Petajoules': 'Energy Supply', 
'Gigajoules': 'Energy Supply per Capita', 
'%': '% Renewable'})

#  Changing rows with ... with NaN
df = df.replace('...',np.nan)

#  Changing country names
df['Country'] = df['Country'].apply(lambda c: c_edit[c] if c in c_edit else c)

# print(df.head(100))

# warnings.filterwarnings('ignore')