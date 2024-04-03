import PySimpleGUI as sg 
import random 
sg.theme('DarkBrown3')

layout =[[sg.T(k ='txt1')],
         [sg.Im(k='img'),sg.T(k = 'txt2')],
         [sg.T(k = 'txt3'), sg.I(k='in1',size =(10)),
          sg.B(' Input ', k = 'btn', bind_return_key = True )]]
win = sg.Window('Addition game ', layout, font = (None,14),finalize = True)

def question():
    global playflag, ans
    a = random.randint(0,100)
    b = random.randint(0,100)
    ans = a + b
    win['txt1'].update('Additionn game. Input the answer')
    win['txt2'].update('')
    win['txt3'].update(f'A question {a} + {b} = ?')
    win['img'].update('futaba0.png')
    playflag = True
    
def anscheck():
    global playflag
    if v['in1'].isdecimal() == False:
        win['txt2'].update('Type a number ')
    else:
        mynum = int(v['in1'])
        if mynum == ans:
            win['txt2'].update('Right ')
            win['txt1'].update('A button for the next question ')
            win['img'].update('futaba2.png')
            playflag = False
        else:
            win['txt2'].update(f'it is not {mynum}')
            
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