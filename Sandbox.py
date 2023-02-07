# %%
import pandas as pd
pew = pd.read_csv('data/pew.csv')
pew.head()
# %%
pew_long = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')
pew_long.head()
# %%
billboard = pd.read_csv('data/billboard.csv')
billboard.head(16)
# %%
ebola = pd.read_csv('data/country_timeseries.csv')
ebola_long = ebola.melt(id_vars=['Date', 'Day'])

# The code below adds two new columns to the DataFrame, status and country, by splitting the variable column on the underscore character.
    # variable_split = ebola_long.variable.str.split('_')
    # status_values = variable_split.str.get(0)
    # country_values = variable_split.str.get(1)
    # ebola_long['status']= status_values
    # ebola_long['country']= country_values

# The code below does the same thing as the code above, but in a more concise way.
variable_split = ebola_long.variable.str.split('_', expand=True)
ebola_long[['status', 'country']] = variable_split
# %%

import pandas as pd
from datetime import datetime
import yfinance as yf

# import openpyxl

def get_quotes(etf_ticker, min_date, max_date):
    quotes = yf.download(etf_ticker, start=min_date, end=max_date)

    # Create a dataframe with the date, quote and the etf ticker
    df_etf = quotes[['Adj Close']].rename(columns={'Adj Close':'ETF_quote'})
    df_etf['ETF_Yahoo_Ticker'] = etf_ticker
    df_etf.reset_index(inplace= True)
    df_etf['Date'] = df_etf['Date'].apply(lambda x: x.date())

    return df_etf
# %%
quotes = yf.download(['SPY','AAPL','MSFT'], start='2021-01-01', end='2022-01-01')
# %%
quotes_long = pd.melt(quotes, id_vars=['Date'], var_name='quote_type')

# %%
print(type(square(x)))
# %%
import numpy as np

def avg_2_mod(x, y):
   """Calculate the average, unless x is 20
   If the value is 20, return a missing value
   """
   if (x == 20):
     return(np.NaN)
   else:
     return (x + y) / 2

df = pd.DataFrame({"a": [10, 20, 30], "b": [20, 30, 40]})
print(avg_2_mod(df['a'], df['b']))

# %%
