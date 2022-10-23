def func(note, nume_materie):
    """
    Trebuie sa creati un tuplu cu numele "pereche",
    in care veti tine, astfel, (media notelor, numele_materiei)
    exemplu: pereche = (...)
    """

    ################### TO DO #########################
    """
        O abordare initiala ar fi sa iterati prin lista de note si sa aflati
    suma, folosind un auxiliar in care adaugati fiecare element din note.
        Python va face viata mai usoara deoarece are multe functii implementate
        deja, functii pe care le puteti folosi in avantajul vostru. (eg sum(), len())
    """
    pereche = (sum(note) / len(note), nume_materie)
    ###################################################

    return pereche
