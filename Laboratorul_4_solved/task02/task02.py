class Image():
    def __init__(self, format='P3', rows=0, columns=0, max_value=255, pixels=[[]]):
        self.format = format
        self.rows = rows
        self.columns = columns
        self.max_value = max_value
        self.pixels = pixels
    def __str__(self):
        # use this for debugging
        image = ""
        image += f"{self.format}{self.rows} {self.columns}\n{self.max_value}\n"
        for i in range(self.rows):
            for j in range(3 * self.columns):
                image += f"{self.pixels[i][j]} "
            image += "\n"
        return image
    def sepia(self):
        # parcurgem matricea de pixeli, tinand cont de numarul de coloane
        for i in range(0, self.rows):
            for j in range(0, 3 * self.columns, 3):
                # folosim 3 variabile pentru a nu altera imaginea
                r = self.pixels[i][j]
                g = self.pixels[i][j + 1]
                b = self.pixels[i][j + 2]
                # aplicam transformarile pe alte 3 variabile
                sepia_r = (int)(0.393*r + 0.769*g + 0.189*b)
                sepia_g = (int)(0.349*r + 0.686*g + 0.168*b)
                sepia_b = (int)(0.272*r + 0.534*g + 0.131*b)
                # tinem cont de cazurile in care un canal depaseste valoarea maxima
                # astfel ii atribuim valoarea maxima
                if sepia_r > 255:
                    sepia_r = 255
                if sepia_b > 255:
                    sepia_b = 255
                if sepia_g > 255:
                    sepia_g = 255
                # adaugam in imaginea originala filtrul aplicat
                self.pixels[i][j] = sepia_r
                self.pixels[i][j + 1] = sepia_g
                self.pixels[i][j + 2] = sepia_b
    def read(self, filename):
        # deschidem fisierul. o alta varianta ar fi sa folositi with open:, care
        # inchide automat fisierul la final
        file = open(filename, 'r')
        # formatul este de forma P3, deci vom avea nevoie de toata linia
        self.format = file.readline()
        # citim urmatoarea linie si vom obtine ceva de forna "n m"
        line = file.readline()
        # folosim line[0] deoarece reprezinta n, iar line[2] m. line[1] este spatiu
        self.rows = int(line[0])
        self.columns = int(line[2])
        # citim urmatoarea linie si obtinem max_value, dar este un string
        # folosim int ca sa obtinem un int pentru a lucra mai usor cu el
        line = file.readline()
        self.max_value = int(line)
        # initializam matricea de pixeli care e de forma (pentru n = 2, m = 3)
        # 0 0 0 0 0 0 0 0 0
        # 1 1 1 1 1 1 1 1 1
        # 3 elemente consecutive de pe o linie reprezinta un pixel
        self.pixels = [[0] * 3 * self.columns for i in range(self.rows)]
        i = 0
        while i < self.rows:
            # citim linie cu linie datele din matrice
            line = file.readline()
            j = 0
            # folosim line split pentru a obtine o lista fara spatii, astfel
            # putem folosi un contor fara sa ne complicam cu posibile spatii in lista
            list = line.split()
            # tinem cont ca numarul de coloane este columns * 3 (dimensiunea unui pixel)
            while j < 3 * self.columns:
                # adaugam in lista de pixeli valoarea efectiva
                self.pixels[i][j] = int(list[j])
                j = j + 1
            i = i + 1
        # inchidem fisierul
        file.close()
    def write(self, filename):
        # asemanator cu read, deschidem fisierul si il inchidem la final
        file = open(filename, 'w')
        # adaugam in lines toate liniile corespunzatoare
        lines = []
        # format
        lines.append(f"{self.format}")
        # numarul de linii, respectiv coloane
        lines.append(f"{self.rows} {self.columns}\n")
        # max_value
        lines.append(f"{self.max_value}\n")
        i = 0
        while i < self.rows:
            j = 0
            # folosim cate un string pentru fiecare linie a matricei
            line = ""
            while j < 3 * self.columns:
                # adaugam valorile din matrice
                line += f"{self.pixels[i][j]} "
                j =  j + 1
            # nu uitam de endline
            line += "\n"
            # adaugam in stringul ce va fi scris in fisier
            lines.append(line)
            i = i + 1
        # writelines va scrie continutul stringului in fisier
        file.writelines(lines)
        file.close()