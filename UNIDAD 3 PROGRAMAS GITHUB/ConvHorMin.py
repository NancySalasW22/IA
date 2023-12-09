##NANCY JANETH PÉREZ SALAS##
##NANCY JANETH PÉREZ SALAS##

#CONVERSION HORAS A MINUTOS
import tensorflow as tf
import numpy as np

horas = np.array([24,14,4], dtype=float)
minutos = np.array ([1440, 840, 240], dtype=float)

#capa = tf.keras.layers.Dense(units=1, input_shape=[1])
#modelo = tf.keras.layers.Sequential([capa])
oculta1=tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2=tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1,oculta2,salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("comenzando entrenamiento...")
historial=modelo.fit(horas,minutos, epochs=1000, verbose=False)
print("modelo entrenado!!!")

import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de perdida")
plt.plot(historial.history["loss"])
