def paros(szam):
    if szam%2==0:
        return True
    
    else:
        return False
    
szam=1
while paros(szam)==False:
    szam=int(input("Kérek egy számot: "))
    if paros(szam):
        print("A szám páros!")
        break