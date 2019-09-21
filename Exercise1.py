#FIFO先进先出

stack=[]

def pushit():
    stack.append(input("Enter new string:").strip())

def popit():
    if len(stack)==0:
        print("Cannot pop from an empty stack!")
    else:
        print("Removed [','stack.pop()',']")

def veiwstack():
    print(stack)  #calls str() internally

CMDs={'u':pushit(),'o':popit(),'v':veiwstack()}

def showmenu():
    pr='''
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit
    
    Enter yourchoice'''

    while 1:
        while 1:
            try:
                choice=input(pr).strip()[0].lower()
            except(EOFError,KeyboardInterrupt.Indexerror):
                choice='q'

            print("\nYou picked:[%s]"%choice)
            if choice not in 'uovq':
                print("Invalid option,try again")
            else:
                break
        if choice=='q':
            break

    CMDs[choice]()

if __name__ == '__main__':
    showmenu()



