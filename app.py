from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
import io


app = Flask(__name__)

def get_prediction(model, process_image):
    yhat = model.prediction(process_image)
    result = 'Hot Dog' if yhat[0] > .5 else 'Not Hot Dog'
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
    file = request.files['get-image']
    image = Image.open(file)
    process_image = preprocess_image(image)
    classification = get_prediction(process_image)

    return render_template('index.html', prediction = classification)

if __name__ == '__main__':
    app.run(debug=True)