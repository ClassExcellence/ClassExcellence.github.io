def add_alpha_row_j_to_row_i(mmatrix,i,j,alpha):                           # Cette fonction ajoute alpha*j ieme ligne a la i eme ligne
	for k in range(len(mmatrix[j-1])):                                     # On fait varier k sur la longueur d'une ligne
		mmatrix[i-1][k]=alpha*mmatrix[j-1][k]+mmatrix[i-1][k]              # Ajoute la alpha*j ieme ligne à la ieme ligne
	return mmatrix                                                         # Retourne la matrice

