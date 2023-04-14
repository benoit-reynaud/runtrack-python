def distance_toilets(marches, hauteur):
    # Calculer la distance en mètres parcourue pour une montée et une descente
    distance_par_marche = (hauteur * 2) / 100.0  # convertir la hauteur en cm en m
    # Calculer la distance totale parcourue en montant et descendant pour une journée
    distance_jour = distance_par_marche * marches * 2
    # Calculer la distance totale parcourue en une semaine
    distance_semaine = distance_jour * 7
    # Formater la chaîne de sortie
    sortie = "Pour {} marches de {} cm, le gardien parcourt {:.2f} m par semaine.".format(marches, hauteur, distance_semaine)
    return sortie

print(distance_toilets(10, 20))