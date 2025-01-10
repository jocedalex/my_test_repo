import PySimpleGUI as ui
from data import import_data
from utilities import add_category,add_movement

#Main Screen
def main():
    headings=['Title','Type','Category','Amount']
    data=import_data('movements')
    categories=import_data('categories')
    

    layout=[[ui.Table(values=data, headings=headings, auto_size_columns=False, display_row_numbers=True, num_rows=10, alternating_row_color='lightblue', key='-TABLE-')],
            [ui.Button("Add Income",key="IN",size=10), ui.Button("Add Spent",key="OUT",size=10)],
            [ui.Button("Add Category",key="CAT",size=23)]]


    window = ui.Window("Your Financial Friend", layout,background_color="grey")
    
    while True:
        event, values = window.read()
        
        if event == ui.WIN_CLOSED:
            break

        elif event=="IN":
            data=income_creation(categories,data)
            window["-TABLE-"].update(values=data)

        elif event=="OUT":
            data=spent_creation(categories,data)
            window["-TABLE-"].update(values=data)

        elif event=="CAT":
            categories=category_creation(categories)

#Category Screen
def category_creation(categories):
    layout=[[ui.Text("Category: "),ui.Input(key="category_field")],
            [ui.Button("Save"),ui.Button('Cancel')]]


    window = ui.Window("Add a new category", layout)
    while True:
        event, values = window.read()
        
        if event == ui.WIN_CLOSED or event == "Cancel":
            break

        elif event=='Save':
            categories=add_category(categories,values['category_field'])
            break
        
    window.close()
    return categories
            
#Outcomes Screen
def spent_creation(categories,data):
    if len(categories)>0:
        layout=[[ui.Text("Title"),ui.Input(key='title_field')],
                [ui.Text("Category"),ui.OptionMenu(categories,default_value=categories[0],key='category_field')],
                [ui.Text("Amount"),ui.Input(key='amount_field')],
                [ui.Button('Save'),ui.Button('Cancel')]]
    else:
        layout=[[ui.Text("Unable to add spents, please create at least 1 category")]]


    window = ui.Window("Add a new spent", layout)
    while True:
        event, values = window.read()
        
        if event == ui.WIN_CLOSED or event=='Cancel':
            break

        elif event=='Save':
            new_data=[values['title_field'],'Out',values['category_field'],values['amount_field']]
            data= add_movement(data,new_data)
            break

    window.close()
    return data

#Incomes Screen
def income_creation(categories,data):
    if len(categories)>0:
        layout=[[ui.Text("Title"),ui.Input(key='title_field')],
                [ui.Text("Category"),ui.OptionMenu(categories,default_value=categories[0],key='category_field')],
                [ui.Text("Amount"),ui.Input(key='amount_field')],
                [ui.Button('Save'),ui.Button('Cancel')]]
    else:
        layout=[[ui.Text("Unable to add incomes, please create at least 1 category")]]


    window = ui.Window("Add a new income", layout)
    while True:
        event, values = window.read()
        
        if event == ui.WIN_CLOSED or event=='Cancel':
            break

        elif event=='Save':
            new_data=[values['title_field'],'In',values['category_field'],values['amount_field']]
            data= add_movement(data,new_data)
            break

    window.close()
    return data



if __name__ == '__main__':
    main()