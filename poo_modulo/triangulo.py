from ponto import *
import math

class Triangulo:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def calc_lado(self, p1, p2):
        return Ponto.calc_dist_entre_pontos(p1, p2)

    def calc_area(self):
        a = self.calc_lado(self._a, self._b)
        b = self.calc_lado(self._b, self._c)
        c = self.calc_lado(self._c, self._a)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def verifica(self):
        a = self.calc_lado(self._a, self._b)
        b = self.calc_lado(self._b, self._c)
        c = self.calc_lado(self._c, self._a)
        
        if a != b and a != c and b != c:
            return "escaleno"
        elif a == b and a == c:
            return "equilátero"
        else:
            return "isósceles"
