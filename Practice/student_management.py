x = input("Enter 1st student name: ")
y = input("Enter 2nd student name: ")
z = input("Enter 3rd student name: ")

students = {}

def total_marks():
    total = m1 + m2 + m3
    return total

def avearge_marks():
    average = total_marks() / 3
    return int(average)

def grade():
    if avearge_marks() >= 90:
        return "A"
    elif avearge_marks() >= 80:
        return "B"
    elif avearge_marks() >= 70:
        return "C"
    elif avearge_marks() >= 60:
        return "D"
    elif avearge_marks() >= 50:
        return "E"
    else:
        return "F"

grade_order = {'A': 0,'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
def grade_key(item):
    return grade_order[item[1][5]]

for student in [x, y, z]:
    m1 = int(input(f"Enter marks 1 for {student}: "))
    m2 = int(input(f"Enter marks 2 for {student}: "))
    m3 = int(input(f"Enter marks 3 for {student}: "))
    students[student]= [m1, m2, m3, total_marks(), avearge_marks(), grade()]

# compute sorted list after the dictionary has been filled
sorted_by_grade = sorted(students.items(), key=grade_key)

print("Full student data:", students)
print("Students sorted by grade:")
for name, data in sorted_by_grade:
    # data is the list [m1,m2,m3,total,avg,grade]
    print(f"{name}: grade {data[5]}, average {data[4]}")