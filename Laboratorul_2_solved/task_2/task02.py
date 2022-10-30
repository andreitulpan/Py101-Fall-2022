import string


def task(*args):
    '''
    args -> elemente de tipuri diferite
    return -> lista cu elementele corespunzatoare
    '''

    result = []
    ################### TO DO #########################
    
    for elem in args:
        # verificam tipul sa fie int sau str cu len == 1 (asa traducem un char in python)
        # functia islower() este asemanatoare cu ce v-am sugerat la laborator,
            # mai exact sa verificati cu codul ASCII daca litera e mica.
        if type(elem) is int:
            result.append(elem)
        elif type(elem) == str and len(elem) == 1:
            if elem not in "aeiou" and elem.islower():
                result.append(elem)
        else:
            continue

    ###################################################
    
    return result
