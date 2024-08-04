# process image
def preprocess_image(image):
    image = image.resize(128)
    image = np.expand_dims(image, axis=0)
    return image

# load model
def creat_model():
    model = tf.keras.Sequential([ 
        tf.keras.layers.Rescaling(1./255, input_shape=(128, 128, 3)),
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
model.load_weights('/Users/brenthoang/Documents/Test_Project/hot-dog/model/training_2/cp-0005.weights.h5')


# predict image
def get_prediction(model, image):
    result = model.predict(image)
    result = 1 if float(result[0]) > .5 else 0
    return result