import PySimpleGUI as sg 
import random 

sg.theme('DarkBrown3')

layout =[[sg.T("Let's draw a luck draw")],
          [sg.Im('futaba0.png')],
          [sg.T(k='txt')],
          [sg.B('Draw',k='btn')]]

win = sg.Window('Lucky draw', layout, font = (None,14))

def omikuji():
    kuji = ['Super lucky:5/5','Very Lucky:4/5','Lucky:3/5','Unlucky:2/5','Unfortune:1/5']
    kekka = random.choice(kuji)
    txt = f'You got {kekka} !'
    win['txt'].update(txt)
    
while True:
    e,v = win.read()
    if e == 'btn':
        omikuji()
    if e == None:
        break
win.close()
    