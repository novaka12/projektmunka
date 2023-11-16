jelszoi="Szivecske<3"
felhi="bori99"
ivh=True
felh=str(input("Adja meg a felhasználónevét: "))
jelszo=str(input("Adja meg a jelszavát: "))
while ivh==True:
    
    if felh==felhi and jelszo==jelszoi:
        ivh=False
        break    
    else:
        print("Belépés megtagadva!")
        felh=str(input("Adja meg a felhasználónevét: "))
        jelszo=str(input("Adja meg a jelszavát: "))

print("Belépés engedélyezve!")