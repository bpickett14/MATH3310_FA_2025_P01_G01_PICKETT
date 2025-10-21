import statsmodels.api as sm
import pandas as pd

#load crime data from data folder
df = pd.read_csv('../data/raw/crime.csv')

df.head()