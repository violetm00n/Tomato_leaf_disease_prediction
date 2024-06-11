import tensorflow as tf
import numpy as np
from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.applications.inception_v3 import InceptionV3
import pathlib
from tensorflow.keras.models import Model
from tensorflow.keras.utils import load_img
from glob import glob
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from google.colab import drive
drive.mount('/content/drive')
I=InceptionV3(input_shape=[224,224,3],weights='imagenet',include_top=False)
for layer in I.layers:
  layer.trainable=False
=glob("/content/drive/MyDrive/Crop desease/Tomato/Train/*")
l=len(L)L
L
x=Flatten()(I.output)
predict=Dense(l,activation='softmax')(x)
