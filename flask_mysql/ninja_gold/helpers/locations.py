from mysqlconnection import connectToMySQL
SCHEMA = "january_ninja_gold"

def all():
  db = connectToMySQL(SCHEMA)
  query = "SELECT * FROM locations;"
  location_list = db.query_db(query)
  return location_list