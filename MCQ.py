def his_sub() :
    subject=open('history.txt','r')
    answer=('c','b','a','b','d')
    question=0
    while True :
        question+=1
        while True :
            data=subject.readline()
            if data.strip().lower() == 'end' :
                break
            print(data,end='')
        option=input('Enter Your Option: ')
        if option == answer[question-1] :
            print("corect option\n------------------------------")
        else :
            print("Wrong Option\n------------------------------")
    subject.close()

def geo_sub() :
    subject=open('geography.txt','r')
    answer=('a','a','c','b','d')
    question=0
    while True :
        question+=1
        while True :
            data=subject.readline()
            if data.strip().lower() == 'end' :
                break
            print(data,end='')
        option=input('Enter Your Option: ')
        if option == answer[question-1] :
            print("corect option\n------------------------------")
        else :
            print("Wrong Option\n------------------------------")
    subject.close()

def phy_sub() :
    subject=open('physics.txt','r')
    answer=('b','a','b','d','b')
    question=0
    while True :
        question+=1
        while True :
            data=subject.readline()
            if data.strip().lower() == 'end' :
                break
            print(data,end='')
        option=input('Enter Your Option: ')
        if option == answer[question-1] :
            print("corect option\n------------------------------")
        else :
            print("Wrong Option\n------------------------------")
    subject.close()

sub=input('Which subject?\n1)History\n2)geography\n3)physics\nSelect: ').lower()
if sub == 'history' :
    his_sub()
elif sub == 'geography' :
    geo_sub()
elif sub == 'physics' :
    phy_sub()
else:
    print("INVALID SUBJECT")