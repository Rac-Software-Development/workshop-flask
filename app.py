from flask import Flask
from flask import render_template
from flask import request
from models.student import *

app = Flask(__name__)

student_model = Student()

@app.route('/')
def hello_world():
    return render_template('hello_world.html')

@app.route('/save-form', methods=['POST'])
def save_form():
    # Collect form data from the request
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    years_on_school = int(request.form.get('yearsOnSchool', 0))  # Convert to int for years on school
    date_of_birth = request.form.get('dateOfBirth')
    email = request.form.get('email')
    password = request.form.get('password')

    # Save the new student record in the database
    student_model.save_student(first_name, last_name, years_on_school, date_of_birth, email, password)

    return '<p> student created</p>'

@app.route('/students', methods=['GET'])
def list_students():
    students = student_model.get_all_students()

    result = ""
    for student in students:
        result += student['first_name'] + ' ' + student['last_name'] + '<br>'
    return result  # Returning the concatenated string after the loop


if __name__ == '__main__':
    app.run()
