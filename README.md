# Loan Prediction Website

Welcome to the Loan Prediction Website project! This project aims to create a web application that predicts whether a loan will be approved based on user input data. The project leverages machine learning algorithms and various libraries to deliver accurate predictions.

Table of Contents
Overview
Technologies Used
Usage
Dataset
Web Application

**Overview**

The Loan Prediction and Credit Classification Website uses a machine learning model to predict the likelihood of loan approval and classify your credit score into 3 different categories i.e, standard, good and excellent .

**Technologies**

It is built with the following technologies:
Machine Learning: For predictive modeling
Front-End: HTML and CSS for the web interface
Back-End: TensorFlow and Keras for model development and Scikit-learn for data processing
Features
User-friendly web interface for inputting data
Real-time loan approval predictions
Data visualization for better insights
Easy integration with other systems
Technologies Used
Python: Core programming language
Pandas: For data manipulation and analysis
TensorFlow & Keras: For building and training the machine learning model
Scikit-learn: For additional machine learning tools and techniques
Matplotlib: For data visualization
HTML, CSS & JavaScript: For the front-end design
Django: As a framework for back-end processing

**Usage**

1. Download Model by [click here](https://drive.google.com/file/d/1ID6ageHzRuk_rilRdZBGf9RVR_1ND6El/view?usp=sharing)
2. Extract File
3. Add the model file to Path
   ```
    \static
   ```
4. (Optional) Creat a Virtual Environment [Learn to Make Virtual Environment](https://freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
5. Now open the terminal and go to the Repo Folder.
6. Run these Comand in the Termial
7. To install all Required Package
   ```
        pip install -r requirement.txt
   ```
8. ```
       python manage.py makemigration
       python manage.py migrate
       python manage.py collectstatic
       python manage.py runserver
   ```

To start the web application, run the following command:

python manage.py runserver

Open your web browser and navigate to
http://127.0.0.1:8000/ to access the application.

**Dataset**

The dataset used for training the model is available on youdata.ai. Please download the dataset and place it in the data directory of the project.
[Cradit Classification ](https://datalink.youdata.ai/yc4nbjvk)

**Web Application**

The web application is built using Django. It provides a simple interface for users to input their data and receive a loan prediction.
