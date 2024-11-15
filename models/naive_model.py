import pandas as pd
import pickle

class NaiveModel:
    def __init__(self):
        self.medias = None


# Metodo fit que recibira unos datos de entrada en formato "Data Frame" de Pandas
# y guarada dentro de la clase (en el self) un diccionario con la media de cada columna.
# convertir a dataframe, despues a diccionario y el valor numerico/media de cada clave/columna.


    def fit(self, dataframe):
        med = [dataframe[m].mean() for m in dataframe.columns]
        columnas = list(dataframe.columns)

        self.medias = {columnas[i]: med[i] for i in range(len(columnas))}

# diccionario guardado en el que cada dato haya sido dividido por la media correspondiente a su columna.
# Se debe hacer con cuidado para no modificar los datos originales por lo que se recomienda hacer una
# copia profunda de los datos de entrada en una variable local del metodo, devolver dataframe. Dividir cada columna
# por la media que corresponda, cada valor dividido por la media de la columna que corresponda.

    def predict(self,dataframe):
        newdf = dataframe.copy()
        med = [dataframe[m].mean() for m in dataframe.columns]
        columnas = list(dataframe.columns)
        for i in range(len(columnas)):
            newdf[columnas[i]] = newdf[columnas[i]] / med[i]
        return newdf

# Guarda las medias calculadas de fit con pickle a disco, se pasa la ruta donde se han guadado en disco
# las medias y carga en la clase las medias calculadas.
    def save(self, ruta):
        with open(ruta, 'wb') as f:
            pickle.dump(self.medias, f, protocol=pickle.HIGHEST_PROTOCOL) #Highest protocol para guardar objetos grandes y no perder tiempo y espacio de disco
# Ruta donde estan guardadas en el disco de las medias y carga las medias calculadas. Carga en disco las medias a la
# propia clase.

    def load(self, ruta):
        with open(ruta, 'rb') as f:
            pickle.load(f)
"""Este Script tiene que estar dentro de un paquete llamado models. Fuera de este paquete debe de haber 2 archivos
mas afuera. For models.nave_model, import NaiveModel.

Fuera del paquete, train_model.py e inference_model.py"""