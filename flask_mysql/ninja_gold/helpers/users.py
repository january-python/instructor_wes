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