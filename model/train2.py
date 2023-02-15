import pandas as pd
from sklearn.ensemble import IsolationForest
from joblib import dump
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
register_matplotlib_converters()
import numpy as np
rng = np.random.RandomState(42)

#Lecture
df = pd.read_csv('data/southE.csv', parse_dates = ['Datetime'], index_col= 'Datetime', usecols=['Datetime', 'precip_totl_tp', 'prsn_atmos_max_tp_prcedt', 'prsn_atmos_min_prmier_tmp', 'rad_gobal', 'tmp_air', 'tmp_pt_rose', 'humid_rlative_air','vent_vitess_tmp'])
#Traitement des données manquantes

df[ 'precip_totl_tp'].fillna(method = 'ffill', inplace = True)
df[ 'prsn_atmos_max_tp_prcedt'].fillna(method = 'ffill', inplace = True)
df[ 'prsn_atmos_min_prmier_tmp'].fillna(method = 'ffill', inplace = True)
df[ 'rad_gobal'].fillna(method = 'ffill', inplace = True)
df[ 'tmp_air'].fillna(method = 'ffill', inplace = True)
df[ 'tmp_pt_rose'].fillna(method = 'ffill', inplace = True)
df[ 'humid_rlative_air'].fillna(method = 'ffill', inplace = True)
df[ 'vent_vitess_tmp'].fillna(method = 'ffill', inplace = True)
df['rad_gobal'].fillna(method = 'bfill', inplace = True)

#verification de la non stationnaire
from statsmodels.tsa.stattools import adfuller
adfulter_result1 = adfuller(df['tmp_air'].diff()[1:])
print('reagbd')
 
print(f'Statistiques ADF :{adfulter_result1[0]}')
print(f'p-value : {adfulter_result1[1]}')
print('Valeurs Critiques :')
for key, value in adfulter_result1[4].items():
    print('\t{}: {}'.format(key, value))

print('\n.......................\n')

adfulter_result2 = adfuller(df['tmp_pt_rose'].diff()[1:])
print('realconst')

print(f'Statistiques ADF :{adfulter_result2[0]}')
print(f'p-value : {adfulter_result2[1]}')
print('Valeurs Critiques :')
for key, value in adfulter_result2[4].items():
    print('\t{}: {}'.format(key, value))
    

print('\n.......................\n')

adfulter_result2 = adfuller(df['rad_gobal'].diff()[1:])
print('realconst')

print(f'Statistiques ADF :{adfulter_result2[0]}')
print(f'p-value : {adfulter_result2[1]}')
print('Valeurs Critiques :')
for key, value in adfulter_result2[4].items():
    print('\t{}: {}'.format(key, value))
print('\n.......................\n')
adfulter_result1 = adfuller(df['precip_totl_tp'].diff()[1:])
print('reagbd')
 
print(f'Statistiques ADF :{adfulter_result1[0]}')
print(f'p-value : {adfulter_result1[1]}')
print('Valeurs Critiques :')
for key, value in adfulter_result1[4].items():
    print('\t{}: {}'.format(key, value))

print('\n.......................\n')

adfulter_result2 = adfuller(df['prsn_atmos_max_tp_prcedt'].diff()[1:])
print('realconst')

print(f'Statistiques ADF :{adfulter_result2[0]}')
print(f'p-value : {adfulter_result2[1]}')
print('Valeurs Critiques :')
for key, value in adfulter_result2[4].items():
    print('\t{}: {}'.format(key, value))
    

print('\n.......................\n')

adfulter_result2 = adfuller(df['prsn_atmos_min_prmier_tmp'].diff()[1:])
print('realconst')

print(f'Statistiques ADF :{adfulter_result2[0]}')
print(f'p-value : {adfulter_result2[1]}')
print('Valeurs Critiques :')
for key, value in adfulter_result2[4].items():
    print('\t{}: {}'.format(key, value))

adfulter_result2 = adfuller(df['humid_rlative_air'].diff()[1:])
print('realconst')

print(f'Statistiques ADF :{adfulter_result2[0]}')
print(f'p-value : {adfulter_result2[1]}')
print('Valeurs Critiques :')
for key, value in adfulter_result2[4].items():
    print('\t{}: {}'.format(key, value))
    

print('\n.......................\n')

adfulter_result2 = adfuller(df['vent_vitess_tmp'].diff()[1:])
print('realconst')

print(f'Statistiques ADF :{adfulter_result2[0]}')
print(f'p-value : {adfulter_result2[1]}')
print('Valeurs Critiques :')
for key, value in adfulter_result2[4].items():
    print('\t{}: {}'.format(key, value))

print(df.shape) 
train = df.iloc[0:800]
test = df.iloc[800:]
print(train.shape, test.shape)
##Model fit
clf = IsolationForest(n_estimators=50, max_samples=500, random_state=rng, contamination=0.01)
clf.fit(train)

dump(clf, './isolation_forest2.joblib')
