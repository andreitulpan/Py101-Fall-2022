def task(register):
    '''
    register -> dictionar
    return -> lista doar cu numele studentilor
    '''
    names = []

    ################### TO DO #########################
    # filtram elementele dictionarului folosind o lambda care ne calculeaza media.
    # x[0] este cheia unui item, iar x[1] este valoarea unui item, in cazul nostru
        # lista care contine notele.
    students = list(filter(lambda x: (sum(x[1]) / len(x[1])) >= 8.5, register.items()))

    # adaugam in lista finala numele studentilor ce au indeplinit conditia.
    for stud in students:
        names.append(stud[0])
    ###################################################
    
    return names
