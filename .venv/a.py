import PySimpleGUI as sg 
import io 
import qrcode

sg.theme('Dark Brown3')

layout = [[sg.T('URL: '),sg.I(k = 'in1')],
          [sg.B('Creating a QR code', k = 'btn1')],
          [sg.B('Saving a file', k = 'btn2'), sg.T(k='txt')],
          [sg.Im(k='img')]]

win = sg.Window('QR code maker', layout, size =(320,455))

img = None

def execute():
    global img
    if not v['in1']:
        sg.PopupTimed('Enter the URL')
        return
    img = qrcode.make(v['in1'])
    img.thumbnail((300,300))
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    win['img'].update(data = bio.getvalue())
    
def saveimage():
    if img == None:
        return
    savename = sg.popup_get_file('Name the PNG file to save ', save_as = True)
    if not savename:
        sg.PopupTimed('Type PNG name ')
        return
    if savename.endswith('.png') == False:
        savename = savename + '.png'
    try:
        img.save(savename)
        win['txt'].update(savename + 'is saved')
        
    except:
        win['txt'].update('Failed')
        
while True:
    e,v = win.read()
    if e == 'btn1':
        execute()
    if e == 'btn2':
        saveimage()
    if e == None:
        break
win.close()