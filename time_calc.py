import time
while True:
    try:
        mins=int(input('Minutes: '))
        break
    except ValueError:
        print('Error! Enter an integer!')
        continue    

start=time.time()

hours=0
days=0
weeks=0
years=0

while mins>=60:
    hours+=1
    mins-=60
    
while hours>=24:
    days+=1
    hours-=24
    
while days>=365:
    if years%4==3:
        if days>=366:
            years+=1
            days-=366
    else:
        years+=1
        days-=365

while days>=7:
    weeks+=1
    days-=7
    
if years!=0:
    print(f'{years} year', end='')
    if years!=1:
        print('s', end='')
    print(',', end='')

if weeks!=0:
    print(f'{weeks} week', end='')
    if years!=1:
        print('s', end='')
    print(',',end='')
    
if days!=0:
    print(f'{days} day', end='')
    if days!=1:
        print('s', end='')
    print(',',end='')

if hours!=0:
    print(f'{hours} hour', end='')
    if hours!=1:
        print('s', end='')
    print(',',end='')

if mins!=0:
    print(f'{mins} min', end='')
    if mins!=1:
        print('s', end='')
    print(',',end='')

print(f'Time taken: {time.time()-start}')