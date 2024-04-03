import datetime 

sch = [[ 'snack', 9,30],
       ['lunch', 12,30]]

now = datetime.datetime.now()
# now = now.replace(hour = 9)

print(f'Right now = {now: %H:%M:%S} ')
for s in sch:
       dt = now.replace(hour = s[1], minute=s[2],second =0) - now
       print(f' Remaining {dt}')