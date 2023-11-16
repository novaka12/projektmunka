def vege(mondat):
    if mondat.endswith("."):
        kijelento=print("Ez egy kijelentő mondat.")
        return kijelento
    elif mondat.endswith("?"):
        kerdo=print("Ez egy kérdő mondat.")
        return kerdo
    elif mondat.endswith("!"):
        felk=print("Ez egy felkiáltó mondat")
        return felk
    
mondat=None
while mondat!="":
    mondat=input("Írj be egy mondatot: ")
    vege(mondat)