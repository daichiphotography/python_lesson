import PySimpleGUI as sg 
sg.theme('DarkBrown3')

layout = [[sg.T('ABCDE',size = (30,1), justification = 'left')],
          [sg.T('ABCDE',size = (30,1),justification = 'center')],
        [sg.I('ABCDE',size = (30,1),justification = 'right')]]

win = sg.Window('Layout test',
                layout, font= (None,14),
                size =(200,120))



e,v= win.read()
win.close()
