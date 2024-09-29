# Asteroid Hazard Prediction

## Overview

The **Asteroid Hazard Prediction** project is a web application that predicts whether an asteroid is potentially hazardous to Earth based on various parameters. This app utilizes a machine learning model trained on NASA asteroid data to classify asteroids as either hazardous or non-hazardous. The application is built using **Streamlit**, a powerful library for creating interactive web applications in Python.

## Features

- Input asteroid parameters, including absolute magnitude, estimated diameter, relative velocity, miss distance, and more.
- Predict if an asteroid is hazardous based on user inputs.
- Visual feedback with images indicating whether the asteroid is hazardous or not.
- An aesthetically pleasing background featuring a galaxy image to enhance user experience.

## Technologies Used

- **Python**: The primary programming language used for building the application.
- **Streamlit**: A library for creating interactive web apps in Python.
- **Scikit-learn**: For machine learning model creation and prediction.
- **Pandas**: For data manipulation and analysis.
- **Joblib**: For loading pre-trained machine learning models.

## Installation

To run this project locally, follow these steps:

### Prerequisites

Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/yourusername/asteroid-hazard-prediction.git
cd asteroid-hazard-prediction
Install Dependencies
You can install the required libraries using pip:
pip install streamlit scikit-learn pandas joblib
Download the Dataset and Model
Make sure you have the following files in your project directory:

nasa.csv: The dataset containing asteroid information.
model.pkl: The pre-trained machine learning model.
scaler.pkl: The scaler used for feature scaling.
ast.png: Image indicating a hazardous asteroid.
giphy.gif: Image indicating a non-hazardous asteroid.
galaxy.jpg: Background image for the web app.
Running the Application
To start the Streamlit application, run the following command in your terminal:


Here’s a detailed README for your Asteroid Hazard Prediction project, written in Markdown style. You can customize it further as needed!

markdown
Copy code
# Asteroid Hazard Prediction

## Overview

The **Asteroid Hazard Prediction** project is a web application that predicts whether an asteroid is potentially hazardous to Earth based on various parameters. This app utilizes a machine learning model trained on NASA asteroid data to classify asteroids as either hazardous or non-hazardous. The application is built using **Streamlit**, a powerful library for creating interactive web applications in Python.

## Features

- Input asteroid parameters, including absolute magnitude, estimated diameter, relative velocity, miss distance, and more.
- Predict if an asteroid is hazardous based on user inputs.
- Visual feedback with images indicating whether the asteroid is hazardous or not.
- An aesthetically pleasing background featuring a galaxy image to enhance user experience.

## Technologies Used

- **Python**: The primary programming language used for building the application.
- **Streamlit**: A library for creating interactive web apps in Python.
- **Scikit-learn**: For machine learning model creation and prediction.
- **Pandas**: For data manipulation and analysis.
- **Joblib**: For loading pre-trained machine learning models.

## Installation

To run this project locally, follow these steps:

### Prerequisites

Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/yourusername/asteroid-hazard-prediction.git
cd asteroid-hazard-prediction
Install Dependencies
You can install the required libraries using pip:

bash
Copy code
pip install streamlit scikit-learn pandas joblib
Download the Dataset and Model
Make sure you have the following files in your project directory:

nasa.csv: The dataset containing asteroid information.
model.pkl: The pre-trained machine learning model.
scaler.pkl: The scaler used for feature scaling.
ast.png: Image indicating a hazardous asteroid.
giphy.gif: Image indicating a non-hazardous asteroid.
galaxy.jpg: Background image for the web app.
Running the Application
To start the Streamlit application, run the following command in your terminal:

bash
Copy code
streamlit run app.py
This will launch the application in your default web browser, usually at http://localhost:8501.

Usage
Open the web application in your browser.
Fill in the input fields with the asteroid's parameters.
Click the Predict button to determine if the asteroid is hazardous.
The application will display an appropriate message along with an image indicating the asteroid's hazard status.
asteroid-hazard-prediction/
│
├── app.py               # Main Streamlit application code
├── model.pkl            # Pre-trained machine learning model
├── scaler.pkl           # Scaler for input feature normalization
├── nasa.csv             # Dataset containing asteroid information
├── ast.png              # Image for hazardous asteroids
├── giphy.gif            # Image for non-hazardous asteroids
└── galaxy.jpg           # Background image for the web application

Acknowledgments
Special thanks to NASA for providing the dataset used in this project.
The machine learning model was trained using Scikit-learn, and the web application was built using Streamlit.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any inquiries or feedback, feel free to reach out to:

Vaishwik Vishwakarma
Email: earthicon31@gmail.com
GitHub: Vaishwik369

