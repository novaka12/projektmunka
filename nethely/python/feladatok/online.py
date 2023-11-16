class Person:
    def __init__(self, name, score, email):
        self.name=name
        self.score=score
        self.email=email

lista=[]

for x in range(3):
    name=input("Kérem a nevet: ")
    score=int(input("Kérem a pontszámod: "))
    email=input("Kérem az email címed: ")
    p=Person(name,score,email)
    lista.append(p)

leggyengebb=lista[0]
for x in lista:
    if x.score<leggyengebb.score:
        leggyengebb=x

print("Leggyengébben teljesítő játékos neve: ",leggyengebb.name," Pontja: ", leggyengebb.score," Email címe: " ,leggyengebb.email)


        