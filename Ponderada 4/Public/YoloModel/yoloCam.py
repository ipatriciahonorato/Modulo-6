#Import the libraries
from ultralytics import YOLO #import the YOLO model
import cv2 #import opencv
import sqlite3

model = YOLO("C:/Users/Inteli/OneDrive/Documents/GitHub/Modulo-6/ponderada 4/codigo/YoloModel/best.pt") #load the model
model.predict(source="0", show = True, conf=0.5) #predict only images with a confidence of 50% and show the image

