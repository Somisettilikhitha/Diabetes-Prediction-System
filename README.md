🩺 Diabetes-Prediction-System

A Machine Learning powered web application that predicts the probability of diabetes based on medical parameters such as Glucose Level, Insulin, BMI, and Age.
The system provides a risk percentage, risk level classification (Low, Medium, High), and a visual progress bar to help users understand the prediction easily.

------------------------------------------------------------------------------------------------------------------------------------------

🚀 Project Overview

Diabetes is a common chronic disease that requires early detection and monitoring.
This project uses a machine learning model trained on a diabetes dataset to predict the likelihood of diabetes and display the results through an interactive Flask web application.

The application allows users to enter health parameters and instantly see:
1. Diabetes risk percentage
2. Risk category (Low / Medium / High)
3. Medical advice
4. A visual progress bar indicating probability

------------------------------------------------------------------------------------------------------------------------------------------

🧠 Machine Learning Model : The model is trained using the Support Vector Machine (SVM) algorithm.

Features Used : 
*** Glucose Level
*** Insulin
*** Body Mass Index (BMI)
*** Age

Data Preprocessing : 
*** Feature selection
*** Data scaling using MinMaxScaler

Output : 
*** Probability of diabetes
*** Risk level classification

--------------------------------------------------------------------------------------------------------------------------------------------

🛠 Technologies Used : 

- 🐍 Python – Programming Language
- 🌐 Flask – Web Framework
- 🤖 Scikit-learn – Machine Learning Library
- 🔢 NumPy – Numerical Computing
- 🐼 Pandas – Data Analysis
- 🧾 HTML – Web Structure
- 🎨 CSS – Web Styling

------------------------------------------------------------------------------------------------------------------------------------------

📁 Project Structure
Diabetes-Prediction
│
├── app.py
├── model.pkl
├── diabetes.csv
├── diabetes.ipynb
│
├── templates
│   └── index.html
│
├── static
│   ├── css
│   │   └── style.css
│   └── images
│       └── diabetes-bg.png
│
├── requirements.txt
└── README.md

--------------------------------------------------------------------------------------------------------------------------------------------

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Somisettilikhitha/Diabetes-Prediction-System

2️⃣ Navigate to Project Folder
cd Diabetes-Prediction-System

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Flask App
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000

-------------------------------------------------------------------------------------------------------------------------------------------

📊 Example Prediction

Input Example:

Feature	                       Value             
Glucose	                        170
Insulin	                        150
BMI	                             36
Age	                             55

Output:
High Risk: 94.34%
Please consult a doctor.

A visual progress bar also indicates the diabetes probability.

----------------------------------------------------------------------------------------------------------------------------------------

🎯 Key Features

Machine Learning based diabetes prediction

Probability-based risk assessment

Risk level classification

Modern responsive user interface

Visual risk progress bar

Flask-based web deployment

---------------------------------------------------------------------------------------------------------------------------------------

🔮 Future Improvements

Add more health parameters

Deploy the application using Docker or Cloud

Add user authentication

Connect with healthcare APIs

Improve prediction accuracy with advanced models

--------------------------------------------------
👩‍💻 Author 
Likhitha Somisetti

----------------------------------------------------------------------------------------------------------------------------------------

⭐ If you like this project

Give this repository a ⭐ on GitHub!
