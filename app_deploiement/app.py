import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle



app = Flask(__name__)
import os
import pickle

# Get the absolute path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the 'model.pkl' file
model_path = os.path.join(script_dir, 'model.pkl')

# Load the model
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    if output == 1:
        response_text = 'demande de crédit acceptée'
    else:
        response_text = 'demande de crédit refusée'

    return render_template('index.html',prediction_text='La réponse à votre demande de crédit est {}'.format(response_text))


if __name__ == "__main__":
    app.run(debug=True)