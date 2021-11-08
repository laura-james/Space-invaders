

class Alien:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.dir = "left"
  
  def draw(self):
    pygame.draw.rect(screen,WHITE,[self.x, self.y, 30,30],5)
  
  def move(self,speed):
    #self.x = self.x + speed
    if self.x > 500 - 30:
      self.dir="left"
      self.y = self.y + 30
    if self.x < 0:
      self.dir="right"
      self.y = self.y + 30

    if self.dir == "right":
      self.x = self.x + speed
    if self.dir == "left":
      self.x = self.x - speed
      


import pygame
pygame.init()
BLACK   = (0,0,0)
WHITE   = (255,255,255)
GREEN   = (0,255,0)
RED     = (255,0,0)
BLUE    = (0,0,255)

size    =[500,500]
screen  = pygame.display.set_mode(size)

pygame.display.set_caption("space invaderz")

clock=pygame.time.Clock()

done=False
#instantiate the aliens
bob = Alien(3,10)
ryan = Alien(300,10)
joanna = Alien(200,400)

aliens = []
for i in range(8):
  aliens.append(Alien(i*60,20))

#----------------- MAIN GAME LOOP START----------------------------
while done==False:

#----------------- CHECK FOR EVENTS START--------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True


#----------------- CHECK FOR EVENTS END----------------------------

#----------------- GAME LOGIC START--------------------------------

#----------------- GAME LOGIC END ---------------------------------

#----------------- DRAWING START-----------------------------------
    screen.fill(BLACK) # starts off with a BLACK screen

    bob.move(15)
    
    bob.draw()    
    ryan.draw()    
    joanna.draw()
    for i in range(8):
      aliens[i].move(5)
      aliens[i].draw()

    

    #pygame.draw.ellipse(screen,RED,[120,120, 250,200],5)


    pygame.display.flip() # have to flip the display to show result

#----------------- DRAWING END-------------------------------------

    # limit to 20 frames per second
    clock.tick(20)
#----------------- MAIN GAME LOOP END ----------------------------
pygame.quit()