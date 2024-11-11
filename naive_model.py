import pandas as pd

class NaiveModel:
    def __init__(self, param1, param2, param3, diccionario):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.diccionario = diccionario

# Metodo fit que recibira unos datos de entrada en formato "Data Frame" de Pandas
# y guarada dentro de la clase (en el self) un diccionario con la media de cada columna.
# convertir a dataframe, despues a diccionario y el valor numerico/media de cada clave/columna.


    def fit(self, diccionario):
        #diccionario=pd.read_csv()
        pass

# diccionario guardado en el que cada dato haya sido dividido por la media correspondiente a su columna.
# Se debe hacer con cuidado para no modificar los datos originales por lo que se recomienda hacer una
# copia profunda de los datos de entrada en una variable local del metodo, devolver dataframe. Dividir cada columna
# por la media que corresponda, cada valor dividido por la media de la columna que corresponda.

    def predict(self):
        pass

# Guarda las medias calculadas de fit con pickle a disco, se pasa la ruta donde se han guadado en disco
# las medias y carga en la clase las medias calculadas.
    def save(self):
        pass

# Ruta donde estan guardadas en el disco de las medias y carga las medias calculadas. Carga en disco las medias a la
# propia clase.
    def load(self):
        pass

"""Este Script tiene que estar dentro de un paquete llamado models. Fuera de este paquete debe de haber 2 archivos
mas afuera. For models.nave_model, import NaiveModel.

Fuera del paquete, train_model.py e inference_model.py"""