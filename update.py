total = 0
xyz = []
pijaca = ["Coke", "Voda", "Sok", "Pivo", "Čaj"]
cena1 = [2.50, 4.60, 3.40, 2.80, 3.20]
glavna_jed = ["Zrezek", "Krompir", "Čufti", "Gobe"]
cena2 = [5.20, 6.30, 4.80, 7.20]
sladica = ["Štrudelj","Torta","Tiramisu"]
cena3 = [3.80, 4.10, 5.10]

print("Pijača")
for i, h in enumerate(cena1, 1): #keeping a count of iterations
    print(f"{i}. {pijaca[i-1]} ____________________{h}€")

izbira = int(input("Vnesite številko pred željeno pijačo: "))
for i in range(len(pijaca)):
    if izbira == i: 
        total += cena1[int(izbira)-1]
        xyz.append(pijaca[i])

print("Glavna jed")
for j, h in enumerate(cena2, 1): #keeping a count of iterations
    print(f"{j}. {glavna_jed[j-1]} ____________________{h}€")

izbira = int(input("Vnesite številko pred željeno glavno jedjo: "))
for j in range(len(glavna_jed)): 
    if izbira == j: 
        total +=cena2[int(izbira)-1]
        xyz.append(glavna_jed[j])

print("Sladica")
for k, h in enumerate(cena3, 1): #keeping a count of iterations
    print(f"{k}. {sladica[k-1]} ____________________{h}€")

izbira = int(input("Vnesite številko pred željeno sladico: "))        
for k in range(len(sladica)):
    if izbira == k: 
        total +=cena3[int(izbira)-1]
        xyz.append(sladica[k])
        
print(str(xyz)[1:-1], f" skupaj znaša: {round(total, 2)}€")

