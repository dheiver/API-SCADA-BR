import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect_anomalies', methods=['POST'])
def detect_anomalies():
    data = request.json['data']
    contamination = request.json['contamination']
    anomalies = detect_anomalies(data, contamination)
    return jsonify(anomalies)

def detect_anomalies(data, contamination):
    # Calculate the first quartile (q1) and third quartile (q3) using Pandas
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)

    # Calculate the Interquartile Range (IQR)
    iqr = q3 - q1

    # Identify the values as anomalies using IQR
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    anomalies_iqr = data[(data < lower_bound) | (data > upper_bound)]

    # Convert data to a 2D array (required by scikit-learn)
    X = data.values.reshape(-1, 1)

    # Isolation Forest
    isolation_forest = IsolationForest(contamination=contamination)
    isolation_forest.fit(X)
    anomalies_isolation_forest = data[isolation_forest.predict(X) == -1]

    # Local Outlier Factor (LOF)
    lof = LocalOutlierFactor(contamination=contamination)
    lof.fit(X)
    anomalies_lof = data[lof.fit_predict(X) == -1]

    # One-Class SVM
    one_class_svm = OneClassSVM(nu=contamination)
    one_class_svm.fit(X)
    anomalies_one_class_svm = data[one_class_svm.predict(X) == -1]

    # Combine the results of all methods to obtain a more comprehensive detection
    anomalies_combined = pd.concat([anomalies_iqr, anomalies_isolation_forest, anomalies_lof, anomalies_one_class_svm]).drop_duplicates()

    # Return the anomalous values found as a list
    return anomalies_combined.tolist()

if __name__ == '__main__':
    app.run(debug=True)
