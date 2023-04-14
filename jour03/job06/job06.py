string = "abcdefghijklmnopqrstuvwxyz" * 10
n = 1
while n*(n+1)//2 <= len(string):
    start = (n-1)*n//2
    end = n*(n+1)//2
    print(string[start:end].center(0))
    n += 1
    
#Autre méthode
alphabet = "abcdefghijklmnopqrstuvwxyz" * 10
rows = 10

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    chars = alphabet[:i*2-1]
    print(spaces + chars + spaces[::-1])
    
#Autre méthode

string = "abcdefghijklmnopqrstuvwxyz" * 10

# Initialisation de la variable pour stocker la position dans la chaîne
pos = 0

# Boucle pour afficher les lignes de la pyramide
for i in range(1, 12):
    # Calcul du nombre de caractères à afficher sur cette ligne
    num_chars = 2*i - 1
    
    # Vérification s'il reste suffisamment de caractères dans la chaîne pour afficher cette ligne
    if pos + num_chars > len(string):
        # Si la réponse est non, on sort de la boucle
        break
    
    # Création de la sous-chaîne à partir de la position actuelle dans la chaîne
    sub_string = string[pos:pos+num_chars]
    
    # Affichage de la sous-chaîne centrée dans la pyramide
    print(sub_string.center(26))
    
    # Mise à jour de la position dans la chaîne
    pos += num_chars