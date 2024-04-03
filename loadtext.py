import PySimpleGUI as sg 
from pathlib import Path

import chardet

sg.theme('DarkBrown3')

layout = [[sg.B('Open the file', k ='btn1'), sg.T(k = 'txt1')],
          [sg.ML(k='txt2', font =(None,14), size =(80,15))]]

win = sg.Window('Reading a text file', layout) #Shows the title and layout

def loadtext():
    global loadname, enc 
    loadname = sg.popup_get_file('Please choose a file ') #With popup, it shows input box to select a file 
    if not loadname: # if there is not file, nothing happens 
        return
    with open (loadname, 'rb')as f: #read a file as a binary file 
        b = f.read() # read the file
        
    enc = chardet.detect(b)['encoding'] #with library, it detects binary file  
    p = Path(loadname) # Finding a path of the file 
    txt = p.read_text(encoding = enc) # read the selected file 
    win['txt1'].update(loadname) 
    win['txt2'].update(txt)
    
while True:
    e,v = win.read()
    if e == 'btn1':
        loadtext()
    if e == None:
        break
win.close()