import random as r

dice=int(input('Number of Dice : '))
count=0
l=[]
while True :
    choice=input('Roll The Dice..?? (y/n) : ')
    if choice in 'Yy' :
        for i in range(dice) :
            l.append(r.randint(1,6))
        count+=1
        print(l)
        l.clear()
        print('Number of Times Dice Rolled : ',count)
    elif choice in 'Nn' :
        print('_Thank You_')
        break
    else :
        print('INVALID CHOICE')