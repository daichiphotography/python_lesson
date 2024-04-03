import PySimpleGUI as sg 
import datetime 

sg.theme('DarkBrown3')

layout = [[sg.T('00:00:00',font = ('Arial', 24), k ='txt1')],
          [sg.ML(font= ('Arial',18),size = (40,12),k ='txt2')]]
win = sg.Window('Timetable app', layout,font = (None,14),size=(400,260),keep_on_top=True)

sch = [['1st period',7,30],
       ['2nd period', 8,50],
       ['3rd period',9,30],
       ['4th period', 11,10],
       ['5th period',13,10],
       ['6th period',14,00]]

def execute():
    now = datetime.datetime.now()
    now = now.replace(hour=8)
    win['txt1'].update(f'{now:%H:%M:%S}')
    txt2 =''
    for s in sch:
        dt = now.replace(hour =s[1], minute =s[2], second = 0) - now
        if dt.total_seconds() >0:
            txt2 += f'{s[0]} {s[1]:02d}:{s[2]:02d}, remaining time is {dt}  '
            
        else:
            txt2 += f'{s[0]}:{s[1]}:{s[2]:02d} ------\n'
    win['txt2'].update(txt2)
while True:
    e,v = win.read(timeout =500)
    if e == None:
        break
    execute()
win.close()