print("\n\n")
print('*'*150)
print("-"*60,": WELCOME IN HANGMAN GAME:","-"*60)
print('*'*150)
def getShape(count):
    print("\n")
    if count ==1:
        print(" "*60,"__|___________________")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         O         ")
        print(" "*60,"  |                  ")
        print(" "*60,"  |                ")
        print(" "*60,"  |                ")
        print(" "*60,"  |                  ")
        print(" "*60,"  |                 ")
        print(" "*60,"  |                ")
        print(" "*60,"  |                 ")
    elif count==2:
        print(" "*60,"__|___________________")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         O         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |        /|         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |                   ")
        print(" "*60,"  |                   ")
        print(" "*60,"  |                   ") 
    elif count==3:
        print(" "*60,"__|___________________")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         O         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |        /|\\         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |                   ")
        print(" "*60,"  |                   ")
        print(" "*60,"  |                   ") 
    elif count==4:
        print(" "*60,"__|___________________")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         O         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |        /|\\         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |        /|         ")
        print(" "*60,"  |                   ")
        print(" "*60,"  |                   ")
        print(" "*60,"  |                   ") 
    elif count==5:
        print(" "*60,"__|___________________")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |         O         ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |        /|\\        ")
        print(" "*60,"  |         |         ")
        print(" "*60,"  |        /|\\        ")
        print(" "*60,"  |                   ")
        print(" "*60,"  |                   ")
        print(" "*60,"  |                   ") 


def getwordfromlist(lst):
    print("\n\n")
    print(" "*60,"THE WORD : ",end='')
    for f in lst:
        print(f.upper(),end=' ')

def play():

    count=0
    word="apple"
    lst=[]
    
    for i in range(1,len(word)+1):
            lst.append('_')
    getwordfromlist(lst)
    while 1>0:
        
        
        character=input("\n\nGUESS CHARACTER : ")
        if 'a'<=character<='z' or 'A'<=character<='Z':
            if character.lower() in word:
                print("                  \u2713",end='')
                j=0
                for k in word:
                    if k==character.lower():
                        lst[j]=character
                    j+=1    
                getwordfromlist(lst)
                if '_' not in lst:
                        print("\n\n")
                        print(" "*40,"😀"*20,"  WINNER  ","😀"*20)
                    
                        # print("!"*110)
                        break 
            else:
                print("                  \u2717",end='')
                count=count+1
                if count<5:
                    getShape(count)
                elif count==5:
                    if '_' in lst:
                        getShape(count)
                        print("\n\n")
                        print(" "*40,"😭"*20,"  LOOSER  ","😭"*20)
                        
                        break
        else:
            print("INVALID CHARACTER..................")            
                
        


play()


