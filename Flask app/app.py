# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:18:55 2020

@author: ut
"""


from flask import Flask , render_template ,request
import pickle
app  = Flask(__name__)
model = pickle.load(open('loanprediction.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html.html',data="null")
@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
      gender = request.form['Gender']
      married= request.form['Married']
      dependents= request.form['Dependents']
      education= request.form['Education']
      employed= request.form['Employed']
      income1= request.form['Income1']
      income2= request.form['Income2']
      crhist= request.form['Crhist']
      area= request.form['Area']
      loan= request.form['Amount']
      term= request.form['Term']
      data=[[int(gender),int(married),int(dependents),int(education),int(employed),int(income1),int(income2),int(crhist),int(area),int(loan),int(term)]]
      p=model.predict(data)  
      if p[0]==1:
          prediction="Loan To Be Granted"
      else:
          prediction="Loan Not To Be Granted"
      return render_template('index.html.html',prediction="Prediction: "+prediction)
if __name__=='__main__':
    app.run(debug=True)