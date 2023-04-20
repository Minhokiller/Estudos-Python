from turtle import Turtle

class Campo(Turtle):
    def __init__(self):
        super().__init__()
        self.Principal()
        self.Linha_meio()
        self.Meio_campo()
        self.Area_cima()
        self.Area_baixo()
        self.Marcas(370,-370)
        self.hideturtle()
    def Principal(self):    
        self.penup()
        self.pensize(3)
        self.goto(-200,400)
        self.pendown()
        self.goto(200,400)
        self.goto(200,-400)
        self.goto(-200,-400)
        self.goto(-200,400)
        self.goto(-200,400)
    
    def Linha_meio(self):
        self.penup()
        self.pensize(3)
        self.goto(-200,0)
        self.pendown()
        self.goto(200,0)

    def Meio_campo(self):
        raio = 60
        num_lados = 360
        comprimento_lado = 2 * raio * 3.1415 / num_lados
        self.penup()
        self.pensize(3)
        self.goto(0,-raio)
        self.pendown()
        self.forward(1)
        for i in range (num_lados):
            self.forward(comprimento_lado)
            self.left(360/num_lados)
        self.penup()
    
    def Area_cima(self):
        self.penup()
        self.pensize(3)
        self.goto(-100,400)
        self.pendown()
        self.goto(-100,300)
        self.goto(100,300)
        self.goto(100,400)
        self.penup()
        self.pensize(3)
        self.goto(-50,400)
        self.pendown()
        self.goto(-50,350)
        self.goto(50,350)
        self.goto(50,400)

    def Area_baixo(self):
        self.penup()
        self.pensize(3)
        self.goto(-100,-400)
        self.pendown()
        self.goto(-100,-300)
        self.goto(100,-300)
        self.goto(100,-400)
        self.penup()
        self.pensize(3)
        self.goto(-50,-400)
        self.pendown()
        self.goto(-50,-350)
        self.goto(50,-350)
        self.goto(50,-400) 

    def Marcas(self,x,z):
        self.penup()
        self.pensize(3)
        self.goto(0,x)   
        self.shape('circle')
        self.penup()
        self.pensize(3)
        self.goto(0,0)   
        self.shape('circle')
        self.penup()
        self.pensize(3)
        self.goto(0,z)   
        self.shape('circle')
            
            