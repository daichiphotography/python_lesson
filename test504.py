import PySimpleGUI as sg 

loadname = sg.popup_get_file('Choose the file name.')
print(loadname)