def func(nume_complete):
    """
    Creeaza un tuplu "nume_formatat" care sa contina 3 elemente:
    nume_formatat[0] = lista cu numele de familie
    nume_formatat[1] = lista cu primele prenume
    nume_formatat[2] = lista cu celelalte prenume

    HINT!  conversie string - lista || (string.split("delimiter"))
    """


    ################### TO DO #########################
    """
        Sunt mai multe metode prin care puteti rezolva acest task. Una dintre
    ele ar fi: folosim split de 2 ori la indecsii corespunzatori. Alta ar fi
    sa modificam ceea ce ne supara cand facem split prima oara (anume '-'), iar
    acest lucru poate fi facut prin replace('-', ' ') si astfel obtinem un nume
    de forma Ionescu Popescu Georgescu.
    """
    # Initializari variabile
    nume_formatat = ()
    nume_familie = []
    prenume1 = []
    prenume2 = []
    # Iteram printr-o lista de string-uri, nume ia valoarea fiecarui string din
    # lista (puteti citi despre foreach in orice limbaj de programare)
    for nume in nume_complete:
        # Facand split la ' ', vom obtine o lista de forma ["nume", "prenume1-prenume2"]
        # pe noi ne intereseaza doar numele in acest caz
        nume_familie.append(nume.split(' ')[0])
        # Pentru a obtine primul prenume, vom face split la '-' si vom obtine
        # o lista de forma [prenume1, prenume2], pe noi ne intereseaza cel de pe pozitia 0
        prenume1.append(nume.split(' ')[1].split('-')[0])
        # Pentru a obtine al doilea prenume, vom face split la '-' si vom obtine
        # o lista de forma [prenume1, prenume2], pe noi ne intereseaza cel de pe pozitia 1
        prenume2.append(nume.split(' ')[1].split('-')[1])
    # Cream variabila ce trebuie returnata
    nume_formatat = (nume_familie, prenume1, prenume2)

    ###################################################

    return nume_formatat

    