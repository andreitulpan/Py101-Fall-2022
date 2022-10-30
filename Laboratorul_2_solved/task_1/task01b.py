def task1b(phrase):
    '''
    phrase -> string
    return -> string

    Transformati in litere mari vocalele din fraza
    si salvati rezultatul in "new_phrase"
    '''

    new_phrase = ""
    ################### TO DO #########################
    # folosim un string pentru a cunoaste vocalele, putem de asemenea sa folosim
        # si o lista pentru vocale.
    vocale = "aeiou"
    # mapam functia lambda, care poate fi scrisa si ca parametru, nu neaparat
        # ca o variabila.
    new_phrase = map(lambda x: x.upper() if x.lower() in vocale else x, phrase)

    ###################################################

    # Nu modificati valoarea de retur a functiei
    return ''.join(list(new_phrase))
