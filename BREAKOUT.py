import pygame
pygame.init()

import random

screen = pygame.display.set_mode ((1920,1080))
pygame.display.set_caption("breakout")


doExit = False

clock = pygame.time.Clock()
#player postitions
p1x = 960
p1y = 800

#ball variables
bx = 350
by = 250
bVx = 5
bVy = 5

class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100, 250), random.randrange(100, 250), random.randrange(100, 250))
        self.isDead = False
        
    def draw(self):
        if self.isDead == False:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100, 50))
        
    def collision(self, bx, by):
        
        if bx < self.xpos+100 and bx +20> self.xpos and by +20 > self.ypos and by < self.ypos + 50 and self.isDead == False:
            print("true collision!")
            return True
        else:
            return False
    def kill(self):
        self.isDead = True
            
            
b1 = brick(50,50)
b2 = brick(150,50)
b3 = brick(250,50)
b4 = brick(350,50)
b5 = brick(450,50)
b6 = brick(550,50)
b7 = brick(650,50)
b8 = brick(750,50)
b9 = brick(850,50)
b10 = brick(950,50)
b11 = brick(1050,50)
b12 = brick(1150,50)
b13 = brick(1250,50)
b14 = brick(1350,50)
b15 = brick(1450,50)
b16 = brick(1550,50)
b17 = brick(1650,50)
b18 = brick(1750,50)
b19 = brick(50,100)
b20 = brick(150,100)
b21 = brick(250,100)
b22 = brick(350,100)
b23 = brick(450,100)
b24 = brick(550,100)
b25 = brick(650,100)
b26 = brick(750,100)
b27 = brick(850,100)
b28 = brick(950,100)
b29 = brick(1050,100)
b30 = brick(1150,100)
b31 = brick(1250,100)
b32 = brick(1350,100)
b33 = brick(1450,100)
b34 = brick(1550,100)
b35 = brick(1650,100)
b36 = brick(1750,100)



    
while not doExit:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
        #game logic here --------------------------------------------------------------------------
    #controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        p1x-=10
    
    if keys[pygame.K_d]:
        p1x+=10
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    
    #ball movement
    bx += bVx
    by += bVy
    #ball wall bounce
    if bx < 0 or bx + 20 > 1920:
        bVx *= -1
    if by < 0: 
        bVy *= -1
    if by > 1080:
        pygame.quit()
        print("Game Over")
    #ball paddle reflection
        
    if bx < p1x + 100 and by + 20 > p1y and by < p1y + 200:
        bVy *= -1
        

        
    if b1.collision(bx, by)==True:
        b1.kill()
        bVy *=-1
    if b2.collision(bx, by)==True:
        b2.kill()
        bVy *=-1
    if b3.collision(bx, by)==True:
        b3.kill()
        bVy *=-1
    if b4.collision(bx, by)==True:
        b4.kill()
        bVy *=-1
    if b5.collision(bx, by)==True:
        b5.kill()
        bVy *=-1
    if b6.collision(bx, by)==True:
        b6.kill()
        bVy *=-1
    if b7.collision(bx, by)==True:
        b7.kill()
        bVy *=-1
    if b8.collision(bx, by)==True:
        b8.kill()
        bVy *=-1
    if b9.collision(bx, by)==True:
        b9.kill()
        bVy *=-1
    if b10.collision(bx, by)==True:
        b10.kill()
        bVy *=-1
    if b11.collision(bx, by)==True:
        b11.kill()
        bVy *=-1
    if b12.collision(bx, by)==True:
        b12.kill()
        bVy *=-1
    if b13.collision(bx, by)==True:
        b13.kill()
        bVy *=-1
    if b14.collision(bx, by)==True:
        b14.kill()
        bVy *=-1
    if b15.collision(bx, by)==True:
        b15.kill()
        bVy *=-1
    if b16.collision(bx, by)==True:
        b16.kill()
        bVy *=-1
    if b17.collision(bx, by)==True:
        b17.kill()
        bVy *=-1
    if b18.collision(bx, by)==True:
        b18.kill()
        bVy *=-1
    if b19.collision(bx, by)==True:
        b19.kill()
        bVy *=-1
    if b20.collision(bx, by)==True:
        b20.kill()
        bVy *=-1
    if b21.collision(bx, by)==True:
        b21.kill()
        bVy *=-1
    if b22.collision(bx, by)==True:
        b22.kill()
        bVy *=-1
    if b23.collision(bx, by)==True:
        b23.kill()
        bVy *=-1
    if b24.collision(bx, by)==True:
        b24.kill()
        bVy *=-1
    if b25.collision(bx, by)==True:
        b25.kill()
        bVy *=-1
    if b26.collision(bx, by)==True:
        b26.kill()
        bVy *=-1
    if b27.collision(bx, by)==True:
        b27.kill()
        bVy *=-1
    if b28.collision(bx, by)==True:
        b28.kill()
        bVy *=-1
    if b29.collision(bx, by)==True:
        b29.kill()
        bVy *=-1
    if b30.collision(bx, by)==True:
        b30.kill()
        bVy *=-1
    if b31.collision(bx, by)==True:
        b31.kill()
        bVy *=-1
    if b32.collision(bx, by)==True:
        b32.kill()
        bVy *=-1
    if b33.collision(bx, by)==True:
        b33.kill()
        bVy *=-1
    if b34.collision(bx, by)==True:
        b34.kill()
        bVy *=-1
    if b35.collision(bx, by)==True:
        b35.kill()
        bVy *=-1
    if b36.collision(bx, by)==True:
        b36.kill()
        bVy *=-1
        
    
    #if collision() True:
    #    bVy *= -1

        
    
        #render section here -----------------------------------------------------------------------
    screen.fill ((0,0,0))
            

    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()
    b11.draw()
    b12.draw()
    b13.draw()
    b14.draw()
    b15.draw()
    b16.draw()
    b17.draw()
    b18.draw()
    b19.draw()
    b20.draw()
    b21.draw()
    b22.draw()
    b23.draw()
    b24.draw()
    b25.draw()
    b26.draw()
    b27.draw()
    b28.draw()
    b29.draw()
    b30.draw()
    b31.draw()
    b32.draw()
    b33.draw()
    b34.draw()
    b35.draw()
    b36.draw()
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 100, 20), 1)

    pygame.draw.rect(screen, (255, 255, 255), (bx, by, 20, 20), 1)
    

            
    pygame.display.flip()