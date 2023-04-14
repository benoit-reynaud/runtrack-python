L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

print("Dans cette liste : ", L)
maximum =L[0]
minimum =L[0]
    
for nombre in L :
    if nombre < minimum:
        minimum=nombre
    if nombre>maximum:
        maximum=nombre

print("Le maximum est : ", maximum)
print ("Le nombre minimum est :", minimum)