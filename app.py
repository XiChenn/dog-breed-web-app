import base64

from flask import Flask, render_template, request, jsonify
from fastai.vision import *
import re

app = Flask(__name__)
learn = load_learner('models/dog-breed')


@app.route('/')
def home():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload():
    image_data = re.sub('^data:image/.+;base64,', '', request.data.decode('utf-8'))
    return predict_image_from_bytes(base64.b64decode(image_data))


def predict_image_from_bytes(image_bytes):
    img = open_image(BytesIO(image_bytes))
    pred_class, _, _ = learn.predict(img)

    return jsonify({
        'breed': ' '.join(str(pred_class).split('_'))
    })


if __name__ == '__main__':
    app.run()
