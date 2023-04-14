L=[8,24,27,48,2,16,9,7,84,91]
total_multiple_de_2 = 0


print(L)

for nombre in L:
    if nombre % 2 ==0:
        total_multiple_de_2 += nombre
        
        
print("Somme de tous les nombres paires est",total_multiple_de_2)       
        

