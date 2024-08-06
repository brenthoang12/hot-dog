from flask import Flask, request, jsonify, render_template

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

from PIL import Image
import numpy as np
import io


app = Flask(__name__)

model = load_model('/Users/brenthoang/Documents/Test_Project/hot-dog/model/model.h5')

def get_prediction(model, process_image):
    yhat = model.predict(process_image)
    result = 'hot dog' if yhat[0] > .5 else 'not hot dog'
    return result


def preprocess_image(user_input):
    image = user_input.resize((128,128))
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    return image



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def predict():
    # get user input
    file = request.files['get-image']

    # check user input
    if file.filename == '':
        return render_template('index.html', prediction='no file selected')
    
    else:
        image = Image.open(file)
        process_image = preprocess_image(image)
        classification = get_prediction(model, process_image)
        return render_template('index.html', prediction = classification)

if __name__ == '__main__':
    app.run(debug=True)