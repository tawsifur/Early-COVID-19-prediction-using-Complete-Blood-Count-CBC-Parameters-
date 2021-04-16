# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 00:54:16 2021

@author: LEGION
"""

  
# Importing essential libraries

from flask import Flask, render_template, request
import pickle
import numpy as np
import math



app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Neutrophils_Count=float(request.form['Neutrophils_Count'])
        Age=int(request.form['Age'])
        Platelet_Count=float(request.form['Platelet_Count'])
        Monocytes=float(request.form['Monocytes'])
        White_Blood_Cell_Count=float(request.form['White_Blood_Cell_Count'])
        Lymphocyte_Count=float(request.form['Lymphocyte_Count'])
        Red_Blood_Cell_Distribution_Width=float(request.form['Red_Blood_Cell_Distribution_Width'])
        
        output= -12.75911+0.5784669*Neutrophils_Count+0.0724752*Age-0.009611*Platelet_Count+0.0931182*Monocytes+0.0064276*White_Blood_Cell_Count-3.567051*Lymphocyte_Count+0.7140086*Red_Blood_Cell_Distribution_Width 
        dp=1/(1+math.exp(-output))
        dp=round(dp,4)
        return render_template('result.html', prediction=dp)

if __name__ == '__main__':
	app.run(debug=True)