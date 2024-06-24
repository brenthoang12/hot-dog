import os # test number of file
import numpy as np
import h5py
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import RMSprop


datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)


###### augmente data for model training ######

train_gen = datagen.flow_from_directory(
    "model/altered/train/",
    target_size=(300, 300),
    batch_size=32,
    class_mode="binary"
)


validation_gen = datagen.flow_from_directory(
    "model/altered/test/",
    target_size=(300, 300),
    batch_size=32,
    class_mode="binary"
)

###### Convnet model ######

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(300, 300, 3)))
model.add(tf.keras.layers.MaxPooling2D(2, 2))

model.add(tf.keras.layers.Conv2D(32, (3,3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(2,2))

model.add(tf.keras.layers.Conv2D(64, (3,3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(2,2))

model.add(tf.keras.layers.Conv2D(64, (3,3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(2,2))

model.add(tf.keras.layers.Conv2D(64, (3,3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(2,2))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(512, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(
    loss='binary_crossentropy',
    optimizer=RMSprop(learning_rate=0.001),
    metrics=['accuracy']
)

###### Fit model ######

history = model.fit(
    train_gen,
    steps_per_epoch=8,
    epochs=15,
    #validation_data=validation_generator,    
    #validation_steps=8,
    verbose=1)

model.save('model/model.h5') # this is a dog shit model (have to come up with new ways)

model.summary()


# using colab to convert h5 to json

# tensorflowjs_converter --input_format=keras /Users/brenthoang/Documents/Test_Project/hot-dog/model/test.h5 /Users/brenthoang/Documents/Test_Project/hot-dog/model

# tensorflowjs_converter --input_format=keras /content/drive/MyDrive/model-test/hotdogmodel.h5 /content/drive/MyDrive/model-test


