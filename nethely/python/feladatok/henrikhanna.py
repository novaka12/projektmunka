def jon(kerd1, kerd2):
    if kerd1=="Igen" and kerd2=="Igen":
        ketto=print("Mind a ketten jönnek kosarazni")
        return ketto
    elif kerd1=="Igen" and kerd2=="Nem":
        egy=print("Csak az egyikük jön kosarazni")
        return egy
    elif kerd1=="Nem" and kerd2=="Igen":
        egy=print("Csak az egyikük jön kosarazni")
        return egy
    elif kerd1=="Nem" and kerd2 =="Nem":
        nulla=print("Egyikük sem jön kosarazni")
        return nulla
    
kerd1=input("Jön Henrik ma kosarazni?")
kerd2=input("Jön Hanna ma kosarazni?")

print(jon(kerd1, kerd2))
