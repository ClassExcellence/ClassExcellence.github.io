def rescale_row(mmatrix,i,alpha):                                              # Cette fonction multiplie la ieme ligne par un scalaire alpha
	for k in range(len(mmatrix[i-1])):                                     # On fait varier k sur la longueur de la ligne
		mmatrix[i-1][k]=alpha*mmatrix[i-1][k]                          # On remplace la ligne i par alpha*ieme ligne
	return mmatrix                                                         # Retourne la matrice
