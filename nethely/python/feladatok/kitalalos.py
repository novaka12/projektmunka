import random

def gepgondol():
    return random.randint(1,5)
gepszam=gepgondol()
szam=0
while szam!=gepszam:
    print("Gondoltam egy számra 1 és 5 között")
    szam=int(input("Kérem adjon meg egy számot 1 és 5 között: "))

    if szam==gepszam:       
        print("Eltaláltad!")
    elif szam<gepszam:
        print("Nagyobb számra gondoltam!")
    elif szam>gepszam:
        print("Kisebb számra gondoltam!")

        