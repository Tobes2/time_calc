import time
print()

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

while mins>=525600:
    if years%4==3:
        if mins>=527040:
            years+=1
            mins-=527040
    else:
        years+=1
        mins-=525600

while mins>=10080:
    weeks+=1
    mins-=10080

while mins>=1440:
    days+=1
    mins-=1440

while mins>=60:
    hours+=1
    mins-=60

1000
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
    print(f'{mins} minute', end='')
    if mins!=1:
        print('s', end='')
    print('.')

print(f'Time taken: {time.time()-start}')
print()