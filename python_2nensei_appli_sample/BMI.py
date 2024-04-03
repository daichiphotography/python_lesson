import PySimpleGUI as sg 
sg.theme('DarkBrown3')

layout =[[sg.T('Type heigh and weight')],
         [sg.T('Height in cm'),sg.I('160', key = 'in1')],
         [sg.T('Weight in Kg'),sg.I('60',key ='in2')],
         [sg.B('Run',k='btn'),sg.T(k='txt')]]

win = sg.Window('BMI calculator', layout,
                font = (None,14), size =(320,150))

def execute ():
    in1 = float(v['in1'])/100.0
    in2 = float(v['in2'])
    bmi = in2 / (in1*in1)
    txt = f'BMI value is {bmi: .2f}'
    win['txt'].update(txt)
    
while True:
    e,v = win.read()
    if e == 'btn':
        execute()
    if e == None:
        break
win.close()

