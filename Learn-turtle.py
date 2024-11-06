import turtle

class Triangle:
    def __init__(self, n):
        self.n = n

    def triangle1(self):
        for i in range(3):
            turtle.forward(self.n)
            turtle.left(120)

    def triangle2(self):
        for i in range(3):
            turtle.forward(self.n)
            turtle.right(120)

    def triangle3(self, angle):
        turtle.setheading(angle)
        for i in range(3):
            turtle.forward(self.n)
            turtle.left(120)

class Carre:
    def __init__(self, a):
        self.a = a

    def carre(self):
        for i in range(4):
            turtle.forward(self.a)
            turtle.right(90)

    def ligne_de_carres(self, n):
        for i in range(n):
            self.carre()
            turtle.penup()
            turtle.forward(self.a + 5)
            turtle.pendown()

    def carres_croissants(self, n):
        current_size = self.a
        for i in range(n):
            carre = Carre(current_size)
            carre.carre()
            turtle.penup()
            turtle.forward(current_size * 1.25)
            turtle.pendown()
            current_size *= 1.25

class FiguresPleines:
    def __init__(self, repetitions, taille):
        self.repetitions = repetitions
        self.taille = taille

    def dessiner(self):
        for i in range(self.repetitions):
            turtle.color("purple", "orange")
            turtle.begin_fill()
            triangle = Triangle(self.taille)
            triangle.triangle1()
            turtle.end_fill()

            turtle.penup()
            turtle.forward(self.taille * 1.25)
            turtle.pendown()
            turtle.begin_fill()
            carre = Carre(self.taille)
            carre.carre()
            turtle.end_fill()

            turtle.penup()
            turtle.forward(self.taille * 1.25)
            turtle.pendown()

class Etoile:
    def __init__(self, a, n):
        self.a = a
        self.n = n

    def etoile(self):
        angle = 180 - (180 / self.n)
        for i in range(self.n):
            turtle.forward(self.a)
            turtle.right(angle)

   
def polygone(cotes, longueur):
        angle_interieur = 360 / cotes
        for i in range(cotes):
            turtle.forward(longueur)
            turtle.left(angle_interieur)

turtle.done()