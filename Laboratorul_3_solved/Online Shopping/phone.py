import product

class Phone(product.Product):
    def __init__(self, name, price, ram, cpu):
        # Good practice sa folosim constructorul __init__ al clasei parinte
        product.Product.__init__(self, name, price)
        self.ram = ram
        self.cpu = cpu

    def __str__(self):
        """
        TODO:
            * supraincarca metoda str

        Returns:
            * str:    un string ce va contine informatiile 
                      specifice telefonului (nume, CPU, RAM)

        """
        # Supraincarcam metoda str pentru a returna string-ul de care avem nevoie
        return "The new {} is an unforgettable experience, CPU {}, RAM {}.".format(self.name, self.cpu, self.ram)