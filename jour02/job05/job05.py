def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator =='%':
        return num1 * (num2/100)
    else :
        return "Opérateur invalide."
    

resultat = calcule(34, '+', 7)
print(resultat)

resultat = calcule(58, '-', 13)
print(resultat)

resultat = calcule (20, '%', 15)
print(resultat)

resultat = calcule (30, '*', 6)
print("le resultat est : ", resultat)


num1 = int(input("Entrez le premier nombre : "))
operator = input("Entrez l'opérateur (+,-, *, /, %) : ") 
num2 = int(input("Entrez le deuxième nombre : "))

resultat = calcule (num1, operator, num2)
print("Le résultat est : ", resultat)

