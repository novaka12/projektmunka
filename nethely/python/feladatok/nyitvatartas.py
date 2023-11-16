ido=int(input("Hány óra van most? "))
if ido>7 and ido<16:
    print("A bolt nyitva van.")
    print("Ennyi órád van még odaérni: ", 16-ido)
else:
    print("A bolt zárva van.")