# create a flask app for salary prediction 
# import the library 
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# create a flask app
app = Flask(__name__)

# load the model
pipeline= pickle.load(open('salary.pkl', 'rb'))

# create a homepage
@app.route('/')
def home():
    return render_template('index.html')

#create a predict function
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Use the exact column names as in the training data/model
    df = pd.DataFrame([{
        'Age': data['age'],
        'Education Level': data['education'],
        'Years of Experience': data['experience']
    }])
    prediction = pipeline.predict(df)
    return jsonify({'salary': round(prediction[0], 2)})

# run the app
if __name__ == '__main__':
    app.run(debug=False)
