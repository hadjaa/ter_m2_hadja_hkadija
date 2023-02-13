import pandas as pd
from joblib import dump
from statsmodels.tsa.arima.model import ARIMA
#import seaborn as sns
import matplotlib.pyplot as plt 
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
register_matplotlib_converters()
import numpy as np

#Lecture
df = pd.read_csv('data/southE.csv', parse_dates = ['Datetime'], usecols=['Datetime', 'tmp_air'])
#Traitement des données manquantes


df[ 'tmp_air'].fillna(method = 'ffill', inplace = True)

#verification de la non stationnaire
from statsmodels.tsa.stattools import adfuller
adfulter_result1 = adfuller(df['tmp_air'].diff()[1:])
print(f'Statistiques ADF :{adfulter_result1[0]}')
print(f'p-value : {adfulter_result1[1]}')
print('Valeurs Critiques :')
for key, value in adfulter_result1[4].items():
    print('\t{}: {}'.format(key, value))

#print(df.shape) 
train = df.iloc[0:800]
test = df.iloc[800:]
#print(train.shape, test.shape)
## Fit model


model_arim = ARIMA(train, order = (2,0,3))

#model_fit = model_arim.fit()

#dump(model_fit, './arimaa.joblib')


