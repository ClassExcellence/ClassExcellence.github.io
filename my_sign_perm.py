def my_sign_perm(sigma):                           # Donne le signe d'une permutation
	i=0                                            # Initialise la variable i
	for k in range(len(my_cycles_perm(sigma))):
		i+=len(my_cycles_perm(sigma)[k])-1         # On somme les "longueurs-1" de chaque cycles
	return (-1)**i                                 # Retourne (-1) exposant la somme
