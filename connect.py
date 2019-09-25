# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:52:25 2019

@author: ishaan
"""

import pyodbc 

#Global variable to see if connection has been made
connection = None

#Function to initialize initial connection
def init():
    global connection 
    
    #Connects to the database
    connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                           "Server=DESKTOP-NBS89UI;"
                           "Database=eduservice_edusmart;"
                           "Trusted_Connection=yes;")
        
#Method to check the number of incompleted quizzes
def queryUncompletedSR():
    global connection
    
    #Checks if connection has been made yet
    if connection is None:
        init()
    
    #Get cursor from the connection made to the database    
    cursor = connection.cursor()
    
    #Executes query to get top 10 incompleted quizzes
    cursor.execute('SELECT top 10 itemid, description, sum_status FROM CommonEdumatics.dbo.EDS_Items edi INNER JOIN ( SELECT SUM(Status) Sum_Status, ItemID FROM [eduservice_edusmart].[dbo].[SR_Result] WHERE Status = -1 Group By ItemID ) SR ON SR.ItemId = edi.id Order By Sum_Status Asc')
    
    #Gets the columns from the selected table
    columns = [column[0] for column in cursor.description]

    #Creates and fills dictionary for top 10 incompoleted SR Quizzes   
    dictionary = []
    for row in cursor.fetchall():
        dictionary.append(dict(zip(columns, row)))
        
    obj = {}
    obj[0] = dictionary
    
    return obj

#Checks the average score of first try of quizzes
def avgScoreFirstTry():
    global connection
    
    #Checks if connection has been made yet
    if connection is None:
        init()
        
    #Get cursor from the connection made to the database         
    cursor = connection.cursor()
    
    #Executes query to get average score for the first try of quizzes
    cursor.execute('SELECT TOP 10 * FROM ( SELECT ItemID, AVG(TotalScore)/3 * 100 avgScore FROM [eduservice_edusmart].[dbo].[SR_RESULT] WHERE AttemptNbr=1 GROUP BY ItemID ) AS x WHERE avgScore!=0 ORDER BY avgScore')
    
    #Gets the columns from the selected table
    columns = [column[0] for column in cursor.description]
    
    #Creates and fills dictionary for the average score on the first try of SR quizzes   
    dictionary = []
    for row in cursor.fetchall():
        dictionary.append(dict(zip(columns, row)))
    
    obj = {}
    obj[0] = dictionary
    
    return obj

#Checks the most popular user made quizzes
def mostPopularQuizzes():
    global connection
    
    
    #Checks if connection has been made yet
    if connection is None:
        init()
        
    #Get cursor from the connection made to the database 
    cursor = connection.cursor()
    
    #Executes query to get top 10 most popular quizzes 
    cursor.execute('SELECT top 10 Category, COUNT(*) as NumOfQuizzes FROM [eduservice_edusmart].[dbo].[QZOResult] GROUP BY Category')
    
    #Gets the columns from the selected table
    columns = [column[0] for column in cursor.description]
    
    #Creates and fills dictionary for the average score on the first try of SR quizzes   
    dictionary = []
    for row in cursor.fetchall():
        dictionary.append(dict(zip(columns, row)))
    
    obj = {}
    obj[0] = dictionary
    
    return obj
    

#Gets the average score for the quizzes ( in a different section )
def avgScorePerQuiz():
    global connection
    
    #Checks if connection has been made yet
    if connection is None:
        init()
  
    #Get cursor from the connection made to the database        
    cursor = connection.cursor()
    
    #Executes the query for the average score of quizzes in a different section
    cursor.execute('SELECT TOP 10 * FROM( SELECT ItemID, AVG(HighestScore) avgScore FROM eduservice_edusmart.dbo.EDS_ContentAccessTracking item GROUP BY ItemID ) AS x WHERE avgScore!=0 ORDER BY avgScore')
    
    
    #Gets the columns from the selected table    
    columns = [column[0] for column in cursor.description]

    #Fills dictionary with the lists of information
    dictionary = []
    for row in cursor.fetchall():
        dictionary.append(dict(zip(columns, row)))
    
    obj = {}
    obj[0] = dictionary
    
    return obj

#Checks the number of attempts people make per lesson
def attemptPerLesson():
    global connection
    
    #Checks if connection has been made yet
    if connection is None:
        init()
    
    #Get cursor from the connection made to the database 
    cursor = connection.cursor()
    
    #Executes query to get number of attempts per lesspm
    cursor.execute('SELECT Top 10 SUM(TimeSpent) AS Time_Sum, SUM(AccessCount) AS Access_Sum, LessonID FROM eduservice_edusmart.dbo.LNTracking GROUP BY LessonID ORDER BY Access_Sum desc')

    #Gets the columns from the selected table
    columns = [column[0] for column in cursor.description]

    #Fills dictionary with the information from the table in the database
    dictionary = []
    for row in cursor.fetchall():
        dictionary.append(dict(zip(columns, row)))
    
    obj = {}
    obj[0] = dictionary
    
    return obj
    
    
    
    
    
