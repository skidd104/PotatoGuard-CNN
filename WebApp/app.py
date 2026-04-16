from flask import Flask, render_template, request, url_for
import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image

app = Flask(__name__)


# This tells Flask where the folder is globally
app.config['UPLOAD_FOLDER'] = 'static/images'


# 1. Load the model
model = tf.keras.models.load_model('./models/modelv2.h5')

model.predict(np.zeros((1, 224, 224, 3)))

# 0: Early Blight (E), 1: Late Blight (L), 2: Healthy (h)
CLASS_NAMES = ['Early Blight', 'Late Blight', 'Healthy']

@app.route('/', methods=['GET'])
def index():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def predict():
    if 'imagefile' not in request.files:
        return render_template('upload.html', prediction="No file uploaded")

    imagefile = request.files['imagefile']

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
        
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], imagefile.filename)
    imagefile.save(image_path)

    # 3. Manual Preprocessing
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    
    # Scale pixels from [0, 255] to [-1, 1]
    img_array = img_array / 127.5
    img_array = img_array - 1.0
    
    img_array = np.expand_dims(img_array, axis=0)

    # 4. Predict
    predictions = model.predict(img_array)
    
    # Check your terminal for these values!
    print(f"DEBUG - Raw Array: {predictions}")
    
    predicted_index = np.argmax(predictions, axis=1)[0]
    predicted_label = CLASS_NAMES[predicted_index]
    confidence_formatted = "{:.2f}".format(100 * np.max(predictions))


    # We pass 'image_path' relative to the static folder for the <img> tag
    display_path = url_for('static', filename='images/' + imagefile.filename)

    return render_template(
        'results.html', 
        label=predicted_label, 
        confidence=confidence_formatted, 
        image_path=display_path
    )

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/tips')
def tips():
    return render_template('tips.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)