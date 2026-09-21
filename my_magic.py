def my_magic(sigma):                # Cette fonction retourne le nombre magic d'une permutation
    k=0                             # Initialise la variable k, qui sommera les i plus tard
    for i in range (1,len(sigma)):  # On laisse varier i sur la liste
        if sigma[i-1]>sigma[i]:     # Si sigma(i)>sigma(i+1) on retient le i
            k+=i                    # Somme les i
    return k                        # Retourne la somme
