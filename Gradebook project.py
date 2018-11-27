class_list = open('class_list.txt','w+')
grade_list = open('grade_list.txt','w+')
admins = {'bigdaddysang'  : 'abc123','bexley1' : 'abc123',' ' : ' '}



def whatgrade():
    print('Enter the 5 test grades')
    mark1 = input();
    if mark1 == 'x':
        exit()   
    else:
        mark1 = int(mark1)
        mark2 = int(input())
        mark3 = int(input())
        mark4 = int(input())
        mark5 = int(input())

        sum = mark1 + mark2 + mark3 + mark4 + mark5
        average = sum/5

        if average >= 90:
            print('your grade is an A')
            print()
            print('Course Average: ', average)
            print()
            main()
        elif average >= 80:
            print('your grade is a B')
            print()
            print('Course Average: ', average)
            print()
            main()
        elif average >= 70:
            print('your grade is a C')
            print()
            print('Course Average: ', average)
            print()
            main()
        elif average >= 60:
            print('your grade is a D')
            print()
            print('Course Average: ', average)
            print()
            main()
        elif average >= 59:
            print('your grade is a F')
            print()
            print('Course Average: ', average)
            print()
            main()
        else:
            ('enter a vaild grade')

def whatGPA():
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


def addclass():
    class1 = input('Enter first class: ')
    class_list.append(class1)
    class2 = input('Enter second class: ')
    class_list.append(class2)
    class3 = input('Enter third class: ')
    class_list.append(class3)
    class4 = input('Enter fourth class: ')
    class_list.append(class4)
    class5 = input('Enter fith class: ')
    class_list.append(class5)
    print(class_list)
    correct_class = input('Are these the correct classes? (1 for yes, 2 for no)')

    if correct_class == '1':
        print('nice')
        main()
    elif correct_class == '2':
        print('try again')
        print()
        addclass()
    else:
        print('invaild choice, try again')



def add_class(classadd):
    class_input = input('Enter class: ')
    count = 0

    while class_input:
        count += 1
        classadd.write(str(count) + ': ' + class_input + '\n')
        class_input = input('Enter class: ')

    return count
def add_class2():
    add_class(class_list)

    class_list.seek(0)
    class_text = class_list.read()

    print()
    print(class_text)
    main()

def add_grade(gradeadd):
    grade_input = input('Enter grade: ')
    count = 0

    while grade_input:
        count += 1
        gradeadd.write(str(count) + ': ' + grade_input + '\n')
        grade_input = input('Enter Grade: ')

    return count

def add_grade2():
    add_grade(grade_list)

    grade_list.seek(0)
    grade_text = grade_list.read()

    print()
    print(grade_text)
    main()
    
def login():
    login = input('User: ')
    password = input('Password: ')

    if login in admins:
        if admins[login] == password:
            print("Welcome " + login,'!')
            print()
            main()
    else:
        invalid_user()

def invalid_user():
    print('Invalid user')
    login()



def seeclasses():
    class_list.seek(0)
    class_text = class_list.read()

    print()
    print(class_text)
    main()
def exitnow():
    print('GOODBYE','\nFRIEND')
    print()
    print('By: Blake Sangster')
def viewgrades():
    grade_list.seek(0)
    grade_text = grade_list.read()

    print()
    print(grade_text)
    main()

def main():
    print('''
                        WELCOME TO THE STUDENT GRADE TARCKER!

                        (1) What's my desired grade?
                        (2) What's my current GPA?
                        (3) Add class scedule
                        (4) View Class scedule
                        (5) View Entered grades
                        (6) Add grades
                        (7) EXIT
    ''')

    action = input('''
                        What would you like to do? ''')

    if action == '1':
        whatgrade()
    elif action == '2':
        whatGPA()
    elif action == '3':
        add_classes2()
    elif action == '4':
        seeclasses()
    elif action == '5':
        viewgrades()
    elif action == '6':
        add_grade2()
    elif action == '7':
        exitnow()

login()
