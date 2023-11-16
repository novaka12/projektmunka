import math

def kerulet(a,b):
    ker=2*(a+b)
    return ker

def terulet(a,b):
    ter=a*b
    return ter

def atlo(a,b):
    atl=math.sqrt((a*a)+(b*b))
    return atl

#main

szam1=int(input("Kérem az a oldalt: "))
szam2=int(input("Kérem a b oldalt: "))

print("A téglalap kerülete: ",kerulet(szam1, szam2))
print("A téglalap területe: ",terulet(szam1, szam2))
print("A téglalap átlója: ",atlo(szam1, szam2))