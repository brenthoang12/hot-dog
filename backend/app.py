from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

# process image
def preprocess_image(image, target_size):
    image = image.resize(target)


# load model
def creat_model():
    model = tf.keras.Sequential([ 
        tf.keras.layers.Rescaling(1./255, input_shape=(SIDE_LEN, SIDE_LEN, 3)),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=[tf.keras.metrics.BinaryCrossentropy(from_logits=True, name='binary_crossentropy'),'accuracy'])
    
    return model

model = creat_model()
model.load_weights()



@app.route('/')
def index():
    return render_template('frontend/index.html')

if __name__ == '__main__':
    app.run(debug=True)