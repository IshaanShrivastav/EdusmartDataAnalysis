# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:24:25 2019

@author: ishaan
"""

from flask import Flask, jsonify
from flask import render_template
import connect

#imporets for the bokeh library to draw
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

app = Flask(__name__)

@app.route("/home")
def home():
    
    return render_template('home.html')


#Incomplete quizzes path
@app.route("/home/incomplete/")
def incomplete():

    #Calls method to return dictionary for incomplete quizzes
    json = connect.queryUncompletedSR()
    
    #Return as json 
    return jsonify( json )

#avg score on the first try of SR Quizzes path
@app.route("/home/avgfirst/")
def avgFirst():

    #Calls method to return dictionary for the average score on the first try of quizzes
    json = connect.avgScoreFirstTry()
    
    #Return the dictionary as a json
    return jsonify( json )

#Path to see number of user created quizzes
@app.route("/home/numquizzes/")
def numQuizzes():
    
    #Returns dictionary for most popular quizzes made
    json = connect.mostPopularQuizzes()
    
    return jsonify( json )

#Path for the avg quiz score
@app.route("/home/avgQuiz/")
def avgPerQuiz():

    #Returns a dictionary for data on the avg score of the quizzes
    json = connect.avgScorePerQuiz()
    
    #Returnss dictionary as json
    return jsonify( json )

#Path for attempts on the lesson
@app.route("/home/attemptLesson/")
def attemptPerLess():
    
    #Calls method to return dictionary for attempts on the lesson
    json = connect.attemptPerLesson()
    
    #Returns the dictionary as a json
    return jsonify( json )


#Main method to run
if __name__ == '__main__':
    app.run(debug=True)
    