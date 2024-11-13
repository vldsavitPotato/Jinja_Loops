from flask import Flask, render_template

app = Flask(__name__)


subjects = {'Math': 5, 'History': 4, 'Informatics': 4}

st_list = [("Ivanov Ivan",
            {'Mathematics': 5, 'History': 4, 'Computer Science': 4}),
           ('Petrov Peter',
            {'Mathematics': 3, 'History': 5, 'Computer Science': 4}),
           ('Yegor Sidorov',
            {'Mathematics': 5, 'History': 5, 'Computer Science': 5}),
           ('Progulov Vasya', {})]

movies = [({'The Godfather': 1}),
          ({'The Shawshank Redemption': 2}),
          ({'Schindlers List': 3}),
          ({'Raging Bull': 4}),
          ({'Casablanca': 5}),
          ({'Citizen Kane': 6}),
          ({'Gone with the Wind': 7}),
          ({'The Wizard of Oz': 8}),
          ({'One Flew Over the Cuckoos Nest': 9}),
          ({'Lawrence of Arabia': 10})]

@app.route("/")
def index():
  return render_template('index.html',
                         name='Itgenik',
                         title='Engine Jinja',
                         count=10)

@app.route("/students")
def students():
  return render_template('students.html',
                        st_list = st_list,
                        subjects = subjects)

@app.route("/workshop")
def students():
  return render_template('students.html',
                        movies = movies)
