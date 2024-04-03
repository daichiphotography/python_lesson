import datetime 
import PySimpleGUI as sg 

layout = [[sg.T(font =('Arial', 40), k = 'txt',size =(20,1), justification = 'center')]]
win = sg.Window('Clock test', layout, size = (320, 280), keep_on_top = True)

c = 0

while True:
    e,v = win.read(timeout= 500)
    c +=1 
    win['txt'].update(f'{c}')
    if e==None:
        break
    
win.close()