import product

class Refrigerator(product.Product):
    def __init__(self, name, price, energy_label):
        # Good practice sa folosim constructorul __init__ al clasei parinte
        product.Product.__init__(self, name, price)
        self.energy_label = energy_label

    def __str__(self):
        """
        TODO: 
            * supraincarca metoda str

        Returns:
            * str:    un string ce va contine informatiile
                      specifice frigiderului (nume, energy label)
                    
        """
        # Supraincarcam metoda str pentru a returna string-ul de care avem nevoie
        return "Enjoy fresh food with {}, energy label {}.".format(self.name, self.energy_label)