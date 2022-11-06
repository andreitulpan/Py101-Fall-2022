
class Complex:

    def __init__(self, real_part: int = 0, imaginary_part: int = 0, var_name: str = 'var') -> None:
        # Initializam campurile
        self.real_part = real_part
        self.imaginary_part = imaginary_part
        self.var_name = var_name

    def __str__(self) -> str:
        # Tinem minte valoarea initiala
        tmp = self.imaginary_part
        # Rezultatul
        ret_string = ""
        # Pentru a putea manipula mai usor string-ul final, facem partea
        # imaginara pozitiva si ii adaugam caracterul - in rezultat
        if self.imaginary_part < 0:
            self.imaginary_part *= -1
        
        # x = y = 0
        if tmp == 0 and self.real_part == 0:
            ret_string = f"{self.var_name} = 0"
        elif self.real_part == 0: # x = 0
            if tmp < 0: # y negativ de forma -yi
                ret_string = f"{self.var_name} = -{self.imaginary_part}i"
            else: # y pozitiv de forma yi
                ret_string = f"{self.var_name} = {self.imaginary_part}i"
        elif tmp == 0: # x != 0 si y = 0, de forma x + 0i = x
            ret_string = f"{self.var_name} = {self.real_part}"
        elif tmp < 0: # x - yi
            ret_string = f"{self.var_name} = {self.real_part} - {self.imaginary_part}i"
        else: # x + yi
            ret_string =  f"{self.var_name} = {self.real_part} + {self.imaginary_part}i"

        # Avem nevoie sa cunoastem modificarile
        self.imaginary_part = tmp
        return ret_string

    def add_complex_numbers(self, other) -> None:
        # Adunare parte reala - parte reala, parte imaginara - parte imaginara
        self.real_part += other.real_part
        self.imaginary_part += other.imaginary_part

    def substract_complex_numbers(self, other) -> None:
        # Scadere parte reala - parte reala, parte imaginara - parte imaginara
        self.real_part -= other.real_part
        self.imaginary_part -= other.imaginary_part

    def multiply_complex_numbers(self, other) -> None:
        
        """
        We know you all love Math. :)
        """
        # Avem nevoie de variabile pentru a nu altera campurile numarului complex
        old_real_part_self = self.real_part
        old_img_part_self = self.imaginary_part

        old_real_part_other = other.real_part
        old_img_part_other = other.imaginary_part
        # (x + yi) * (a + bi) = x * a - y * b
        self.real_part = self.real_part * other.real_part - \
                    self.imaginary_part * other.imaginary_part
        # (x + yi) * (a + bi) = x * b + y * a
        self.imaginary_part = old_real_part_self * old_img_part_other + \
                        old_img_part_self * old_real_part_other
