import PySimpleGUI as sg 
sg.theme('DarkBrown3')

layout = [[sg.Text('row1,column1')],[sg.Text('row1,column2')],
          [sg.Text('row2,column1')],[sg.Text('row2,column2')],
          [sg.Text('row3,colum1')],[sg.B('Button')]]

win = sg.Window('Layout test',
                layout, font= (None,14),
                size =(350,220))


e,v= win.read()
win.close()