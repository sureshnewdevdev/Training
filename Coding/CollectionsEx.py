fruits = ["apple", "banana", "cherry", "acrot"]
fruits.append("mango")

for i in range(len(fruits)):
    print(fruits[i])
print("***********************************************************************")
fruits.sort()
print(fruits)

fruits.pop()    
print(len(fruits))
print(fruits)

print("********************************Tuple***************************************")
coordinates = (13.061537955623047, 80.2436516909143)
coList =[]
coList.append(coordinates)
print(coList)
x, y = coordinates
print(x, y)

coordinates2 = (10.061537955623049, 70.2436516909149)
coList.append(coordinates2)
print(coList)

recordEmployee = ("John", 25, "New York")
print(recordEmployee)

print("********************************End Tuple***************************************")

print("********************************Set***************************************")
mySet = {"apple", "banana", "cherry"}
mySet.add("orange")
print(mySet)
mySet.remove("banana")
print(mySet)


A = {1, 2, 3,3}
B = {3, 4, 5}
print("Duplicate values are not allowed in Set ")
print(A.union(B))

print("********************************End Set***************************************")

dd= (101, 'Gopi', 'IT')
ee= (102, 'SALES')

from collections import namedtuple

Employee = namedtuple('Employee', ['id', 'name', 'department'])
emp1 = Employee(101, 'Gopi', 'IT')
emp2 = Employee(10,"Raja","Dep1")
print(emp1.name)
print(emp1._asdict())

print("********************************Named Tuple***************************************")
