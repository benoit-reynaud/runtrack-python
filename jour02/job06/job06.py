def affiche_signe(nombre):
    if nombre<0:
        print("negatif")
    elif nombre>0:
        print("positif")
    else:
        print ("zero")
        
affiche_signe(10)
affiche_signe(-5)
affiche_signe(0)

nombre = int(input("Entrez un nombre : "))
affiche_signe(nombre)