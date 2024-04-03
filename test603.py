import random

def question():
    global playflag, ans 
    a = random.randint(0,100)
    b = random.randint(0,100)
    
    ans = a + b 
    
    print(f'{a}+{b} = ? ')
    playflag = True
    
def anscheck():
    global playflag 
    if indata.isdecimal() == True:
        mynum = int(indata)
        if mynum == ans:
            print('Right!')
            playflag = False
        else:
            print(f'it is not {mynum} ')
            
question()
while True:
    indata = input('Please input a number ')
    if playflag == False:
        question()
    else:
        anscheck()