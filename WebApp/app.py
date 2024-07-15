from flask import Flask, render_template, request
import pickle
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.optimizers import RMSprop



app = Flask(__name__)
model = pickle.load(open('models/model_ni_michael_10.pkl', 'rb'))


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('iphone.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile= request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    img = image.load_img(image_path, target_size=(200,200))
    img = np.array(img)
    img = img / 255.0

    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)

    predicted_class = np.argmax(predictions, axis=1)
    
    print (predicted_class)


    return render_template('iphone.html', prediction=predicted_class)


if __name__ == '__main__':
    app.run(port=3000, debug=True)