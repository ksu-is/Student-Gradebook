import pandas as pd
import numpy as np
from xlsxwriter.utility import xl_rowcol_to_cell


class_list = open('class_list.txt','w+')
grade_list = open('grade_list.txt','w+')
admins = {'bigdaddysang'  : 'abc123','bexley1' : 'abc123',' ' : ' '}



def whatgrade():
    print('Enter the 5 test grades')
    grade1 = input();
    if grade1 == 'x':
        exit()   
    else:
        grade1 = int(grade1)
        grade2 = int(input())
        grade3 = int(input())
        grade4 = int(input())
        grade5 = int(input())

        sum = grade1 + grade2 + grade3 + grade4 + grade5
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
        elif average == 69:
            print()
            print('nice.')
            print()
            print('your grade is a D')
            print()
            print('course average: ', average)
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

def excel():
    df = pd.read_excel('GradebookDatabase.xlsx')
    df.head()
    print(df.head(40))
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

                        (1) Whats my desired grade?
                        (2) Add class scedule
                        (3) View Class scedule
                        (4) Add grades
                        (5) View entered grades
                        (6) Excel
                        (7) EXIT
    ''')

    action = input('''
                        What would you like to do? ''')

    if action == '1':
        whatgrade()
    elif action == '2':
        add_class2()
    elif action == '3':
        seeclasses()
    elif action == '4':
        add_grade2()
    elif action == '5':
        viewgrades()
    elif action == '6':
        excel()
    elif action == '7':
        exitnow()

login()
    

        
