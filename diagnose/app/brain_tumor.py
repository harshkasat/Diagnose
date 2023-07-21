import tensorflow as tf
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np


def prediction(image_path):
    # Using save_model
    model = tf.keras.models.load_model('Brain Tumor savedmodel//2019-06-07_VGG_model.h5')


    img_path = f'{image_path}' # Replace with the path to your input image
    img = image.load_img(img_path, target_size=(224, 224))  # Resize the image to match the model input size


    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    input_image = tf.keras.applications.mobilenet.preprocess_input(img_array)  # Preprocess the image for the specific model


    predictions = model.predict(input_image)


    predicted_class = np.argmax(predictions, axis=1)
    confi = np.max(predictions, axis=1)


    class_list = ["Brain Tumor", "Not Brain Tumor"]


    if predicted_class.size >0.5 and confi > 0.9:
        return  class_list[0]
    else: 
         class_list[1]


