from pathlib import Path 

def savetext(filename):
    p = Path(filename)
    txt ='Test data'
    p.write_text(txt,encoding ="UTF-8")
    
savetext('output.txt')