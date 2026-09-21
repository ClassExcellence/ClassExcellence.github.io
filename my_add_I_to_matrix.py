def my_add_I_to_matrix(mmatrix):         # Cette foction ajoute la matrice identite correspondante a droite de la matrice carrée
    for k in range(len(mmatrix)):        # On laisse varier k sur les lignes des la matrice
	    cc=[0]*(len(mmatrix)-1)          # On crée les lignes de la matrice identité, mais sans les "1"
	    cc.insert(k,1)                   # On ajoute les 1 a la bonne place
	    mmatrix[k].extend(cc)            # On colle la kieme ligne de la matrice identité a la k ieme ligne de la matrice
    return mmatrix                       # Retourne la matrice
