import PySimpleGUI as sg 

layout = [[sg.Input('NAME',key ='in')],
          [sg.Button('Run',key = 'btn')],
          [sg.Text(key = "txt")]]
window = sg.Window('Hello world test',layout)

def execute():
    txt = 'Hello, ' + values['in'] + ' and Bye lol '
    window['txt'].update(txt)
    
    
while True:
    event, values = window.read()
    if event == 'btn':
        execute()
    if event == None:
        break
window.close()