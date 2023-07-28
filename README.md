
# Medical Image Classification Web Application

This web application is built using Django and utilizes pre-trained machine learning models to classify medical images for brain tumor, chest X-ray, and melanoma cancer. Users can upload their medical images and get predictions on whether the images indicate the presence of cancer.

## Table of Contents
1. Installation
2. Usage
3. Features
4. Technologies Used
5. Model Information
6. Data Sources
7. Docker pull


## 1. Installation
### Prerequisites
- Python  3.11.2
- Django 4.2.3
- TensorFlow (for using the machine learning models)
- Other Python libraries as specified in the requirements.txt

### Setup
1. Clone this repository to your local machine. ```git clone https://github.com/harshkasat/Diagnose.git```
2. Create a virtual environment: ```python -m venv .venv```
3. Activate virtual environment: ``` .\.venv\Scripts\activate```
4. Install the required packages: ```pip install -r requirements.txt ```
5. Change dir for  Django development server: ``` cd diagnose```
6. Run the Django development server: ``` python manage.py runserver ```

5. Access the application at http://localhost:8000/

## 2. Usage
1. Upload a medical image for classification.
2. The application will use the pre-trained machine learning models to make predictions.
3. The results will be displayed, indicating whether the image shows signs of brain tumor, chest X-ray abnormalities, or melanoma cancer.

## 3. Features
- Image upload and classification for brain tumor detection.
- Image upload and classification for chest X-ray abnormalities.
- Image upload and classification for melanoma cancer detection.

## 4. Technologies Used
- Django: Web framework for backend development.
- HTML, CSS: Frontend development.
- TensorFlow: Machine learning library for the models.
- Python: Backend and model implementation.

## 5. Model Information
- Brain Tumor Model: Trained on a dataset of brain MRI images using CNN architecture.
- Chest X-ray Model: Trained on a dataset of chest X-ray images using transfer learning with a pre-trained model.
- Melanoma Cancer Model: Trained on a dataset of skin lesion images using CNN architecture.

## 6. Data Sources
- Brain Tumor Dataset: [Brain Tumor](https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection)
- Chest X-ray Dataset: [Pneumonia](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- Melanoma Cancer Dataset: [Melanoma Cancer](https://www.kaggle.com/datasets/hasnainjaved/melanoma-skin-cancer-dataset-of-10000-images)

## 7. Acknowledgments
- Install Docker
- ```docker pull zedmate/python-django ```




