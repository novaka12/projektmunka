class Person:
    def __init__(self, name, country, attack, defence):
        self.name=name
        self.country=country
        self.attack=attack
        self.defence=defence

focistak=[]

#4 ember bekérése
for x in range(3):
    name=input("Kérem a nevet: ")
    country=input("Kérem az országot: ")
    attack=int(input("Kérem a támadását: "))
    defence=int(input("Kérem a védekezését: "))
    p=Person(name,country,attack,defence)
    focistak.append(p)

for x in focistak:
    print(x.name, " Nemzet: ",x.country," Támadás: ", x.attack," Védekezés: ", x.defence)


legjobb=focistak[0]
for x in focistak:
    if x.attack>legjobb.attack:
        legjobb=x

ind=0
jobb=focistak[0]
maxind=0
for x in focistak:
    one=x.attack+x.defence
    two=jobb.attack+jobb.defence
    if one>two:
        two=one
        maxind=ind
    ind+=1
        

f=open("focikartya.txt", "w")
f.write(legjobb.name,)
f.write(" ")
f.write(legjobb.country)
f.write(" ")
f.write(str(legjobb.attack,))
f.write(" ")
f.write(str(legjobb.defence,))
f.write("\n")
f.write(focistak[maxind].country)
f.close()