def determine_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("Impossible de construire un triangle avec ces longueurs")
    elif a == b == c:
        print("Le triangle est équilatéral")
    elif a == b or a == c or b == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Le triangle est rectangle et isocèle")
        else:
            print("Le triangle est isocèle mais pas rectangle")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Le triangle est rectangle mais pas isocèle")
    else:
        print("Le triangle est quelconque")
        
        
a = int(input("Entrez la longeur A : "))
b = int(input("Entrez la longeur B : "))
c = int(input("Entrez la longeur C : "))

determine_triangle(a, b, c)

