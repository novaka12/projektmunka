def abetu(szo):
    if szo.startswith("a") or szo.startswith("A"):
        return True
    else:
        return False
    

szo=None
while szo!="":
    szo=input("Írj be egy szavat: ")
    if abetu(szo):
        print("A szó a betűvel kezdődik!")
    else:
        print("A szó nem a betűvel kezdődik!")

    