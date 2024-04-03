import PySimpleGUI as sg 
from PIL import Image
import io 

sg.theme('DarkBrown3')

layout =[[sg.B('Open a file ',k ='btn1'),sg.T(k='txt')],
         [sg.Im(k='img')]]

win = sg.Window('Display the file ', layout, size =(320,380))

def loadimage():
    loadname = sg.popup_get_file('Choose the image file ')
    if not loadname:
        return
    try:
        img = Image.open(loadname)
        img.thumbnail((300,300))
        bio = io.BytesIO()
        img.save(bio, format = 'PNG')
        win['img'].update(data=bio.getvalue())
        win['txt'].update(loadname)
    except:
        win['img'].update()
        win['txt'].update('Failed')
        
        
while True:
    e,v = win.read()
    if e == 'btn1':
        loadimage()
        
    if e == None:
        break
win.close()