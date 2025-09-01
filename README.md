# Introduction to DevOps 
(Merged - CSIZG514/SEZG514) (S1-25)

## Objective 
This assignment aims to provide students with hands-on experience in fundamental DevOps practices. By completing this assignment, students will gain proficiency in version control with Git and GitHub, containerization using Docker, and implementing continuous integration and continuous delivery (CI/CD) pipelines with GitHub Actions. 

## Problem statement
You are tasked with developing a robust and automated application for ACEest_Fitness and Gym, a burgeoning startup. As a Junior DevOps Engineer, your primary responsibility is to establish a streamlined development and deployment workflow that ensures code quality, consistency, and efficient delivery. Your solution should encompass the following key phases:
1.	Application Development
2.	Version Control System (VCS) Implementation
3.	Unit Testing Framework Integration
4.	Automated Testing Configuration
5.	Containerization with Docker
6.	CI/CD Pipeline with GitHub Actions

## Tools Used:
     > Flask 2.3.2
     > Python 3.13
     > Docker Engine 28.3.3
     > Nginx 1.29.1
     > Git 2.51.0
     > GitHub Desktop
     > Visual Studio code 1.103.2

## Problem statement deliverables:
#### Goal : Build a Flask web app for ACEest-Fitness
#### Step 1: 
    > Use the code provided in ACEest-Fitness.py (in Main Branch)
    > Add a Flask structure to it and save it as app.py, example given below (in Master Branch)
    > 
```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

workouts = []

@app.route('/')

def indexhome():
return render_template('index.html', workouts=workouts)

@app.route('/add', methods=['POST'])

def add_workout():
workout = request.form.get('workout')
duration = request.form.get('duration')
if not workout or not duration:
return "Please enter both workout and duration.", 400
try:
   duration = int(duration)
   workouts.append({'workout': workout, 'duration': duration})
         return redirect(url_for('home'))
   except ValueError:
        return "Duration must be a number.", 400

if __name__ == '__main__':
   app.run(debug=True)
```
