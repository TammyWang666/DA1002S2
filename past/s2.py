import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
df = pd.read_csv("pisa.csv")
df.head()

# extract all columns except for 'MEASURE' and 'FREQUENCY'
df = df.iloc[:, [0, 1, 2, 5, 6]]
# get rid of rows with 'TOT' subject
df = df[df['SUBJECT'] != "TOT"]

# get list of variable categories of indicator and location
indicators = list(df["INDICATOR"].unique())
locations = list(df['"LOCATION"'].unique())

print(df.head())