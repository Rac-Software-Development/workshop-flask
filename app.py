from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from models.student import *

app = Flask(__name__)

student_model = Student('./databases/database.db')


@app.route('/')
def hello_world():
    first_name = request.args.get('firstName', '')
    last_name = request.args.get('lastName', '')
    years_on_school = request.args.get('yearsOnSchool', '')
    date_of_birth = request.args.get('dateOfBirth', '')
    email = request.args.get('email', '')
    password = request.args.get('password', '')
    print(first_name)
    print(last_name)
    print(years_on_school)
    print(date_of_birth)
    print(email)
    print(password)
    return render_template('hello_world.html')


@app.route('/save-form', methods=['POST'])
def save_form():
    # Collect form data from the request
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    years_on_school = request.form['yearsOnSchool']
    date_of_birth = request.form['dateOfBirth']
    email = request.form['email']
    password = request.form['password']

    # Save the new student record in the database and get the new ID
    student_id = student_model.save_student(first_name, last_name, years_on_school, date_of_birth, email, password)

    # Redirect to the student detail page
    return redirect(f'/students/{student_id}')


@app.route('/students', methods=['GET'])
def list_students():
    students = student_model.get_all_students()

    result = ""
    for student in students:
        result += f'<b>Naam:</b> {student['first_name']} {student['last_name']} - <a href="/students/{student['id']}"> Details </a><br>'
    return result

@app.route('/students/<student_id>', methods=['GET'])
def show_student(student_id):
    # Fetch the details of the student
    student = student_model.get_single_student(student_id)

    # Build an HTML string with the student details
    result = f"""
    <h1>Student Details</h1>
    <p>
        ID: {student['id']}<br>
        Voornaam: {student['first_name']}<br>
        Achternaam: {student['last_name']}<br>
        Schooljaar: {student['years_on_school']}<br>
        Geboortedatum: {student['date_of_birth']}<br>
        Email: {student['email']}
    </p>
    <a href="/">Terug naar formulier</a><br>
    <a href="/students">Studenten overzicht</a><br>
    """
    return result


if __name__ == '__main__':
    app.run()
