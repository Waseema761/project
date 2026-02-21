from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# connect to MySQL container
db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root123",
    database="hospital"
)

cursor = db.cursor()

# home page
@app.route('/')
def home():
    return render_template("index.html")

# add patient
@app.route('/add', methods=['POST'])
def add_patient():
    name = request.form['name']
    age = request.form['age']

    cursor.execute("INSERT INTO patients (name, age) VALUES (%s,%s)", (name,age))
    db.commit()

    return "Patient Added Successfully"

# view patients
@app.route('/patients')
def patients():
    cursor.execute("SELECT * FROM patients")
    data = cursor.fetchall()
    return str(data)

app.run(host="0.0.0.0", port=5000)
