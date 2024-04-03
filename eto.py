import PySimpleGUI as sg 

sg.theme('DarkBrown3')

layout = [[sg.T('Checking a Chinese year animal')],
          [sg.T('Which year is this year? '), sg.I('2022', k = 'in1')],
          [sg.B('Run', k = 'btn')],
          [sg.T(k = 'txt')],
          [sg.Im('futaba.png'),sg.Im('Elicia.png')]]

win = sg.Window('Chinese Year Animal Checker',
                layout,
                font = (None,14),
                size = (520,350))

def execute():
    eto = ['Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Sheep','Monkey','Chicken','Dog','Pig']
    in1 = int(v['in1'])
    etonum = (in1 - 4) % 12
    txt = f"{in1} year is {eto[etonum]}"
    win['txt'].update(txt)

while True:
    e,v = win.read()
    if e == 'btn':
        execute()
    if e == None:
        break
win.close()
        
    