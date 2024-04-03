import PySimpleGUI as sg 
sg.theme('DarkBrown3')

layout = [[sg.T('Show your secret of the birth')],
          [sg.T('How old are you? '),sg.I('18',k='in1')],
          [sg.T('How old is your parent? '),sg.I('48',k='in2')],
          [sg.B('Run',k = 'btn')],
          [sg.T(k='txt')]] #k ='in1' is a placeholder

win = sg.Window('Birth app', layout,
                font = (None, 14),size =(420,170))

def execute():
    in1 = int(v['in1'])
    in2 = int(v["in2"])
    txt = f'When your parent was {in2-in1}, you were born'
    win['txt'].update(txt)
    
while True:
    e,v = win.read()
    if e == 'btn':
        execute()
    if e == None:
        break
    
win.close()

