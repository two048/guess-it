from flask import Flask, request
from flask_cors import CORS
from keras.applications import ResNet50
from keras.applications.resnet import preprocess_input, decode_predictions
import keras.utils as image
import numpy as np
import base64
import PIL

app = Flask(__name__)
CORS(app)
model = ResNet50(weights='imagenet')

@app.route('/', methods=['POST'])
def process():
    img = request.get_json()['image']
    return detect(img)

def detect(b64):
    decoded_img = base64.b64decode(b64)

    img_file = open('img.jpg', 'wb')
    img_file.write(decoded_img)
    img_file.close()

    img = image.load_img('img.jpg', target_size=(224, 224))

    processed_img = image.img_to_array(img)
    processed_img = np.expand_dims(processed_img,axis=0)
    processed_img = preprocess_input(processed_img)

    pred = model.predict(processed_img)
    prediction = [decode_predictions(pred,top=10)[0][i][1] for i in range(10)]

    return {'prediction': prediction}

