from ponto import *

class Retangulo:
    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def calc_perimetro(self):
        ab = Ponto.calc_dist_entre_pontos(self._a, self._b)
        bc = Ponto.calc_dist_entre_pontos(self._b, self._c)
        cd = Ponto.calc_dist_entre_pontos(self._c, self._d)
        da = Ponto.calc_dist_entre_pontos(self._d, self._a)
        return ab + bc + cd + da

    def calc_area(self):
        ab = Ponto.calc_dist_entre_pontos(self._a, self._b)
        bc = Ponto.calc_dist_entre_pontos(self._b, self._c)
        return ab * bc
