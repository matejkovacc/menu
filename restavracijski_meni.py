
#MENU = "Big mac", "French fries", "Burger"
#print(MENU)
#trenutno_narocilo = []
#order = input("Vnesite svoje naročilo")

#if order in MENU: 
#    trenutno_narocilo.append(order)
#    print(trenutno_narocilo)
#else: 
#    print('Tega ne strežemo')



#print("[1] Burger, \n[2] Big mac\n, \n[3] Chicken nuggets")

#narocilo = []
#pijaca = []
#sladica = []
#option = int(input("Izberite meni"))
#for narocilo, pijaca, option in 
#while option != 0: 
#    if option == 1: 
#        narocilo.append(option)
#        print("izbrali ste opcijo 1")
#    elif option == 2: 
#        narocilo.append(option)
#        print("izbrali ste opcijo 2")
#    else: 
#        print("tega ne morete izbrati")
#        narocilo.append(option)
#    option = int(input("Izberite pijačo"))

#print(f"Pijačo ste naročili: {pijaca}, za glavno jed ste naročili: {narocilo}, za sladico ste narocili: {sladica}")
total = 0
x = [["Coke", float(2.50)], ["Water", float(4.60)], ["Juice", float(3.42)], ["Tea", float(2.80)]]
y = [["Goveja juha", float(3.5)], ["Dunajski zrezek", float(5.50)], ["Krompir", float(4.20)]]
z = []
xyz = []
cene = [2.50, 4.52, 35.3, 24.3]

#ime = input("Dobrodošli, vpišite ime na katero imate rezervacijo.")
#print(f"Gospod/gospa {ime}prosim prisedite za sledečo mizo.")
#pijaca = input("Kaj boste pili? Prosim vnesite številko pred željeno pijačo")
#if pijaca != str():  
#    input("Vnesite številko pred željeno pijačo. Poskusite ponovno ")
#else: 

narocilo = int(input("Vnesite številko pred željeno pijačo: "))
for i in range(len(x)):
    if narocilo == i: 
        total += x[i][1]
        xyz.append(x[i])
        narocilo = int(input("Vnesite željeno glavno jed: "))
for j in range(len(y)):
    if narocilo ==j: 
        total +=y[j][1]
        xyz.append(y[j])
        narocilo = int(input("Vnesite željeno sladico: "))
for k in range(len(z)): 
    if narocilo == k: 
        total += z[i][1]
        xyz.append(z(i))

print(f"Narocili ste {xyz}")



    #else: 
    #    print("Žal tega nimamo v ponudbi. Predlagma ")

print("Thank you for your ordering!\nYour total cost is: €" + str(total))






    
    
    #if izbira == x[i]: 
      #  print(f"Izbrali ste {x[izbira]}")
     #   continue
    #print(f"Izbrali ste {x[izbira]}")
        



