student_list = []

class AutoIncrementIDGenerator:
    def __init__(self, prefix='SID-'):
        self.prefix = prefix
        self.counter = len(student_list)

    def generate_next_id(self):
        self.counter += 1
        unique_id = f'{self.prefix}{self.counter:03d}'
        return unique_id  
    
class Student:  
    def __init__(self, firstname, lastname, age, major) :
        self.id = AutoIncrementIDGenerator().generate_next_id()
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.major = major

def main():
    print('\n')
    print('==========================')
    print('||  Student Management  ||')
    print('==========================')

    print('1: To View Student\'s List')
    print('2: To Add Student To The List')
    print('3: To Search Student From The List')
    print('4: To Remove Student From The List')
    print('5: Exit')

    input_num = input('Please Select An Above Option : ')
    option_number = 0
    try:
        option_number = int(input_num)
    except ValueError:
        print('\nIncorrect Input!')
        main()

    if option_number == 1 :
        view_student()
        main()
    elif option_number == 2 : 
        add_student()
    elif option_number == 3 : 
        if len(student_list) == 0 :
            print('\n======================')
            print('No Student Registered!')
            main()
        search_student_by_id(input('Enter Student\'s ID = '))
    elif option_number == 4 : 
        if len(student_list) == 0 :
            print('\n======================')
            print('No Student Registered!')
            main()
        delete_student(input('Enter Student\'s ID = '))
    elif option_number == 5 : 
        print('\nProgram Exited!\n')
        exit()
    else:
        print('\nIncorrect Input!')
        main()

def add_student():
    firstname = input('Input Firstname : ')
    lastname = input('Input Lastname : ')
    age = input('Input Age : ')
    major = input('Input Major : ')
    student_list.append(Student(firstname,lastname, age, major))
    view_student()

def find_student(id):
    for student in student_list:
        if student.id == id :
            return student
    return None
        
def search_student_by_id(id) :

    student = find_student(id)
    if student :
        print(f'\n====== { 1} ======')
        print(f'ID = {student.id}')
        print(f'Firstname = {student.firstname}')
        print(f'Lastname = {student.lastname}')
        print(f'Age = {student.age}')
        print(f'Major = {student.major}')
    else :
        print('\n==================')
        print('Student Not Found!')
    main()

def delete_student(id):
    student = find_student(id)
    if student : 
        student_list.remove(student)
        print('Student Removed!')
    else :
        print('\n==================')
        print('Student Not Found!')
    main()

def view_student():
    if len(student_list) == 0 :
        print('\n======================')
        print('No Student Registered!')
        return
    
    print('\n======== <<< List Of Students >>> ========')

    for index,student in enumerate(student_list):
        print('\n')
        print(f'====== {index + 1} ======')
        print(f'ID = {student.id}')
        print(f'Firstname = {student.firstname}')
        print(f'Lastname = {student.lastname}')
        print(f'Age = {student.age}')
        print(f'Major = {student.major}')
    main()
        
main()
