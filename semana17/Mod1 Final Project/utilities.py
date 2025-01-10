from data import save_data
import PySimpleGUI as ui

def add_movement(data,new_data):
    try:

        new_data[3]=int(new_data[3])

        print('Movement added',new_data)

        data.append(new_data)
        
        save_data(data,'movements')

        return data
    
    except ValueError:
        layout=[[ui.Text("Unable to add data, you gave a non-numeric amount!")],
                [ui.Button("Ok")]]


        window = ui.Window("Error!", layout)
        while True:
            event, values = window.read()
            
            if event == ui.WIN_CLOSED or event=="Ok":
                break

        window.close()
        return data
    

def add_category(categories,category):
    
    print('Category added',category)
    categories.append(category)

    save_data(categories,'categories')

    return categories

if __name__ == '__main__':
    print('This file is not designed to be executed on its own.')