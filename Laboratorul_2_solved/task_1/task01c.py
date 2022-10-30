def task1c(words):
    '''
    words -> lista string-uri
    return -> lista string-uri

    Salvati cuvintele care sunt palindrom in "palindromes"
    '''

    palindromes = []

    ################### TO DO #########################
    # filtram words folosind functia lambda pe care am scris-o ca parametru.
    # spre deosebire de map, care doar aplica functia pe elementele listei, fiter
        # ne pastreaza elementele ce satisfac functia transmisa ca parametru.
    palindromes = filter(lambda cuv: cuv == cuv[::-1], words)
    ###################################################
    
    # Nu modificati valoarea de retur a functiei
    return list(palindromes)
