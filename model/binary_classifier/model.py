import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import cv2
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import load_img
from tensorflow.keras.models import load_model


TARGET_SIZE = 300

img = image.load_img('backend/model/01.jpeg', target_size=(TARGET_SIZE,TARGET_SIZE))

print(img)

x = np.asarray(img)



