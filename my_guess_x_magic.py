def my_guess_x_magic(nn):             # Cette fonction retourne my_x_magic(nn) mais avec une autre formule
    polynome_final=1                  # Initiale le polynome_final (avec le neutre de la multiplication = 1)
    for i in range(nn):               # A chaque étape on multipliera ce dernier par le my_polynome
        my_polynome=0                 # On va crée le my_polynome, commencons par l'initialiser
        for j in range(nn-i):
            my_polynome+=x**j         # On ajoute le monome correspondant a my_polynome
        polynome_final*=my_polynome   # Multiplie my_polynome a polynome final
    return (expand(polynome_final))   # Retourne le polynome final
