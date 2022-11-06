class Product:
    def __init__(self, name, price):
        """ 
        TODO:
            * completeaza constructorul clasei Product
        
        Args:
            * name (str):    numele produsului instantiat 
            * price (int):    pretul produsului instantiat

        """
        # Completam constructorul clasei, astfel avem doua campuri pentru clasa Product
        self.name = name
        self.price = price

    def __add__(self, other):
        """
        TODO:
            * completeaza supraincarcare operatorului "+"
            * va returna suma preturilor celor doua produse

        Args:
            * self (Product):    primul termen al operatiei de adunare
            * other (Product):    cel de-al doilea termen

        Return:
            * int:  suma preturilor celor doua produse
            
        """
        # Adunam pretul a doua obiecte. Self este o referinta la obiectul curent,
        # iar other este o referinta la un oricare alt obiect.
        return self.price + other.price