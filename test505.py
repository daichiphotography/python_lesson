import PySimpleGUI as sg 

savename = sg.popup_get_file('Choose the name.', default_path = 'test.txt',save_as = True)
print(savename)