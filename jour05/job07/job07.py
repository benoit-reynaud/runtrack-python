def is_valid_word(word):
    """Vérifie si un mot contient uniquement des lettres de l'alphabet."""
    return all(c.isalpha() and c.islower() for c in word)

def next_word(word):
    """Retourne le mot alphabétiquement suivant en permutant deux lettres."""
    if not is_valid_word(word):
        raise ValueError("Le mot doit contenir uniquement des lettres de l'alphabet en minuscules.")
    
    # Trouve les deux premières lettres consécutives qui sont dans l'ordre décroissant
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            break
    else:
        # Le mot est déjà le dernier dans l'ordre alphabétique
        return word
    
    # Trouve la dernière lettre plus grande que la lettre à la position i
    for j in range(len(word)-1, i, -1):
        if word[j] > word[i]:
            break
    
    # Permute les deux lettres trouvées
    new_word = list(word)
    new_word[i], new_word[j] = new_word[j], new_word[i]
    
    # Trie les lettres suivantes dans l'ordre croissant
    new_word[i+1:] = sorted(new_word[i+1:])
    
    return ''.join(new_word)
    
# Demande un mot à l'utilisateur
while True:
    word = input("Entrez un mot contenant uniquement des lettres de l'alphabet en minuscules : ")
    if is_valid_word(word):
        break
    else:
        print("Le mot contient des caractères non autorisés.")
    
# Trouve le mot alphabétiquement suivant et l'affiche
next = next_word(word)
print("Le mot alphabétiquement suivant est :", next)