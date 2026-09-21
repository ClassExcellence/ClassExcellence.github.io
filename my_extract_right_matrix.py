def my_extract_right_matrix(mmatrix):            # Cette fonction extrait la sous matrice carrée a droite d'un matrice de taille nx2n
    for k in range(len(mmatrix)):                # On laisse varier k sur les lignes des la matrice
	    mmatrix[k]=mmatrix[k][-len(mmatrix):]    # On va garder que les "n" derniers éléments de chaque ligne
    return mmatrix                               # On retourne la matrice
