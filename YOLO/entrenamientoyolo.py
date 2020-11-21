# -*- coding: utf-8 -*-
"""EntrenamientoYOLO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yufsf1cXzLUYbc351GuU80gLhWbEk8GG
"""

# Comenzar entrenamiento
!./darknet detector train data/obj.data cfg/yolov4-obj.cfg yolov4.conv.137 -dont_show

# descomentar para que imprima el resultado del entrenamiento
# imShow('chart.png')

# Para reanudar un entrenamiento a partir de un peso en específico, actualizar ruta a donde se encuentre el .weights
# !./darknet detector train data/obj.data cfg/yolov4-obj.cfg /mydrive/yolov4/backup/yolov4-obj_last.weights -dont_show

# Obtener métricas de desempeño por cada clase entrenada
#!./darknet detector map data/obj.data cfg/yolov4-obj.cfg /mydrive/yolov4/backup/yolov4-obj_last.weights