def renormalize_columns(mmatrix,j,h):             # Echange la hieme ligne par la premiere ligne inferieure qui possede un coefficient non nul a la jieme position
	k=h-1                                         # On commencera a chercher à partir de la hieme position
	while k<len(mmatrix):                         # On crée un boucle pour que k puisse parcourir la colonne, et s'arreter quand elle arrive au bout de la colonne
		if mmatrix[k][j-1]!=0:                    # Si elle trouve un coefficient non nul à la kieme position, elle echange la hieme ligne avec la kieme
			mmatrix[h-1],mmatrix[k]=mmatrix[k],mmatrix[h-1]
			k=len(mmatrix)                        # Apres avoir echangé, on pose k egale a la longueur de la ligne pour que la boucle s'arrete
		k+=1                                      # Si elle ne trouve pas de coefficient non nul, elle ne fait rien et elle passe au therme suivant
	return mmatrix                                # Retourne la matrice
