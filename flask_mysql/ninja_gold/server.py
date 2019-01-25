from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
from helpers import users

SCHEMA = "january_ninja_gold"

app = Flask(__name__)
app.secret_key = "as;dlfkjasd;lfkjasdlkfjhawelkjf"


@app.route('/')
def index():
  db = connectToMySQL(SCHEMA)
  query = "SELECT * FROM locations;"
  location_list = db.query_db(query)
  return render_template('index.html', locations=location_list)

@app.route('/users/new')
def users_new():
  return render_template('users_new.html')

@app.route('/users/create', methods=['POST'])
def users_create():
  errors = users.validate(request.form)

  if errors:
    for error in errors:
      flash(error)
    return redirect('/users/new')

  # hash_pw and create user

  return redirect('/')

@app.route('/login')
def login():
  return redirect('/users/new')

if __name__ == "__main__":
  app.run(debug=True)