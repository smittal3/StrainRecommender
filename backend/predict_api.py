import pickle
import pandas as pd
import numpy as np
from flask_cors import CORS
from flask import Flask, jsonify, request
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
CORS(app)

@app.route('/getRec', methods=['GET'])
def get_recommendation():
  type = request.args.get('type')
  type = type.trim().split(",")
  flavors = request.args.get('flavors')
  flavors = flavors.trim().split(",")
  effects = request.args.get('effects')
  effects = effects.trim().split(",")

  # Creating user req string with all requested params
  for t in type:
      user_req = t + " "
      
  for flavor in flavors:
    user_req += flavor + " "
    
  for effect in effects: 
    user_req += effect + " "
    
  # Cleaning the user req 
  user_req = user_req.lower()
  user_req = np.asarray([user_req])
  
  distances, indices = knn.kneighbors((tfidf.transform(user_req)).todense())
  
  # Changing dimension of indices array from 2 to 1
  indices = indices[0]
  
  return str(strain_data.iloc[indices]['Strain'].values)



if __name__ == "__main__":
  file = open('strain_data.pkl', 'rb')
  # dump information to that file
  strain_data = pickle.load(file)
  
  file = open('models/kNN-5.pkl', 'rb')
  knn = pickle.load(file)
  
  file = open('models/tfidf_model.pkl', 'rb')
  tfidf = pickle.load(file)  
  
  file.close()
  
  app.run(debug=True, port=5000)

  
  
