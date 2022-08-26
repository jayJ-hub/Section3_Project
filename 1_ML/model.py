import sqlite3
import pandas as pd

PATH = '1_ML'

#connection with sqlite
conn = sqlite3.connect("0_database/spotify.db")

#read db data
dt = pd.read_sql_query("SELECT * FROM analytics", conn)
df = dt.set_index("id")

#define feature, target
y = 'popularity'
X = df.columns.tolist()
X.remove(y)

#linear regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(df[X], df[y])

#Pickle : export model
import pickle
with open(f'{PATH}/model.pkl', 'wb') as pickle_file:
	pickle.dump(model, pickle_file)
