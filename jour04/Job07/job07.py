L=[8,24,48,2,16]
total_multiple_de_3 = 0


print(L)

for nombre in L:
    if nombre % 3 ==0:
        total_multiple_de_3 += 1
        
        
print("Le nombre de multiple de 3 dans la liste : ",L,"est : ",total_multiple_de_3)       
        

