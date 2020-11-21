# -*- coding: utf-8 -*-
"""ConfigYOLO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10ygx9ZH9kHUkN3MTuaqsxRsjL0Kp3LsM
"""

# clonar repositorio de darknet
!git clone https://github.com/AlexeyAB/darknet

# Commented out IPython magic to ensure Python compatibility.
# modificar el makefile para garantizar que opencv y el gpu estén activos
# %cd darknet
!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile
!sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

# verificar versión de cuda
!/usr/local/cuda/bin/nvcc --version

# construcción de darknet
!make

# pesos para primeros entrenamientos 
!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights

# Commented out IPython magic to ensure Python compatibility.
# función auxiliar de impresión de imagen
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

'''
Para entrenar un modelo:
  La carpeta con imágenes de entrenamiento deberán de estar dentro de 'darknet/data/'
  El archivo que genera el txt para entrenar el modelo 'generate_train.py' debe estar dentro del directorio 'darknet/'
Funcionamiento general:
  El archivo con la configuración 'yolov4-obj.cfg' debe de estar dentro de 'darknet/cfg'
  Los archivos con la información de las clases 'obj.data' y 'obj.names' deben de estar dentro de 'darknet/data/'
  El archivo que genera el txt para probar y hacer inferencias el modelo 'generate_test.py' debe estar dentro del directorio 'darknet/'
'''