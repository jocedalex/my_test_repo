import csv
from time import sleep
from os import system
from copy import deepcopy

def save_data(students):
    system('cls')
    file_name=input('Enter the file name: ')

    students_data=deepcopy(students)

    with open(f'{file_name}.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file,('name', 'section', 'grades', 'average'))
        writer.writeheader()
        for student in students_data:
            student['grades'] = str(student['grades']).replace('[','').replace(']','')
            writer.writerow(student)

    print('Data saved successfully')
    sleep(3)

def import_data():
    system('cls')
    file_name=input('Enter the file name: ')
    students=[]

    try:
        with open(f'{file_name}.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({
                    'name': row['name'],
                    'section': row['section'],
                    'grades': [float(item) for item in row['grades'].split(',')],
                    'average': float(row['average'])
                })

        return students
    
    except FileNotFoundError:
        print('File not found, unable to export data')


if __name__ == '__main__':
    print('This file is not designed to be executed on its own.')