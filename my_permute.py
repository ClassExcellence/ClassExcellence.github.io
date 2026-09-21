def my_permute(llist):                          # Cette fonction donne toutes les permutations possibles d'une liste
    auxllist=list(llist)
    tout=[]                                     # On crée une liste "tout" qui contiendra les éventuelles permutations
    if len(auxllist)==0:                        # Une liste vide ne possède aucune permutation par convention
        return []
    elif len(auxllist)==1:                      # Un seul élèment possède seulement la permutation identité
        return [auxllist]
    else:                                       # Si la liste possède n elements (n>1), nous procédons a l'algorithme
        for n in range(len(auxllist)):          # On commence par fixer un premier élement, nous avons n choix
            a=auxllist[n]
            auxllist.remove(a)                  # On crée une liste avec les élements non fixés
            for p in my_permute(auxllist):      # Maintenant on laisse se permuter les n-1 elements non fixes
                tout.insert(-1,[a]+p)           # Par récurrance, nous arriverons a la permutation triviale d'un seul élément
            auxllist.insert(n,a)                # On ajoute chaque permutations a notre liste "tout"
        return tout                             # Retourne liste "tout"
