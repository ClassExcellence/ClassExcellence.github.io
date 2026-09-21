def my_x_magic(nn):                         # Cette fonction renvoie le polynome magic
    polynome=0                              # Initialise le polynome
    s_n=my_permute(list(range(1,nn+1)))     # On crée l'ensemble Sn
    for k in s_n:
        polynome+=x**my_magic(k)            # On ajoute le monome correspondant
    return polynome                         # Retourne le polynome
