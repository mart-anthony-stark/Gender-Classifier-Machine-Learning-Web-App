from application import app
from flask import render_template, request
import json
import pickle
from sklearn.feature_extraction.text import CountVectorizer

clf = pickle.load(open('./gender_classifier.pkl', 'rb'))

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  cv = CountVectorizer()
  names = []
  names.append(request.form['name'])
  print(names)
  # vector = cv.transform(names)
  # print(vector)
  # prediction = clf.predict(vector)
  # print(prediction)
  return render_template('index.html')