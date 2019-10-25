import os
from app import app
from flask import render_template, request, redirect

import math
import random


# INDEX

@app.route('/')
@app.route('/input')
def index():
    return render_template("input.html")

@app.route('/results', methods = ["GET", "POST"])
def results():
    #Storing user inputs as the variable userdata as a dictionary
    userdata = dict(request.form)
    freq_q_1 = int(userdata['freq_q_1'])
    freq_q_2 = int(userdata['freq_q_2'])
    freq_q_3 = int(userdata['freq_q_3'])
    questions_per_test = int(userdata['questions_per_test'])
    tests_number = userdata['tests_number']

    a = freq_q_1/(freq_q_1 + freq_q_2 + freq_q_3)
    b = freq_q_2/(freq_q_1 + freq_q_2 + freq_q_3)
    c = freq_q_3/(freq_q_1 + freq_q_2 + freq_q_3)
    #I am using floors to underestimate the number of questions that we create
    questions_1 = math.floor(a * questions_per_test/100)
    questions_2 = math.floor(b * questions_per_test/100)
    questions_3 = math.floor(c * questions_per_test/100)
    #Sometimes the floor will be off, so I am adding questions back randomly based on that
    #I am using floors instead of rounding because floors guarantee that the number will be less than the original percentage, so we know to add questions back. Rounding makes it much more mess because the final result could either be greater or less than if it is not equal to.
    if questions_1 + questions_2 + questions_3 < questions_per_test:
        while questions_1 + questions_2 + questions_3 < questions_per_test:
            num = random.randint(1,3)
            if num == 1:
                questions_1 += 1
            if num == 2:
                questions_2 += 1
            else:
                questions_3 += 1

    questions_array = []

    #Generation of problems
    for a in range(questions_1):
        base = str(random.randint(1,11))
        height = str(random.randint(1,11))
        question = "A triangle has a base of " + base + " and a height of " + height + ". What is the area of the triangle?"
        questions_array.append(question)
    for b in range(questions_2):
        angle1 = 180
        angle2 = 180
        #Angles cannot be too big or else we don't get a triangle
        while angle1 + angle2 > 179:
            angle1 = random.randint(1,180)
            angle2 = random.randint(1,180)
        angle1 = str(angle1)
        angle2 = str(angle2)
        question = "A triangle has angles " + angle1 + " degrees and " + angle2 + " degrees. What is the degree measure of the third angle?"
        questions_array.append(question)
    for c in range(questions_3):
        side1 = 2
        side2 = 3
        side3 = 5
        #Triangle inequality, so we don't get a degenerate triangle
        while side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            side1 = random.randint(2,6)
            side2 = random.randint(2,6)
            side3 = random.randint(2,6)
        side1 = str(side1)
        side2 = str(side2)
        side3 = str(side3)
        question = "A triangle has side lengths " + side1 + ", " + side2 + ", and " + side3 + ". Is the triangle scalene, isoceles, or equilateral?"
        questions_array.append(question)

    print(questions_array)

    #Redirect to index route
    return render_template("results.html", test = questions_array)
