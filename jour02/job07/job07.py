def codeur(langage):
    if langage =='javascript':
        print("tu es un develloppeur web")
    elif langage=='python':
        print("tu es un developpeut IA")
    elif langage=='java':
        print ("tu est un developpeur logiciel")
    elif langage=='reactjs':
        print("tu es un developpeu mobile")
    else:
        print("un jour, je serai le meilleur developpeur...")
        
        
codeur('python')
codeur('java')
codeur('miaou')

langage=input("Dans quel langage informatique écrivez-vous ? : ")
codeur(langage)