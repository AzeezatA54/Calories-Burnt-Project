from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('calories.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/')

@app.route('/main_template',methods=["GET"])
def main_template():

    #render form
    return render_template('Index.html')

#get form data
@app.route('/predict',methods=['GET','POST'])
def predict():

    #checking request type
    str_req_type = request.method

    #convert string value into numeric value
    if request.method == str(str_req_type):

        if request.args.get('gender') == 'Male':
            gender = 1

        else:
            gender = 0

        age = request.args.get('age')

        duration = request.args.get('duration')

        heart_Rate = request.args.get('heart_rate')

        temp = request.args.get('temp')

        height = request.args.get('height')

        weight = request.args.get('weight')

        #store form values into set
        values = [gender, age, height, weight, duration, heart_Rate,temp]

        #turn into array & reshape array for prediction
        input_array = np.asarray(values)
        final_features = input_array.reshape(1, -1)

        predicted = model.predict(final_features)
        

        return render_template ('index.html', prediction_text = 'You will burn {} calories'.format(predicted))
    else:
        return render_template('index.html')
    
     
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
