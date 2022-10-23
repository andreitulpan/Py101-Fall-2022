
def func(string_message):
    """ 
    Puneti rezultatul codificarii mesajului in "encoded_message"

    HINT!
    chr() si ord() sunt functii implicite care "jongleaza" cu caracterele
    ASCII si codificarile lor. Astfel, daca pentru litera 'A', avem codificarea
    65, iar pentru 'B' avem 66, atunci:
    
    chr(65) = 'A'   ||   chr(66) = 'B'  
    ord('A') = 65   ||   ord('B') = 66

    ANOTHER HINT!
    Poti folosi dictionarele.
    """
    
    encoded_message = ""
    ################### TO DO #########################
    """
        Si aici sunt diferite modalitati prin care se poate rezolva. Cateva ar fi:
    creearea unei liste cu alfabetul, maparea literelor intr-un hashmap.
        Voi rezolva task-ul cu hashmap pentru a ne familiariza mai mult cu conceptul.
    Maparea se va face: caracterele vor fi cheile, iar codificarile lor vor fi
    valorile.
    """
    # initializam hashmap-ul
    hashmap = {}
    hashmap[' '] = 0    # Avem nevoie de un hashmap pentru a putea tine minte indexul fiecarei litere
                        # eg. A -> 1, B -> 2 samd. Vom crea un hashmap in felul urmator:
                        # hashmap[' '] = 0, hashmap['A'] = 1 samd.
    # Alfabetul englez are 26 de litere, deci vom avea nevoie de 26 de pasi pentru
    # a mapa literele. Ne vom folosi de codificarea ASCII a caracterelor noastre
    # si A are codul ASCII 65. Daca vom creste acest numar vom obtine B, C samd.
    for i in range(26):
        # Functia chr ne va oferi caracterul ASCII cu codul 65 + i
        # ii atribuim valoarea i + 1 deoarece for-ul incepe de la 0, iar la noi
        # valoarea 0 corespunde ' '
        hashmap[chr(65 + i)] = i + 1
    # Un foreach pentru a trece prin fiecare caracter al string-ului primit
    # si creearea rezultatului
    for char in string_message:
        encoded_message += str(hashmap[char])

    ###################################################

    return encoded_message