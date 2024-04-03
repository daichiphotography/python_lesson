import PySimpleGUI as sg 

sg.theme('DarkBrown3')

layout = [[sg.Text('Type amount and a number of people ')],
          [sg.Text('Amount'),sg.Input('1000', k = 'in1')],
          [sg.Text('Number'),sg.Input('4', k ='in2')],
          [sg.B('Run', k ='btn'),sg.T(k='txt')]]
win = sg.Window('Split calculator', layout, 
                font = (None,14), size = (320,150))

def execute():
    in1 = int(v['in1'])
    in2 = int(v['in2'])
    txt = f'1 person {in1/in2} baht'
    win['txt'].update(txt)
    
while True:
    e,v = win.read()
    if e== 'btn':
        execute()
    if e == None:
        break

win.close()