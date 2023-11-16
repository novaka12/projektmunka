ev=int(input("Kérek egy évszámot: "))
if(ev%4==0 and ev%100!=0 or ev%400==0):
    print("Az év szökőév!")
else:       
    print("Az év nem szökőév!")
