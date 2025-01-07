import actions as ac
from data import save_data, import_data


def main_menu():
    students=[]

    while True:
        
        print('Main Menu'.center(30, '#'))
        print('1. Add Student')
        print('2. Show all students')
        print('3. Show student\'s top 3')
        print('4. Show general average')
        print('5. Save Data')
        print('6. Import Data')
        print('7. Exit')

        try:
            option = int(input('Choose an option: '))

            if option == 1:
                students=ac.add_student(students)

            elif option == 2:
                ac.show_students(students)

            elif option == 3:
                ac.show_top3(students)

            elif option == 4:
                ac.general_average(students)

            elif option == 5:
                save_data(students)

            elif option == 6:
                students=import_data()

            elif option == 7:
                break

        except ValueError as e:
            print('invalid Option',e)


if __name__ == '__main__':
    print('This file is not designed to be executed on its own.')