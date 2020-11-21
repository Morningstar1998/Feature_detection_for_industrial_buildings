# -*- coding: utf-8 -*-
"""InferenciasYOLO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17TmfF_ruXDJB19JnhUxIoMbhdax5vltP
"""

# Commented out IPython magic to ensure Python compatibility.
def imShow(path):
  import cv2
  import matplotlib.pyplot as plt
#   %matplotlib inline

  image = cv2.imread(path)
  height, width = image.shape[:2]
  resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

  fig = plt.gcf()
  fig.set_size_inches(18, 10)
  plt.axis("off")
  plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
  plt.show()

#!python generate_train.py
!python generate_test.py
'''
Dentro de la carpeta de 'darknet/data/' deberían de existir los archivos de 'train.txt' y 'test.txt'
'''

# Commented out IPython magic to ensure Python compatibility.
# cambiar la configuración a modo de pruebas
# %cd cfg
!sed -i 's/batch=64/batch=1/' yolov4-obj.cfg
!sed -i 's/subdivisions=16/subdivisions=1/' yolov4-obj.cfg
# %cd ..

# Para correr inferencias sobre solo 1 imagen
# La prier ruta debe ser adaptada a donde se encuentre el archivo .weights que se desee usar
# La segunda ruta debe ser de la imagen a procesar
# -thresh define el mínimo porcentaje de confianza que deben tener las inferencias

!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/yolov4/backup/yolov4-obj_last.weights /content/2020-06-24_11-50-01.JPG -thresh 0.5
imShow('predictions.jpg')

#Para correr múltiples inferencias en imágenes que están dentro de una misma carpeta

import os

#!cp -r /mydrive/yolov4/test/ ../


ims = os.listdir("../test") #insertar la ruta donde se encuentra la carpeta de las imagenes a las que se desea procesar

for i in ims:
  im = os.path.join("/content/test/", i) #Cambiar ruta a la ruta de la carpeta de imágenes

  # Primera ruta debe ser referencia a donde se encuetra el archivo .weights que correrá las inferencias

  !./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/yolov4/backup/yolov4-obj_last.weights $im -thresh 0.5
  imShow('predictions.jpg')