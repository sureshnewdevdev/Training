students = []  # (name, age, marks)
print("Enter students (type -1 as choice to stop).")
choice = 1
while choice != -1:
    name = input("Name (-1 to stop): ").strip()
     
    try:
        age = int(input("Age: ").strip())
        marks = float(input("Marks: ").strip())
    except ValueError:
        print("Invalid number. Try again.\n")
        continue
    students.append((name, age, marks))
    print("Added.\n")
    choice = int(input("Choice (-1 to stop): ").strip())
    

if students:
    max_marks = max(students, key=lambda s: s[2])[2]
    min_marks = min(students, key=lambda s: s[2])[2]
    toppers = [s for s in students if s[2] == max_marks]
    lowest  = [s for s in students if s[2] == min_marks]

    print("\n=== Results ===")
    print("Max marks:", max_marks, "| Students:", toppers)
    print("Min marks:", min_marks, "| Students:", lowest)
else:
    print("No students entered.")
