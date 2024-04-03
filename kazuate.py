import PySimpleGUI as sg 
import random 

sg.theme('Darkbrown3')

layout = [[sg.T('Guess the number between 0 - 100 ')],
          [sg.Im(k='img1'),sg.T(k='txt1')],
          [sg.I(k ='in1', size = (10)),
          sg.B('Input', k ='btn', bind_return_key = True)]]

win = sg.Window('Guessing game', layout, font = (None,14), finalize = True)

def question():
    global playflag, ans , count 
    ans = random.randint(1,100)
    count = 0
    win['txt1'].update('')
    win['img1'].update('futaba0.png')
    playflag = True
    
def anscheck():
    global playflag,count
    if v['in1'].isdecimal == False:
        win['txt1'].update('Type a number ')
    else:
        count +=1
        mynum = int(v['in1'])
        if mynum == ans:
            win['txt1'].update(f'{count} times: Correct \n You can continue by clicking a button')
            win['img1'].update('futaba2.png')
            playflag = False
        elif mynum < ans:
            win['txt1'].update(f'{count} times : Still bigger ')
        else:
            win['txt1'].update(f'{count} times still smaller ')
question()

while True:
    e,v = win.read()
    if e == 'btn':
        if playflag == False:
            question()
            
        else:
            anscheck()
            
    if e == None:
        break
win.close()