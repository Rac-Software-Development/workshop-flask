from flask import Flask
from flask import render_template
from flask import request
from databases.database import Database

app = Flask(__name__)

db = Database('databases/database.db')
db.setup_student_table()

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
    first_name = request.form['firstName']
    print(request.form)
    return first_name


if __name__ == '__main__':
    app.run()
