import datetime 

now = datetime.datetime.now()
print(f'{now: %m/%d/%H:%M:%S}')
goal = now.replace(hour = 16, minute = 00, second = 0)

print(f'Goal = {goal:%m/%d %H:%M:%S}')
td = goal - now
print(td)
