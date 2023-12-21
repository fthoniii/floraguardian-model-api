from flask import Flask, request, jsonify
import io
import os
import numpy as np
from PIL import Image
from tensorflow import keras

app = Flask(__name__)

# Load model.h5 using Keras
model = keras.models.load_model("model.h5")

# Label available in model.h5
label = [
    "Nepenthaceae", "Orchidaceae", "Simaroubaceae", "Taxaceae", "Thymelaeaceae",
    "Araucariaceae", "Arecaceae", "Asteraceae", "Dipterocarpaceae", "Fagaceae",
    "Lauraceae", "Leguminosae", "Araceae", "Malvaceae"
]

def preprocess_image(image):
    image = image.resize((224, 224))
    img_array = np.asarray(image)
    img_array = img_array / 255.0
    return img_array

def predict_label(image):
    processed_img = preprocess_image(image)
    processed_img = np.expand_dims(processed_img, axis=0)
    pred = model.predict(processed_img)
    result = label[np.argmax(pred)]
    return result

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            file_content = request.files['file'].read()
            image = Image.open(io.BytesIO(file_content))
            pred_label = predict_label(image)
            return jsonify({"prediction": pred_label})
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return jsonify({"error": "Send a POST request with 'file' as form-data."})

if __name__ == "__main__":
    app.run(debug=True)