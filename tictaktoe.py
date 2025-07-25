def board(row,column):
    for i in range(size):
        row.append([])
        for j in range(size):
            row[i].append(column)

def output(size,row):
    for i in range(size):
        print(size*'----')
        for j in range(size):
            print('|',row[i][j],end=' ')
        print('|\n',end='')
    print(size*'----')

size=int(input("Number of Rows & Columns: "))
play=x_score=o_score=tie_score=0
row=[]
column=' '
while True :
    board(row,column)
    horizontal=vertical=0

 
    for i in range(size*size) :
        print(row)
        play+=1
        if play % 2 == 0:
            print('Player O\'s turn')
        else:
            print('Player X\'s turn')
        row_dt=int(input(f"Enter Row (1-{size}): "))
        column_dt=int(input(f"Enter Cloumn (1-{size}): "))
        if play %2 == 0:
            row[row_dt][column_dt]='O'
        else :
            row[row_dt][column_dt]='X'
        output(size,row)
        for z in range(size):
            x_counter=o_counter=tie_counter=count=0
            for j in range(size):
                if row[z][j] == 'X':
                    x_counter+=1
                elif row[z][j] == 'O' :
                    o_counter+=1
                else :
                    tie_counter+=1
                
            if x_counter == size :
                print('Player X WIN\'S') 
                x_score+=1
                horizontal=1           
            elif o_counter == size:
                print("Player O WIN'S")
                o_score+=1
                horizontal=1
            elif horizontal != 1 :
                x_counter=o_counter=tie_counter=count=0
                for j in range(size):
                    if row[j][z] == 'X':
                        x_counter+=1
                    elif row[j][z] == 'O' :
                        o_counter+=1
                    else :
                        tie_counter+=1
                    
                if x_counter == size :
                    print('Player X WIN\'S')
                    x_score+=1
                    vertical=1            
                elif o_counter == size:
                    print("Player O WIN'S")
                    o_score+=1 
                    vertical=1   

                elif vertical != 1 :
                    x_counter=o_counter=tie_counter=count=0
                    for j in range(size):
                        if row[j][j] == 'X' or row[j][size - 1 - j] == 'X' :
                            x_counter+=1
                        elif row[j][j] == 'O' or row[j][size - 1 - j] == '0':
                            o_counter+=1
                        else :
                            tie_counter+=1
                        
                    if x_counter == size :
                        print('Player X WIN\'S') 
                        x_score+=1          
                    elif o_counter == size:
                        print("Player O WIN'S")  
                        o_score+=1          
                    else :
                        count+=1
                        if count == size :
                            print("TIE")  
                            tie_score+=1                  
                        else:
                            continue

                else :
                    count+=1
                    if count == size :
                        print("TIE") 
                        tie_score+=1                   
                    else:
                        continue              
            else :
                count+=1
                if count == size :
                    print("TIE") 
                    tie_score+=1                   
                else:
                    continue
            print("Player 'X' Score:",x_score)
            print("Player 'O' Score:",o_score)
            print("'TIE' Counter:",tie_score)
            print('--------------------------------')
            row.clear()
            board(row,column)
            choice=input("Do you want to Restart the game? (y/n) ").lower()
            if choice=='n':
                continue
            else:
                x_score=o_score=tie_score=0