import PySimpleGUI as sg 
import random

sg.theme('DarkBrown3')

layout = [[sg.T('Rock scissor and paper!')],
          [sg.Im('futaba0.png',k ='img1'),sg.Im(k='img2')],
          [sg.T(k='txt')],
          [sg.B('Rock',k='btn0'),
           sg.B('Scissors', k='btn1'),
           sg.B('Paper',k = 'btn2')]
          ]
win = sg.Window('Rock Scissors and paper app', layout, font = (None, 14))

handimg = ['h0.png','h1.png','h2.png']
message = ('Even','You won', 'You lost')
faceimg = ['futaba0.png','futaba1.png','futaba2.png']


def janken(mynum):
    comnum = random.randint(0,2)
    win['img2'].update(handimg[comnum])
    hantei = (comnum - mynum) %3
    win['txt'].update(message[hantei])
    win['img1'].update(faceimg[hantei])
    
while True:
    e,v = win.read()
    if e == 'btn0':
        janken(0)
        
    if e == 'btn1':
        janken(1)
        
    if e == 'btn2':
        janken(2)
        
    if e == None:
        break
    
win.close()