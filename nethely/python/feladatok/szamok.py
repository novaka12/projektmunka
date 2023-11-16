szam=0
ossz=0
szamok=[]
while szam>=-5 and szam<=5:
    szam=int(input("Írjon be egy számot -5 és 5 között: "))
    if szam<-5 or szam>5:
        break
    szamok.append(szam)
    ossz=ossz+szam
print(szamok)
print(ossz)
