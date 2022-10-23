from operator import truediv


def zig_zag(rows, cols):

    # Initializari
    zig_zag_matrix = []
    # De acest flag ne vom folosi pentru a cunoaste directia in care se "plimba"
    # valorile noastre de 1
    flag = True
    # Acest step ne va spune cand trebuie sa schimbam flag-ul si ne vom folosi
    # de el pentru a adauga 1 in matricea noastra
    step = 0
    # numara cate linii am format
    indexRow = 0
    ################### TO DO #########################
    # Un while pentru a crea numarul de randuri necesar
    while (indexRow <= rows):
        """
            In acest caz, inseamna ca 1 a atins peretele imaginar din dreapta al
            matricei. De exemplu:
        1 0 0 0
        0 1 0 0
        0 0 1 0
        0 0 0 1 in acest moment step == cols - 1 si trebuie sa schimbam flag-ul pentru a avea continuitate
        0 0 1 0 etc
        """
        if (step == cols - 1):
            flag = False
        
        """
            In acest caz, inseamna ca 1 a atins peretele imaginar din stanga al
            matricei. De exemplu:
        1 0 0 0
        0 1 0 0
        0 0 1 0
        0 0 0 1
        0 0 1 0
        0 1 0 0
        1 0 0 0 aici atinge peretele din stanga si trebuie schimbat flag-ul din nou
        """ 
        if (step == 0):
            flag = True
        
        # Vom crea o lista de liste, iar row va fi fiecare linie din matricea pe
        # care o vom crea.
        row = []
        # Avem nevoie de un numar cols de coloane
        for i in range(cols):
            # In acest caz, punem 1 pentru ca face parte din diagonala noastra
            # zig zag, altfel avem doar 0
            if (i == step):
                row.append(1)
            else:
                row.append(0)
        # Adaugam fiecare linie in lista noastra pentru a forma matricea
        zig_zag_matrix.append(row)

        # In acest caz, ne vom muta o pozitie mai la dreapta pentru a mentine continuitatea
        # altfel, ne vom muta o pozitie mai la stanga din acelasi motiv
        if (flag):
            step += 1
        else:
            step -= 1
        indexRow += 1
            

    ###################################################

    return zig_zag_matrix
