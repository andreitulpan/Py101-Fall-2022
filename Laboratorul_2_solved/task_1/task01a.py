from unittest import result


def task1a(nums):
    '''
    nums -> vector int
    return -> vector int

    Dublati elementele care se divid cu 6, iar pe cele 
    care nu se divid, triplati-le folosind functionale
    '''

    result = []

    ################### TO DO #########################
    # o functie lambda care dubleaza un element daca e divizibil cu 2,
        # alftel il triplam
    doubleElem = lambda x : x * 2 if x % 6 == 0 else x * 3
    # mapam functia lambda pentru fiecare element din nums
    # va puteti imagina ca map face un for prin elementele lui nums si aplica functia doubleElem
        # pe fiecare element din nums
    result = (map(doubleElem, nums))
    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(result)
