from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from helpers import users, locations, activities

SCHEMA = "january_ninja_gold"

app = Flask(__name__)
app.secret_key = "as;dlfkjasd;lfkjasdlkfjhawelkjf"

bcrypt = Bcrypt(app)

@app.route('/')
def index():
  if not 'user_id' in session:
    return redirect('/users/new')

  return render_template('index.html',
    locations=locations.all(),
    user=users.get_by_id(session['user_id']),
    activities=activities.get_all_with_user_id(session['user_id'])
  )

@app.route('/process_gold', methods=['POST'])
def process():
  # get the min and max gold amount from the location (form['location_id'])
  # calculate gold amount
    # create a random integer between min and max
  gold_amt = locations.calculate_gold(request.form['location'])
  # Create an activity using location_id, user_id, gold_amt
  activities.create(request.form['location'], session['user_id'], gold_amt)
  # Update the user's current gold_total
  users.update_gold(session['user_id'], gold_amt)
  # Redirect to index page
  return redirect('/')

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

  user_id = users.create(request.form, bcrypt)
  session['user_id'] = user_id
  return redirect('/')

@app.route('/login', methods=['POST'])
def login():
  success, response = users.login(request.form, bcrypt)
  if success:
    session['user_id'] = response
    return redirect('/')
  else:
    flash(response)
  return redirect('/users/new')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/users/new')

if __name__ == "__main__":
  app.run(debug=True)