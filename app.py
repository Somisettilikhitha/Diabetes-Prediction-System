import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

dataset = pd.read_csv('diabetes.csv')

dataset_X = dataset.iloc[:,[1, 2, 5, 7]].values

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0,1))
dataset_scaled = sc.fit_transform(dataset_X)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict( sc.transform(final_features) )

    # Probability calculation
    probability = model.predict_proba(sc.transform(final_features))[0][1]
    risk_percent = round(probability * 100, 2)

    # Risk levels
    if risk_percent < 30:
        message = "🟢 Low Risk"
        advice = "No immediate signs of diabetes."
        color = "low-risk"

    elif risk_percent < 70:
        message = "🟡 Medium Risk"
        advice = "Consider medical advice."
        color = "medium-risk"

    else:
        message = "🔴 High Risk"
        advice = "Please consult a doctor."
        color = "high-risk"

    return render_template('index.html', message=message, advice=advice, color=color, risk_percent=risk_percent)
if __name__ == "__main__":
    app.run(debug=True)
