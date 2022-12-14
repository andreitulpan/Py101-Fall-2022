class Cart:
    def __init__(self):
        # Observam ca avem o lista de produse
        self.list_cart = []

    def add(self, new_product):
        """
        TODO:
            * adauga un produs in lista de cumparaturi list_cart

        Args:
            * new_product (Product):    produsul ce va fi adadugat in cart
            
        """
        # Adaugam noul produs in cart
        self.list_cart.append(new_product)

    def remove(self, product_name):
        """
        TODO:
            * sterge produsul din lista de cumparaturi list_card
        
        Args:
            * product_name (str):    numele produsului ce va fi scos din cart

        """
        # Verificam daca exista in cart un produs cu numele product_name
        # Noi primim ca parametru un nume, insa in lista avem produse cu
            # campurile aferente
        for product in self.list_cart:
            if product.name == product_name:
                self.list_cart.remove(product)

    def view(self):
        return self.list_cart

    def cart_checkout(self):
        """
        TODO:
            * calculeaza suma preturilor tuturor produselor din cart
            * goleste cartul (in urma cart_checkout, cartul va fi gol)
        
        Return:
            * int:    suma preturilor tuturor produselor din cart

        """
        # Folosim list comprehensions pentru a avea lista de preturi si apelam
        # sum pentru a avea suma totala
        # De asemenea, trebuie sa golim si cosul
        total_sum = sum([product.price for product in self.list_cart])
        self.list_cart = []
        return total_sum