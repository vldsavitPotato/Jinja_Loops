from flask import Flask, render_template

app = Flask(__name__)

st_list = ["Alex D", 
           "Nick A",
           "Dave B"]

subjects = {'Math': 5, 'History': 4, 'Informatics': 4}

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
