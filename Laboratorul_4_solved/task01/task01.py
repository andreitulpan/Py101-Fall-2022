import random as rd
import math

def random_points(radius, x_center, y_center):
    r = math.sqrt((radius**2) * rd.random())
    # avem nevoie de un unghi dintr-un cerc, deci vom inmulti cu 2 * pi un numar
    # random, care va ajunge tot in intervalul 0-2pi deoarece daca numarul e mai
    # mare de 2 pi, putem scadea din acel nr 2 pi si il reducem.
    # eg: 2pi * 2 inseamna tot 2pi
    theta = 2 * math.pi * rd.random()   
    # returnam o lista cu cele doua componente     
    return [x_center + r * math.cos(theta), y_center + r * math.sin(theta)]