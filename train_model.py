import pandas as pd
from models.naive_model import NaiveModel

data = pd.read_csv('mnist_784.csv')

model = NaiveModel()
model.fit(data)
model.save('medias.pkl')