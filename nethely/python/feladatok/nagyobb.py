szam1=int(input("Kérek egy számot: "))
szam2=int(input("Kérek egy másik számot: "))
if szam1 < szam2 or szam1>szam2:
    print("A nagyobb érték: ", max(szam1, szam2))
elif szam1==szam2:
    print("A két szám egyenlő")