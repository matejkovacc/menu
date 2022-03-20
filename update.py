total = 0
xyz = []
pijaca = ["Coke", "Voda", "Sok", "Pivo", "Čaj"]
cena1 = [2.50, 4.60, 3.40, 2.80, 3.20]
glavna_jed = ["Zrezek", "Krompir", "Čufti", "Gobe"]
cena2 = [5.20, 6.30, 4.80, 7.20]
sladica = ["Štrudelj","Torta","Tiramisu"]
cena3 = [3.80, 4.10, 5.10]

print("Pijača")
for i, h in enumerate(cena1, 1): 
    print(f"{i}. {pijaca[i-1]} ____________________{h}€")

izbira = int(input("Vnesite številko pred željeno pijačo: "))
for i in range(len(pijaca)):
    if izbira == i+1: 
        total += cena1[int(izbira)-1]
        xyz.append(pijaca[i])

print("Glavna jed")
for j, h in enumerate(cena2, 1): 
    print(f"{j}. {glavna_jed[j-1]} ____________________{h}€")

izbira = int(input("Vnesite številko pred željeno glavno jedjo: "))
for j in range(len(glavna_jed)): 
    if izbira == j+1: 
        total +=cena2[int(izbira)-1]
        xyz.append(glavna_jed[j])

print("Sladica")
for k, h in enumerate(cena3, 1): 
    print(f"{k}. {sladica[k-1]} ____________________{h}€")

izbira = int(input("Vnesite številko pred željeno sladico: "))        
for k in range(len(sladica)):
    if izbira == k+1: 
        total +=cena3[int(izbira)-1]
        xyz.append(sladica[k])
        
for m, n in enumerate(xyz, 1): 
    print(f"{m}. {xyz[m-1]}")
print(f"Skupen znesek znaša: {round(total, 2)}€")

izbira= int(input("Vnesite številko naročila, ki ga želite odstraniti: "))
xyz.pop(izbira-1)
for o, p in enumerate(xyz, 1): 
    print(f"{o}. {xyz[o-1]}")
    total = total 
print(f"Skupen znesek znaša: {round(total, 2)}€")

#print(xyz)
#print(f"Skupen znesek znaša: {round(total, 2)}€")
#izbira = input("Vnesite številko pred naročilom, ki ga želite odstraniti: ")
#for o in xyz:
#    if izbira == o: 
#        xyz.pop(o)
#print(xyz)
#for o in xyz: 
#    if izbira == o: 
#        xyz.remove(xyz[o])
#print(xyz)
#for m, n in enumerate(xyz, 1): 
#    if izbira == m: 
#        xyz.remove(m-1)
#    print(f"{m}. {xyz[m-1]}")





#for  in range(len(xyz)): 
#    if izbira == n+1:
#        xyz.remove(n)
#    print(xyz)
    #print(f"{m}. {xyz[m-1]}")
print(f"Skupen znesek znaša: {round(total, 2)}€")

