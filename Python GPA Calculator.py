 #GPA Calc

#Lists 
classes= []
grades = []

#Collects the data of Class names and Grades in Letter Form
def collect():
    i = 0
    while (i <= 5):
        className = input("Enter Class Name: ")
        classes.append(className)
        i = i +1


    print(classes)
    y = 0
    while (y <=5):
        grade = input("Enter Your Grade For Each Class Listed in Order (Letter Form): ")
        grade = grade.upper()
        grades.append(grade)
        y = y + 1
    calculate()

def calculate():
    total= 0
    for element in grades:
        if element == "A+":
            total = total + 4.0
        elif element == "A":
            total = total + 4.0
        elif element == "A-":
            total = total + 3.7
        elif element == "B+":
            total = total + 3.3
        elif element == "B":
            total = total + 3.0
        elif element == "B-":
            total = total + 2.7
        elif element == "C+":
            total = total + 2.3
        elif element == "C":
            total = total + 2.0
        elif element == "C-":
            total = total + 1.7
        elif element == "D":
            total = total + 1.0
    gpa = total / 6
    print(gpa)


collect()
