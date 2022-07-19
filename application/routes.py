from application import app
from flask import render_template, request
import pickle
from sklearn.feature_extraction.text import CountVectorizer

clf = pickle.load(open('./gender_classifier.pkl', 'rb'))
cv = pickle.load(open('./vectorizer.pkl', 'rb'))

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  names = []
  names.append(request.form['name'])
  vector = cv.transform(names).toarray()
  genders = ['Male', 'Female']
  prediction = clf.predict(vector)
  probability = clf.predict_proba(vector)[0][0] * 100
  result = genders[prediction[0]]
  print(result)
  return render_template('index.html',vars={"name": names[0], "result": result, "probability": probability})