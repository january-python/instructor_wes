from mysqlconnection import connectToMySQL
import random
SCHEMA = "january_ninja_gold"

def all():
  db = connectToMySQL(SCHEMA)
  query = "SELECT * FROM locations;"
  location_list = db.query_db(query)
  return location_list

def calculate_gold(location_id):
  db = connectToMySQL(SCHEMA)
  query = "SELECT min_gold, max_gold FROM locations WHERE id=%(id)s;"
  data = {
    'id': location_id
  }
  location_list = db.query_db(query, data)
  location = location_list[0]
  curr_gold = random.randint(location['min_gold'], location['max_gold'])
  return curr_gold