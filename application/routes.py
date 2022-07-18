from application import app
from flask import render_template, request
import json

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  name = request.form['name']
  return render_template('index.html')