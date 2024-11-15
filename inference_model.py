import pandas as pd
from models.naive_model import NaiveModel

model = NaiveModel()
model.load('medias.pkl')

datos = pd.read_csv('mnist_784.csv')
nuevos_datos = model.predict(datos)
print(nuevos_datos.head())
nuevos_datos.to_csv('nuevos_datos.csv')