total = 0
x = ["Coke", float(2.50)], ["Water", float(4.60)], ["Juice", float(3.42)], ["Tea", float(2.80)]
y = ["Goveja juha", float(3.5)], ["Dunajski zrezek", float(5.50)], ["Krompir", float(4.20)]
z = ["Štrudelj", float(2.50)], ["Torta", float(4.20)], ["Tiramisu", float(3.80)]
xyz = []

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
    if narocilo == j: 
        total +=y[j][1]
        xyz.append(y[j])

narocilo = int(input("Vnesite željeno sladico: "))
for k in range(len(z)): 
    if narocilo == k: 
        total += z[k][1]
        xyz.append(z[k])


print(str(xyz)[1:-1])

print("Hvala za vaše naročilo\nVaše naročilo stane €" + str(total))






    



