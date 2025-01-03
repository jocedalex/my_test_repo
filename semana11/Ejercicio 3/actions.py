from os import system

class Student:
    def __init__(self, name, section, grades):
        self.name = name
        self.section = section
        self.grades = grades
        self.average = 0

    def __str__(self):
        return f"Name: {self.name} - Section: {self.section} - Average: {self.average}"

    def __repr__(self):
        return f"Name: {self.name} - Section: {self.section} - Average: {self.average}"

def add_student(students):
    system('cls')
    print('Add Student'.center(30, '#'))
    student=Student(input('Name: '), input('Section: '), [])
    students.append(student)

    subjects = ['Spanish', 'English', 'Socials', 'Sciences']
    for i in range(4):

        grade=float(input(f'Enter grade {subjects[i]}: '))
        
        if grade < 0 or grade > 100:
            print('Invalid grade')
            i-=1
            continue
            
        students[-1].grades.append(grade)

    students[-1].average = sum(students[-1].grades)/4

    return students

def show_students(students):
    system('cls')
    print('Student\'s List'.center(30, '#'))
    for item in students:
        print(f"Name: {item.name}", end=' - ')
        print(f"Section: {item.section}")
        print(f"Spanish: {item.grades[0]}")
        print(f"English: {item.grades[1]}")
        print(f"Socials: {item.grades[2]}")
        print(f"Sciences: {item.grades[3]}")
        print(f"Average: {item.average}")
        print()

def show_top3(students):
    system('cls')
    print('Top 3 Students'.center(30, '#'))

    students.sort(key=lambda x: x.average, reverse=True)
    
    print(f"Name: {students[0].name}", end=' - ')   
    print(f"Section: {students[0].section}")
    print(f"Average: {students[0].average}")
    print()

    print(f"Name: {students[1].name}", end=' - ')
    print(f"Section: {students[1].section}")
    print(f"Average: {students[1].average}")
    print()

    print(f"Name: {students[2].name}", end=' - ')
    print(f"Section: {students[2].section}")
    print(f"Average: {students[2].average}")
    print()


def general_average(students):
    system('cls')

    average=0
    for student in students:
        average+=student.average

    print('General Average'.center(30, '#'))
    print(f"General Average: {average/len(students)}")


if __name__ == '__main__':
    print('This file is not designed to be executed on its own.')