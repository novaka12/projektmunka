import random

def gepdob():
    return random.choice(["fej", "írás"])

jo=0

for x in range(3):
    
    be=str(input("fej vagy írás?: "))
    gepdobott=gepdob()
    
    print("A gép dobása: ", gepdobott)
    
    if be==gepdobott:
        jo=jo+1
        print("Eltaláltad!")
    else:
        print("Nem talált!")

    
print("Helyes találatok száma: ",jo)
    

    



        
    