def func(size):

    romb = ""

    ################### TO DO #########################
    """
        Pentru a nu hardcoda tot mereu valorile @ . ' ', cel mai bine folosim
    constante. Le-am declarat si asignat aici.
    """
    edge = '@'
    interior = '.'
    space = ' '

    # Numarul de linii de care avem nevoie sa stim de cate ori adaugam in string
    lines = size
    # Avem nevoie de middle pentru a folosi numarul corespunzator de spatii
    # x va fi deinmultitul spatiilor, iar y deinmultitul punctelor din interior
    middle = size // 2
    x = middle
    y = 0
    if not size % 2:
        middle -= 1
    # Cream rand cu rand in string-ul nostru
    while (lines):
        # Adaugam in string fiecare "rand" pe care il formam
        romb += x * space + edge + y * interior + edge
        # Trecem la urmatorul rand
        lines -= 1
        # In cazul in care e lines mai mare decat mijlocul, inseamna ca suntem
        # in jumatatea de jos a rombului si trebuie sa crestem numarul de puncte
        # si scadem numarul de spatii
        if lines > middle:    
            y += 2
            x -= 1
        else:   # In caz contrar, scadem numarul de puncte si crestem numarul de spatii
            y -= 2
            x += 1
        # cate un \n pentru a trece la randul urmator
        romb += "\n"
    if not size % 2:
        romb += x * space + 2 * edge + "\n"

    ###################################################

    return romb