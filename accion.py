from turtle import Screen, Turtle
import math

pantalla = Screen()
canicaDos = Turtle()
canicaDos.speed(0.6)
canicaUno = Turtle()
canicaUno.speed(0.6)
canicaDos.screen.title("Proyecto Maquina de Goldberg")


canicaUno.penup()
canicaUno.goto(-100,100)
canicaUno.pendown()
canicaUno.write("Canica N° 1")

canicaDos.penup()
canicaDos.goto(100,100)
canicaDos.pendown()
canicaDos.write("Canica N° 2")


def movCanicaUno():
    canicaUno.right(10)
    canicaUno.forward(60)
    canicaUno.write("   caida 1")
    canicaUno.right(80)
    canicaUno.forward(140)
    canicaUno.right(90)
    canicaUno.forward(100)
    canicaUno.left(90)
    canicaUno.forward(35)
    canicaUno.left(45)
    canicaUno.forward(40)


def movCanicaDos():
    ##1
    canicaDos.right(90)
    canicaDos.forward(30)
    canicaDos.write("   caida 1")

    ##2
    canicaDos.left(77)
    canicaDos.forward(50)
    canicaDos.right(77)
    canicaDos.forward(30)
    canicaDos.write("   caida 2")
    ##3
    canicaDos.right(77)
    canicaDos.forward(50)
    canicaDos.left(77)
    canicaDos.forward(30)
    canicaDos.write("   caida 3")
    ##4
    canicaDos.left(77)
    canicaDos.forward(50)
    canicaDos.right(77)
    canicaDos.forward(70)
    canicaDos.write("   caida 4")



movCanicaUno()
movCanicaDos()

pantalla.exitonclick()