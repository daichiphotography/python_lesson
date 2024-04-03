import PySimpleGUI as sg 
sg.theme('DarkBrown3')

layout = [[sg.T('Text')],
          [sg.I('Input')],
          [sg.Multiline('Multiple lines text\n 1st \n2nd', size =(30,3))],
          [sg.Image('futaba.png')]]

win = sg.Window('Input test', layout, 
                font = (None,14), size = (300,240))

e,v = win.read()
win.close()