# Flask utils
from flask import Flask, redirect, url_for, request, render_template
import pickle
import numpy as np


file = open('covid_prediction.pkl','rb')
rf = pickle.load(file)
file.close()

# Define a flask app
app = Flask(__name__)



@app.route('/')
def index1():
    return render_template('home.html')

@app.route('/symptom')
def symptom():
    return render_template('symptom.html')

@app.route('/prevention')
def prevention():
    return render_template('prevention.html')


@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        my_dict = request.form
        gender = int(my_dict['gender'])
        if gender == 1:
            patient_type_2 = 0
        else:
            patient_type_2 = 1
        intubed = int(my_dict['intubed'])
        if intubed == 1:
            intubed_1 = 1
            intubed_2 = 0
        elif intubed == 2:
            intubed_1 = 0
            intubed_2 = 1


        pne = int(my_dict['pne'])
        if pne == 1:
            pneumonia_2 = 1 
        elif pne == 2:
            pneumonia_2 = 1

        age = int(my_dict['age'])

        pne1 = int(my_dict['pne1'])
        if pne1 == 1:
            pregnancy_1 = 1
            pregnancy_2 = 0
        elif pne1 == 2:
            pregnancy_1 = 0
            pregnancy_2 = 1
        

        pne2 = int(my_dict['pne2'])

        if pne2 == 1:
            diabetes_1 = 1
            diabetes_2 = 0
        elif pne2 == 2:
            diabetes_1 = 0
            diabetes_2 = 1
        
        pne3 = int(my_dict['pne3'])

        if pne3 == 1:
            asthma_1 = 1
            asthma_2 = 0
        elif pne3 == 2:
            asthma_1 = 0
            asthma_2 = 1
        
        pne4 = int(my_dict['pne4'])

        if pne4 == 1:
            hypertension_1 = 1
            hypertension_2 = 0
        elif pne4 == 2:
            hypertension_1 = 0
            hypertension_2 = 1
        
        pne5 = int(my_dict['pne5'])

        if pne5 == 1:
            other_disease_1 = 1
            other_disease_2 = 0
        elif pne5 == 2:
            other_disease_1 = 0
            other_disease_2 = 1
        
        pne6 = int(my_dict['pne6'])

        if pne6 == 1:
            cardiovascular_1 = 1
            cardiovascular_2 = 0
        elif pne6 == 2:
            cardiovascular_1 = 0
            cardiovascular_2 = 1

           
        pne7 = int(my_dict['pne7'])
       
        if pne7 == 1:
            tobacco_1 = 1
            tobacco_2 = 0
        elif pne7 == 2:
            tobacco_1 = 0
            tobacco_2 = 1
        
        pne8 = int(my_dict['pne8'])

        if pne8 == 1:
            contact_other_covid_1 = 1
            contact_other_covid_2 = 0
        elif pne8 == 2:
            contact_other_covid_1 = 0
            contact_other_covid_2 = 1
        
        pne9 = int(my_dict['pne9'])

        if pne9 == 1:
            icu_1 = 1
            icu_2 = 0
        elif pne9 == 2:
            icu_1 = 0
            icu_2 = 1
        
        pne10 = int(my_dict['pne10'])

        if pne10 == 1:
            covid_res = 1
        elif pne10 == 2:
            covid_res = 2
        elif pne10 == 3:
            covid_res = 3
                
        input_features = [age, covid_res, patient_type_2, intubed_1, intubed_2,
        pneumonia_2, pregnancy_1, pregnancy_2, diabetes_1, diabetes_2,
        asthma_1, asthma_2, hypertension_1, hypertension_2,
        other_disease_1, other_disease_2, cardiovascular_1,
        cardiovascular_2, tobacco_1, tobacco_2, contact_other_covid_1,
        contact_other_covid_2, icu_1, icu_2]
        
        inf = rf.predict([input_features])
        
        if inf == 1:
            inf = 'POSITIVE'
        elif inf == 2:
            inf = 'NEGATIVE'
        elif inf == 3:
            inf = 'RESULT IN PROGRESS...'
        print(inf)

        return render_template('show.html',inf = inf) 
               
    return render_template('predict.html')





if __name__ == '__main__':
    app.run(debug=True)