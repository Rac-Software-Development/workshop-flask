# workshop-flask

- Iets over het doel van de workshop
1. Student model
2. Student controller
3. POST van formulier naar DB
4. Show all students

## Opdracht 1 - Maak een student model

Alle dingen die jij je kan voorstellen als database tabel moet in code omgezet moeten worden als model object. 
Alle gegevens die in het formulier opgenomen zijn bij hello_world.html zouden mooi opgeslagen kunnen worden in een student tabel.
Dit tabel staat al netjes in de database.db, dus dat hoef jij niet meer te doen. Het model maken moet nog wel gemaakt worden.

Kijk naar het formulier en wat er opgeslagen wordt:
```html
    <form method="post" action="/save-form">
        <label for="firstname-input">voornaam</label>
        <input id="firstname-input" name='firstName' type="text">
        <label for="lastname-input">achternaam</label>
        <input id="lastname-input" name="lastName" type="text">
        <label for="yearsOnSchool-input">Jaar op school</label>
        <input id="yearsOnSchool-input" name="yearsOnSchool" type="number">
        <label for="dateOfBirth-input">Geboortedatum</label>
        <input id="dateOfBirth-input" name="dateOfBirth" type="date">
        <label for="email-input">email</label>
        <input id="email-input" name="email" type="email">
        <label for="password-input">Wachtwoord</label>
        <input id="password-input" name="password" type="password">
        <input type="submit">
    </form>
```
We willen dus de volgende informatie kunnen opslaan in de database zodra de submit button wordt aangeklikt:
* first name
* last name
* years on school
* date of birth
* email
* password

Hiervoor gaan we nu een model aanmaken in een map genaamd models:
![img.png](img.png)

In de student.py file maken we een class aan genaamd Student met een init die de database initializeerd en de databaase 
tabel aanmaakt voor Student. De SQL code voor het maken van de tabel staat al in database.py.
```python
class Student:
    def __init__(self):
        database = Database('./databases/database.db')
        database.setup_student_table()
```

Het model neemt ook alle database logica op zich, wat betekent dat de database queries hier ook worden geplaatst. We
willen studenten kunnen opslaan en kunnen weergeven, dus daar hebben we ook functies voor nodig in de student.py.

```python
    def save_student(self, first_name, last_name, years_on_school, date_of_birth, email, password):
        database = Database('./databases/database.db')
        cursor, con = database.connect_db()

        cursor.execute("INSERT INTO students (first_name, last_name, years_on_school, dob, email, password) VALUES (?, ?, ?, ?, ?, ?)",
        (first_name, last_name, years_on_school, date_of_birth, email, password))
        con.commit()
        con.close()

    def get_all_students(self):
        database = Database('./databases/database.db')
        cursor, con = database.connect_db()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return students
```
## Opdracht 2 - Opslaan na invullen van formulier
De controller roept de data op om er vervolgens iets mee te doen om weer te geven. In deze workshop functioneert app.py
als de controller. In grotere applicaties zou je dit eigenlijk willen splitten. Dus een aparte controller voor student data, 
een aparte controller voor cijfer data, een aparte controller voor docenten data, enz.

We hebben al een bestaande POST request in die nadat de submit knop is geklikt de voornaam print die zojuist is ingevoerd.
Dit is leuk en aardig, maar we willen eigenlijk dat die data wordt opgeslagen in de database. Hiervoor moet de save_form
methode worden aangepast. Dit doen we door het studenten model aan te roepen:
```python
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

if __name__ == '__main__':
    app.run()
```
Het verschil met de oude app.py is dat we nu het student model aanroepen bovenaan het bestand, en nadat we alle 
informatie hebben opgeslagen in een variabel gebruiken om de save_student functie aan te roepen in het student_model.

## Opdracht 3 - Alle studenten weergeven
Tot slot willen we de student (en alle studenten die ervoor of erna zijn toegevoegd) weergeven. Hiervoor gaan we een
we een nieuwe Route aanmaken. Dit keer gebruiken we een GET-methode omdat we iets van de database willen krijgen, en niet
op willen sturen (POST).

Voeg de volgende functie toe aan app.py:
```python
@app.route('/students', methods=['GET'])
def list_students():
    students = student_model.get_all_students()

    result = ""
    for student in students:
        result += student['first_name'] + ' ' + student['last_name'] + '<br>'
    return result  # Returning the concatenated string after the loop
```

Ga nu naar localhost:5000/students en als het goed is moet je alle studenten kunnen zien die je hebt ingevuld met het
formulier




