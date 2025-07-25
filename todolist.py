task=[[],[]]
task_count=0

while True :
    print("To Do List Menu:")
    print("1. View Taks\n2. Add a Task\n3. Mark a Task as Completed\n4. Exit")
    choice=int(input("Enter Your Choice: ")) 
    match choice:
        case 1 :
            task_count=0
            if len(task[0]) != 0:
                print('Personal Task\'s:')
                for i,t in enumerate(task[0]):
                    task_count+=1
                    print(f'{task_count}. {t}')
            if len(task[1]) != 0 :
                print("Work Task's:")
                for i,t in enumerate(task[1]):
                    task_count+=1
                    print(f'{task_count}. {t}')
            print("--------------------------------------")
        case 2 :
            task_count+=1
            task_file=open('todolist.txt','a')
            choice=int(input("1. Personal\n2. Work\nChoice: "))
            match choice:
                case 1 :
                    add_task=input("Enter Task: ").lower()
                    task[0].append(add_task)
                    task_file.write(f'{task_count}. {add_task}\n')
                case 2 :
                    add_task=input("Enter Task: ").lower()
                    task[1].append(add_task)
                    task_file.write(f'{task_count}. {add_task}\n')
            task_file.close()
            print("--------------------------------------")
        case 3 :
            work=input("Enter Your Completed Work: ").lower()
            for category in task :
                for i,t in enumerate(category):
                    if t == work :
                        category[i]=f'{t} (COMPLETED)'

            print("--------------------------------------")
        case 4:
            task_file=open('todolist.txt','w')
            task_file.write('')
            task_file.close()
            break