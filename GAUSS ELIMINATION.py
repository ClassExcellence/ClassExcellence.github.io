def my_Gauss_elimination(mmatrix):
    auxmmatrix=deepcopy(mmatrix)
    mm=len(auxmmatrix) # mm est le nombre de lignes
    nn=len(auxmmatrix[0]) # nn est le nombre de colonnes
    ll=1 # ll tient compte des lignes
    kk=1 # kk tient compte des colonnes
    while kk<=nn and ll<=mm:
        auxmmatrix=renormalize_columns(auxmmatrix,kk,ll) # on s'assure d'avoir un coefficient non nul en position (ll,kk)
        auxcoeff=auxmmatrix[ll-1][kk-1]
        if auxcoeff!=0:
            auxmmatrix=rescale_row(auxmmatrix,ll,1/auxcoeff) # on normalise la ligne ll-ème
            hh=1
            while hh<=mm: # on efface les coefficients dans la colonne kk-ème,
                if hh!=ll: # sauf le coefficient (ll,kk)
                    auxcoeff2=auxmmatrix[hh-1][kk-1]
                    if auxcoeff2!=0:
                        auxmmatrix=add_alpha_row_j_to_row_i(auxmmatrix,hh,ll,-auxcoeff2)
                hh=hh+1
            ll=ll+1 # on passe à la ligne suivante seulement si "auxcoeff" n'était pas 0
        kk=kk+1 # on passe toujours à la colonne suivante
    return auxmmatrix
a,b,c,d=0,1,2,3
my_Gauss_elimination([[1,-1,1,-1,1,a],[0,0,0,0,1,b],[1,1,1,1,1,c],[16,8,4,2,1,d]])
