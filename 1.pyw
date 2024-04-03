import tkinter as tk 
def execute():
    txt = 'Hello'
    lbl.configure(text = txt)
    
root = tk.Tk()
root.title('Hello Test')
root.geometry('200x100')

lbl = tk.Label(text = '')
btn = tk.Button(text = 'Run', command = execute)

lbl.pack()
btn.pack()
tk.mainloop()


