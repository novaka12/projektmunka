ido=int(input("Hány órás visszaszámlálást tervezünk? "))
db=int(0)
for x in range(-ido, 0):
    print("Visszaszámlálás: ",x*(-1))
    felf=(input("Fel kell függeszteni a visszaszámlálást? (i/n) "))
    if felf=="i":
        db+=1

print("A rakéta a visszaszámlálást követően ennyi órával indult: ",ido+db)
    