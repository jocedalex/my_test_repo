import csv

def save_data(data, file_name):

    if file_name=='movements':
        with open(f'my_test_repo/semana17/Mod1 Final Project/{file_name}.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file,('Title', 'Type', 'Category', 'Amount'))
            writer.writeheader()

            for item in data:
                writer.writerow({'Title': item[0], 'Type': item[1], 'Category': item[2], 'Amount': item[3]})
                       

        print('Data saved successfully')

    elif file_name=='categories':
        with open(f'my_test_repo/semana17/Mod1 Final Project/{file_name}.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file,('Name',))
            writer.writeheader()

            for item in data:
                writer.writerow({'Name': item})
            

        print('Data saved successfully')

def import_data(file_name):
    
    data=[]

    try:
        with open(f'my_test_repo/semana17/Mod1 Final Project/{file_name}.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if file_name=='movements':
                    data.append([row['Title'], row['Type'], row['Category'], row['Amount']])
                elif file_name=='categories':
                    data.append(row['Name'])

        return data
        
    except FileNotFoundError as e:
        with open(f'my_test_repo/semana17/Mod1 Final Project/{file_name}.csv', mode='w', newline='') as file:
            if file_name=='movements':
                writer = csv.DictWriter(file,('Title', 'Type', 'Category', 'Amount'))
                writer.writeheader()

            elif file_name == 'categories':
                writer = csv.DictWriter(file,('Name',))
                writer.writeheader()

        return data



if __name__ == '__main__':
    print('This file is not designed to be executed on its own.')