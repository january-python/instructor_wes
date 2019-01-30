from mysqlconnection import connectToMySQL
import re
SCHEMA = "january_ninja_gold"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def validate(form):
  errors = []

  if len(form['first_name']) < 1:
    errors.append("First name must not be empty")
  if len(form['last_name']) < 1:
    errors.append("Last name must not be empty")
  if not EMAIL_REGEX.match(form['email']):
    errors.append("Email must be valid")

  db = connectToMySQL(SCHEMA)
  query = "SELECT id FROM users WHERE email = %(email)s;"
  data = {
    'email': form['email'],
  }
  matching_users = db.query_db(query, data)

  if matching_users:
    errors.append('Email already in use')
  if len(form['password']) < 8:
    errors.append("Password must be at least 8 characters long")

  return errors

def create(form_data, bcrypt):
  pw_hash = bcrypt.generate_password_hash(form_data['password'])

  db = connectToMySQL(SCHEMA)
  query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES(%(first)s, %(last)s, %(email)s, %(password)s, NOW());"
  data = {
    'first': form_data["first_name"],
    'last': form_data["last_name"],
    'email': form_data["email"],
    'password': pw_hash,
  }
  user_id = db.query_db(query, data)
  return user_id

def login(form_data, bcrypt):
  db = connectToMySQL(SCHEMA)
  query = "SELECT id, email, pw_hash FROM users WHERE email=%(email)s;"
  data = {
    'email': form_data['email']
  }
  user_list = db.query_db(query, data)
  if user_list:
    user = user_list[0]
    if bcrypt.check_password_hash(user['pw_hash'], form_data['password']):
      return (True, user['id'])
    else:
      return (False, "Email or password incorrect")
  else:
    return (False, "Email or password incorrect")

def get_by_id(user_id):
  db = connectToMySQL(SCHEMA)
  query = "SELECT * FROM users WHERE id=%(id)s;"
  data = {
    'id': user_id
  }
  users = db.query_db(query, data)
  return users[0]