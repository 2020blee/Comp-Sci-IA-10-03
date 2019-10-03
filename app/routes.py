import os
from app import app
from flask import render_template, request, redirect

import math
import random

class Subtopics():
    def __init__(self, q_1, q_2, q_3):
        self.q_1 = q_1
        self.q_2 = q_2
        self.q_3 = q_3

    def design_the_questions(num_of_problems):
        print("These three frequencies must add up to exactly 100")
        #Takes in user input based on how frequent they want each type of question to be:
        freq_q_1 = int(input("How frequent to do you want questions about " + self.q_1 + " to be in terms of percentage?\n"))
        if self.q_2 == "-":
            freq_q_2 == 0
        else:
            freq_q_2 = int(input("How frequent to do you want questions about angles to be in terms of percentage?\n"))
        if self.q_3 == "-":
            freq_q_3 == 0
        else:
            freq_q_3 = int(input("How frequent to do you want questions about classfying triangles to be in terms of percentage?\n"))
        #Noting possible errors that could occur that would give back an undesired output
        if freq_q_1 + freq_q_2 + freq_q_3 != 100:
            print("Error: The three frequencies must add up to exactly 100")
            geometry_subtopic()
        if freq_q_1 < 0 or freq_q_2 < 0 or freq_q_3 < 0:
            print("Error: the percentage cannot be negative")
            geometry_subtopic()
        #Takes in user input
        questions_per_test = int(input("How many questions do you wish per test?\n"))
        tests_number = int(input("How many tests do you wish to be generated?\n"))
        #I am using floors to underestimate the number of questions that we create
        questions_1 = math.floor(freq_q_1 * questions_per_test/100)
        questions_2 = math.floor(freq_q_2 * questions_per_test/100)
        questions_3 = math.floor(freq_q_3 * questions_per_test/100)
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



circles = Subtopics("area", "-", "-")



#Hash to store all the tests created
tests_hash = {}

#Hash that stores the problems created
problems_hash = {}

#This function is the start menu of the program
def start():
    directory = int(input("Welcome to Math Test Creator Beta version. What do you want to do? 1. Create a test. 2. View the history of created tests. 3. How to use this program. 4. Quit\n"))
    if directory == 1:
        select_a_topic()
    elif directory == 2:
        print("History of tests not available yet")
        quit()
    elif directory == 3:
        print("Directions not available yet")
        quit()
    elif directory == 4:
        print("Quitting")
        quit()
    else:
        print("Invalid input")
        start()

#This function allows the user to select their topic
def select_a_topic():
    #Only option 2 works for now; others can be coded later
    topic_picker = int(input("Select a topic: 1. Proportions. 2. Geometry. 3. Systems of equations. 4. Transformations.\n"))
    if topic_picker == 2:
        geometry_subtopic()
    else:
        print("Invalid input")
        select_a_topic()

#This function allows the user to select their subtopic and the frequency of their questions
def geometry_subtopic():
    #Only subtopic 3 works for now; others can be coded later
    subtopic_picker = int(input("Select a subtopic: 1. Circles. 2. Squares. 3. Triangles.\n"))

    if subtopic_picker == 1:
        print("Only area problems are available")
        #Takes in user input
        questions_per_test = int(input("How many questions do you wish per test?\n"))
        tests_number = int(input("How many tests do you wish to be generated?\n"))
        questions_1 = questions_per_test
        create_circles_tests(tests_number, questions_1)


    if subtopic_picker == 2:
        print("Only area problems are available")
        #Takes in user input
        questions_per_test = int(input("How many questions do you wish per test?\n"))
        tests_number = int(input("How many tests do you wish to be generated?\n"))
        questions_1 = questions_per_test
        create_squares_tests(tests_number, questions_1)


    if subtopic_picker == 3:
        print("These three frequencies must add up to exactly 100")
        #Takes in user input based on how frequent they want each type of question to be:
        freq_q_1 = int(input("How frequent to do you want questions about area to be in terms of percentage?\n"))
        freq_q_2 = int(input("How frequent to do you want questions about angles to be in terms of percentage?\n"))
        freq_q_3 = int(input("How frequent to do you want questions about classfying triangles to be in terms of percentage?\n"))
        #Noting possible errors that could occur that would give back an undesired output
        if freq_q_1 + freq_q_2 + freq_q_3 != 100:
            print("Error: The three frequencies must add up to exactly 100")
            geometry_subtopic()
        if freq_q_1 < 0 or freq_q_2 < 0 or freq_q_3 < 0:
            print("Error: the percentage cannot be negative")
            geometry_subtopic()
        #Takes in user input
        questions_per_test = int(input("How many questions do you wish per test?\n"))
        tests_number = int(input("How many tests do you wish to be generated?\n"))
        #I am using floors to underestimate the number of questions that we create
        questions_1 = math.floor(freq_q_1 * questions_per_test/100)
        questions_2 = math.floor(freq_q_2 * questions_per_test/100)
        questions_3 = math.floor(freq_q_3 * questions_per_test/100)
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
        create_triangles_tests(tests_number, questions_1, questions_2, questions_3)



#This for loop creates the number of tests desired
def create_circles_tests(tests_number, questions_1):
    for x in range(tests_number):
        create_circles_problems(questions_1)
        problems_hash.clear()

#This function takes in the frequencies of each question and creates problems based off of that
def create_circles_problems(questions_1):
    questions_array = []

    #Generation of problems
    for a in range(questions_1):
        random_integer = random.randint(1,3)
        if random_integer == 1:
            length = str(random.randint(1,13))
            question = "A circle has a radius of " + length + ". What is the area of the circle?"
        if random_integer == 2:
            length = str(2 * random.randint(1,13))
            question = "A circle has a diameter of " + length + ". What is the area of the circle?"
        if random_integer == 3:
            length = str((random.randint(1,13))**2)
            question = "A circle has an area of " + length + "π. What is the radius of the circle?"
        questions_array.append(question)

    #https://stackoverflow.com/questions/473973/shuffle-an-array-with-python-randomize-array-item-order-with-python - This helped me with shuffling the elements in an array
    #Randomly orders the questions
    random.shuffle(questions_array)

    #Puts the questions into a hash
    for l in range(len(questions_array)):
        problems_hash[l] = questions_array[l]

    #I used this site to help me solve a key error problem in my code: https://stackoverflow.com/questions/23297569/python-key-error-0-cant-find-dict-error-in-code
    tests_hash[str(len(tests_hash) + 1)] = problems_hash

    print(tests_hash)
    print(problems_hash)




#This for loop creates the number of tests desired
def create_squares_tests(tests_number, questions_1):
    for x in range(tests_number):
        create_squares_problems(questions_1)
        problems_hash.clear()

#This function takes in the frequencies of each question and creates problems based off of that
def create_squares_problems(questions_1):
    questions_array = []

    #Generation of problems
    for a in range(questions_1):
        length = str(random.randint(1,13))
        question = "A square has a side length of " + length + ". What is the area of the square?"
        questions_array.append(question)

    #https://stackoverflow.com/questions/473973/shuffle-an-array-with-python-randomize-array-item-order-with-python - This helped me with shuffling the elements in an array
    #Randomly orders the questions
    random.shuffle(questions_array)

    #Puts the questions into a hash
    for l in range(len(questions_array)):
        problems_hash[l] = questions_array[l]

    #I used this site to help me solve a key error problem in my code: https://stackoverflow.com/questions/23297569/python-key-error-0-cant-find-dict-error-in-code
    tests_hash[str(len(tests_hash) + 1)] = problems_hash

    print(tests_hash)
    print(problems_hash)





#This for loop creates the number of tests desired
def create_triangles_tests(tests_number, questions_1, questions_2, questions_3):
    for x in range(tests_number):
        create_triangles_problems(questions_1, questions_2, questions_3)
        problems_hash.clear()

#This function takes in the frequencies of each question and creates problems based off of that
def create_triangles_problems(questions_1, questions_2, questions_3):
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

    #https://stackoverflow.com/questions/473973/shuffle-an-array-with-python-randomize-array-item-order-with-python - This helped me with shuffling the elements in an array
    #Randomly orders the questions
    random.shuffle(questions_array)

    #Puts the questions into a hash
    for l in range(len(questions_array)):
        problems_hash[l+1] = questions_array[l]

    #I used this site to help me solve a key error problem in my code: https://stackoverflow.com/questions/23297569/python-key-error-0-cant-find-dict-error-in-code
    tests_hash[str(len(tests_hash) + 1)] = problems_hash

    if len(tests_hash) > 10:
        dequeue.tests_hash

    print(tests_hash)
    print(problems_hash)

    #The problems_hash is like a dinner plate. We use it to put stuff on it and then we clean it off. However, the tests hash permenately stores anything necessary without having to clean it

start()

# INDEX

@app.route('/')
@app.route('/index')

def index():
    #Connect to the mongo events database that you made
    events = mongo.db.events
    #Query all Events and stored them as myquery
    myquery = list(events.find({}))
    print("#############" *4)
    print(myquery)
    return render_template('index.html', myquery = myquery)


# CONNECT TO DB, ADD DATA

@app.route('/add')
