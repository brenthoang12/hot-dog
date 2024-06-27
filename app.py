import numpy as np
from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import io

#Create an app object using the Flask class. 
app = Flask(__name__)

#Load model
model = load_model('model/model.h5')

#Process image for model
def preprocess_image(image):
    image = image.resize((300, 300)) 
    image = np.array(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = image / 255.0  # Normalize the image
    return image

#Connecting to website
@app.route('/')
def home():
    return render_template('index.html')


#Getting image
@app.route('/predict', methods=['POST'])
