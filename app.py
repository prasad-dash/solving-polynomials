from operator import methodcaller
import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
import nltk
def textUtility(s):
  tokenizer = nltk.RegexpTokenizer(r"\w+")
  s=' '.join(tokenizer.tokenize(s))
  return s  
app= Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
vectoriser=pickle.load(open('vectorizer.pkl','rb'))
vocabulary=pickle.load(open('vocabulary.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    input_values=[x for x in request.form.values()][0]
    input_values=[word for word in input_values.split() if word in vocabulary]
    input_values=' '.join(input_values)
    if(input_values==''):
        return render_template('index.html',prediction=2)    
    input_values=textUtility(input_values)
    X=vectoriser.transform([input_values])
    prediction=model.predict(X)[0]
    print(prediction)
    print(input_values)
    feelings={
        0:"Neutral",
        1:"Positive",
        -1:"Negative"
                }
    return render_template('index.html',prediction=prediction)
if __name__=="__main__":
    app.run()