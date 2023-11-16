def sikeres(pont):
    if pont>=48:
        return True
    else:
        return False

nev=None


while nev!="":
    nev=str(input("Add meg a vizsgázó nevét: "))
    if nev=="":
        break
    pont=int(input("Add meg a pontszámát: "))
    if sikeres(pont):
        print(nev, " vizsgája sikeres!")
       
    else:
        print(nev, " vizsgája sikertelen!")
        

