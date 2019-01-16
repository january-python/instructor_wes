# Set myNumber to 42 . Set myName to your name. Now swap myNumber into myName & vice versa.

my_number = 42
my_name = "Wes Harper"

temp = my_name
my_name = my_number
my_number = temp

# print(my_number)
# print(my_name)

# Print all integer multiples of 5, from 512 to 4096. Afterward, also print how many there were.
# count = 0
# for num in range(515, 4096, 5):
#   print(num)
#   count += 1
# print(count)

# given lowNum , highNum , mult , print multiples of mult from highNum down to lowNum , using a FOR . For (2,9,3) , print 963 (on successive lines).
def flexible_countdown(low_num, high_num, mult):
  for num in range(high_num, low_num, -1):
    if num % mult == 0:
      print(num)

# flexible_countdown(2, 12, 3)

students = [
  {'first_name':  'Michael', 'last_name' : 'Jordan'},
  {'first_name' : 'John', 'last_name' : 'Rosales'},
  {'first_name' : 'Mark', 'last_name' : 'Guillen'},
  {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterate_students(student_list):
  for student in student_list:
    print("first_name - {}, last_name - {}".format(student['first_name'], student['last_name']))
  # iterate through the list
    # for student in students
  # unpack the values in the dictionaries
    # specific_dictionary['first_name']

iterate_students(students)