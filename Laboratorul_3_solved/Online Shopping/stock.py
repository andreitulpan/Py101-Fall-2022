class Stock:
    def __init__(self, list_stock):
        # Observam ca stock este o clasa cu un singur camp, o lista de produse
        # Atentie: produse, nu nume de produse
        self.list_stock = []
        for product in list_stock:
            self.list_stock.append(product)

    def add(self, new_product):
        """
        TODO:
            * adauga un produs nou in stoc
        
        Args:
            * new_product (Product):    noul produs de adaugat in stoc

        """
        # Adaugam noul produs in stock
        self.list_stock.append(new_product)
    
    def remove(self, product_name):
        """
        TODO:
            * sterge din stocul magazinului produsul dat ca parametru
        
        Args:
            * product_name (str):    numele produsului urmeaza a fi sters

        """
        # Verificam daca exista in stock un produs cu numele product_name
        # Noi primim ca parametru un nume, insa in lista avem produse cu
            # campurile aferente
        for product in self.list_stock:
            if product.name == product_name:
                self.list_stock.remove(product)

    def view(self):
        """
        TODO:
            * returneaza stocul curent

        Returns:
            * [Product]:    lista de produse din stoc
            
        """
        # Returnam lista de produse
        return self.list_stock