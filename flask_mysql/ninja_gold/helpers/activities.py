from mysqlconnection import connectToMySQL
SCHEMA = "january_ninja_gold"

def create(location_id, user_id, gold):
  db = connectToMySQL(SCHEMA)
  query = 'INSERT INTO activities (location_id, user_id, gold, created_at) VALUES(%(location)s, %(user)s, %(gold_amt)s, NOW());'
  data = {
    'location': location_id,
    'user': user_id,
    'gold_amt': gold
  }
  db.query_db(query, data)
  return

def get_all_with_user_id(user_id):
  db = connectToMySQL(SCHEMA)
  query = "SELECT activities.gold AS gold, locations.name AS location, activities.created_at AS date FROM activities JOIN locations ON locations.id = activities.location_id WHERE user_id = %(id)s ORDER BY activities.created_at DESC;"
  data = {
    'id': user_id
  }
  return db.query_db(query, data)