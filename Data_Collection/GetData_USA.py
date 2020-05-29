import numpy as np
import pandas as pd
from datetime import date
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.worldometers.info/coronavirus/country/us/')
soup = BeautifulSoup(req.content)
data = list(map(lambda x: list(map(lambda y: y.text, x.select('td, th'))), soup.select('table#usa_table_countries_today tr')))
# Turn array of arrays into a Pandas Dataframe
df = pd.DataFrame(data)

# Set the column names to the first row
df.columns = df.iloc[0]

# Delete first row to avoid confusing it as a country
df = df.drop(0, axis=0)

# Add date column to distinguish daily data
idx=0
df.insert(loc=idx, column='Date', value=date.today())

file_name = 'USAData/'+ str(date.today()) + '.csv'
df.to_csv(file_name, sep=',', index=False)