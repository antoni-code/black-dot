import pygame
pygame.init()

#global variables
screen = pygame.display.set_mode([500,500])
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
yellow = (255,255,0)
black = (0,0,0)

screen.fill(white)

class myCircle():
    def __init__(self,color,pos,rad,wid=0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.scrn = screen

    def draw(self):
        pygame.draw.circle(self.scrn,self.color,self.pos,self.rad,self.wid)

    def grow(self,x):
        self.rad  += x
        pygame.draw.circle(self.scrn,self.color,self.pos,self.rad,self.wid)

#how do draw a circle
position = (300,300)
radius = 50
wid = 2
pygame.draw.circle(screen,red,position,radius,wid)
pygame.display.update()

#creating instances
blueCircles = myCircle(blue,position,radius+60)
redCircles = myCircle(red,position,radius+40)
yellowCircles = myCircle(yellow,position,radius,5)
greenCircles = myCircle(green,position,20)

while (1):
    for event in pygame.event.get():
        if (event.type==pygame.MOUSEBUTTONDOWN):
            blueCircles.draw()
            redCircles.draw()
            yellowCircles.draw()
            greenCircles.draw()
            pygame.display.update()

        elif(event.type==pygame.MOUSEBUTTONUP):
            blueCircles.grow(2)
            redCircles.grow(2)
            yellowCircles.grow(2)
            greenCircles.grow(2)
            pygame.display.update()

        elif (event.type ==pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackCircle = myCircle(black,pos,5)
            blackCircle.draw()
            pygame.display.update()  

     
