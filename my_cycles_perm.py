def my_cycles_perm(sigma):                    # Cette fonction décompose une permutation en cycles dinstincts.
	auxsigma=list(sigma)
	compteur=list(range(1,len(auxsigma)+1))   # On va créer la permutaion identité
	liste_cycles=list()                       # On crée la liste qui contiendra les éventuels cycles
	for k in compteur:                        # On laisse k lire la permutation
		if k!=auxsigma[k-1]:                  # On verifie que k n'est pas un element fixe
			cycle=[k]                         # Alors il peut etre le premier nombre d'un cycle
			b=auxsigma[k-1]                   # On pose b = l'image de k par la permutation sigma
			while b != k:                     # On crée une boucle qui s'arrete quand on retombe sur k.
				cycle.append(b)               # On ajoute b a notre cycle.
				compteur.remove(b)            # On retire les nombres déjà mis dans un cycle
				b=auxsigma[b-1]               # On reccommence avec l'image de b
			liste_cycles.append(cycle)        # Maintenant que notre cycle est crée on l'ajoute a notre liste
	return liste_cycles                       # Si il n'y a plus de nombres, on retourne la décomposition
