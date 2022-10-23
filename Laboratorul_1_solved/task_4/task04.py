def func(given_numbers):
    ################### TO DO #########################

    # Completeaza doar linia urmatoare
    # Vom crea un tuplu cu 3 elemente care va avea valorile din cerinta
    # sintaxa a fost explicata mai bine in pdf-ul de la curs, insa niciodata
    # nu e rau sa cautati pe google cand si daca uitati one-linerele ca mine:)
    nice_list = [(i, i ** 2, i ** 3) for i in given_numbers if (i % 2 == 0 or i % 3 == 0) and i < 100]

    ###################################################

    return nice_list
