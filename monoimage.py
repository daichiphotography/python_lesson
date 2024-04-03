import PySimpleGUI as sg 
from PIL import Image 
import io

sg.theme('Dark Brown3')

layout = [[sg.B('Open a file ',k = 'btn1'),sg.T(k = 'txt')],
          [sg.B('Save a file',k='btn2')],
          [sg.Im(k='img')]]

win = sg.Window('Change to Monochrome',layout, size=(820,800))

def loadimage():
    global img
    loadname = sg.popup_get_file('Choose an image')
    if not loadname:
        return
    try:
        img = Image.open(loadname).convert('L')
        img2 = img.copy()
        img2.thumbnail((700,700))
        bio = io.BytesIO()
        img2.save(bio,format = 'PNG')
        win['img'].update(data = bio.getvalue())
        win['txt'].update(loadname)
        
    except:
        win['img'].update()
        win['txt'].update('Failed1')
        
img = None

def saveimage():
    if img == None:
        return 
    savename = sg.popup_get_file('name the png file',save_as = True)
    if not savename:
        sg.PopupTimed('Type the name of the PNG file')
        return
    if savename.endswith('.png') == False:
        savename =savename +'.png'
    try:
        img.save(savename)
        win['txt'].update(savename +'is saved ')
    except:
        win['txt'].update('Failed2')
        
while True:
    e,v = win.read()
    if e == 'btn1':
        loadimage()
    if e == 'btn2':
        saveimage()
    if e == None:
        break
    
win.close()