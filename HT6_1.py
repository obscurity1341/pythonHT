# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math
class Triangle ():
    def _init_(self, ax, ay,bx, by, cx, cy):
        self.ax = ax,
        self.ay = ay,
        self.bx = bx,
        self.by = by,
        self.cx = cx,
        self.cy = cy,
        self.AB = math.sqrt(int(math.fabs((ax-bx)**2+(ay - by)**2))),
        self.BC = math.sqrt(int((bx-cx)**2+(by-cy)**2)),
        self.AC = math.sqrt(int((ax-cx)**2 + (ay - cy)**2)),

    def peri(self):
        return self.AB + self.AC + self.BC

    def height(self):
        self.peri /= 2
        self.height = 2*sqrt(int(self.peri * (self.peri - self.AB) * (self.peri - self.BC) * (self.peri - self.AC)))/self.AC
        return self.height

    def square(self):
        return 1/2 * self.AC * self.height


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math
class Trapeze() :
    def __init__(self,ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax,
        self.ay = ay,
        self.bx = bx,
        self.by = by,
        self.cx = cx,
        self.cy = cy,
        self.dx = dx,
        self.dy = dy,


    def check(self):
        AC = math.sqrt(int((ax-cx)**2 + (ay -cy)**2))
        BD = math.sqrt(int((bx - dx)**2 + (by - dy)**2))
        if AC == BD:
            return "ОК"
        else:
            return "Error"

    def lengths(self):
        self.AB = math.sqrt(int((ax - bx) ** 2 + (ay - by) ** 2)),
        self.BC = math.sqrt(int((bx - cx) ** 2 + (by - cy) ** 2)),
        self.CD = math.sqrt(int((dx - cx) ** 2 + (dy - cy) ** 2)),
        self.AD = math.sqrt(int((dx - ax) ** 2 + (dy - ay) ** 2)),

    def square(self):
        s = ((self.AB + self.BC)/2) * (math.sqrt((self.CD**2)-((((self.BC - self.AB)**2) + (self.CD)**2) - (self.AD)**2))/(2*(self.BC - self.AB)))
        return s
    def perime(self):
        p = self.AB + self.BC + self.CD + self.AD
        return p