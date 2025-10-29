# Simple lambda function that adds 10 to the given number
add_10 = lambda x, y: x + y

print(add_10(5, 10))  # Output: 15
print(add_10(50, 10))  # Output: 60
print(add_10(500, 10))  # Output: 510

print("*****************Sorted list**********************")
# Sorting a list of tuples based on the second item (age)
people = [("zlice", 30), ("dob", 25), ("aharlie", 35)]
sorted_people = sorted(people, key=lambda ff: ff[0])

print(sorted_people)  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

print("*****************Filter even numbers**********************")

# List of employees with their names and salaries
employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 60000},
    {"name": "Charlie", "salary": 40000},
    {"name": "Charlie", "salary": 42000},
    {"name": "Aronold", "salary": 42000}


]

# Sorting by salary, and then by name alphabetically
sorted_employees = sorted(employees, key=lambda x: (x["salary"], x["name"]))

print(sorted_employees)
# Output: [{'name': 'Charlie', 'salary': 40000}, {'name': 'Alice', 'salary': 50000}, {'name': 'Bob', 'salary': 60000}]

print("*****************Map Square Function**********************")

from functools import reduce

# Using reduce() to multiply all elements in the list
numbers = [1, 2, 3, 4]

def printValues(x,y):
    print(x,y)
   
    return x+y

product = reduce(lambda x, iterationValue: printValues(x , iterationValue), numbers)
print("*****************Reduce Function**********************")
print(product)  