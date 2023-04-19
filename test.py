import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image as image_utils
from tensorflow.keras.models import load_model
from utils import get_classes

def visualize_classification(model_path, image_path, class_labels):
    """
    Visualize the classification of an image using a Keras model.

    :param model_path: str, path to the trained Keras model
    :param image_path: str, path to the input image
    :param class_labels: list of str, class labels corresponding to the model output
    """
    # Load the model
    model = load_model(model_path)

    # Load and preprocess the image
    image = image_utils.load_img(image_path, target_size=(224, 224))
    image_array = image_utils.img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array /= 255.0

    # Perform inference
    predictions = model.predict(image_array)
    ind = np.argpartition(predictions[0], -3)[-3:]
    ind = ind[::-1]
    # predicted_class_idx = np.argmax(predictions[0])
    predicted_class_label = [class_labels[x] for x in ind]
    confidence = [predictions[0][x] for x in ind]

    # Display the image and prediction
    plt.imshow(image)
    plt.title(f"""
    Predicted#1: {predicted_class_label[0]} ({confidence[0] * 100:.2f}%)
    Predicted#2: {predicted_class_label[1]} ({confidence[1] * 100:.2f}%)
    Predicted#3: {predicted_class_label[2]} ({confidence[2] * 100:.2f}%)
    """, x=0.9, y=0.9)
    plt.axis("off")
    plt.show()

# Example usage
model_path = "./models/minion_image_classifier.h5"
image_path = "./data/test/bob2.jpeg"
class_labels = get_classes() # Replace with your class labels

visualize_classification(model_path, image_path, class_labels)