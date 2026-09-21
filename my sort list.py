def my_sort_list(l):                      //range les nombres d'une liste par ordre croissant
    i=0                                   //initialise une variable i
    while i+1<len(l):                     //cette boucle comparer un terme et le terme suivant
        if l[i]<=l[i+1]:                  //si le premier est plus petit ou egale au suivant on continue
            i+=1
        else:                             // sinon on echange ces deux termes et on repred depuis le tout debut
            l[i],l[i+1]=l[i+1],l[i]
            i=0
    return l
