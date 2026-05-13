 
from pygame import *
import random
from time import time as timer
#crear ventana de juego
window=display.set_mode((700,500))
display.set_caption('pygame_window')
fondo=transform.scale(image.load('galaxy.jpg'), (700,500))

game=True




# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
      def __init__ (self, player_image, player_speed, player_x, player_y, size_x, size_y):
            super().__init__()
            self.image=transform.scale(image.load(player_image),(size_x, size_y))
            self.speed= player_speed
            self.rect= self.image.get_rect()
            self.rect.x= player_x
            self.rect.y= player_y
            
      def reset(self):
            window.blit(self.image, (self.rect.x,self.rect.y))


    # método que dibuja al personaje en la ventana

class Bullet(GameSprite):
      def update(self):
            self.rect.y = self.rect.y-10
            if self.rect.y <= -10000:
                  self.kill()
# clase del jugador principal
bullets=sprite.Group()
class Player(GameSprite):
          
      
      def move(self):
    
               
            coso=key.get_pressed()
      

            if coso[K_LEFT]:
                  self.rect.x=self.rect.x-15
      
      
      
      
            if coso[K_RIGHT]:
                  self.rect.x=self.rect.x+15
      def fire(self):
            bullet=Bullet('bullet.png',-15, self.rect.centerx, self.rect.top, 15, 40)
            bullets.add(bullet)

a=0
class Enemy(GameSprite):
      
     
  
      def update(self):
            w=random.randint(1, 2)
            self.rect.y= self.rect.y + w
            global a
            if self.rect.y >= 500:
                  self.rect.y = -10
                  self.rect.x = random.randint(1, 600)
                  a=a+1
                  


grupo1=sprite.Group()



aaa=900
e1 = Enemy('ufo.png', 2, 100, -100, 100, 50)
e2 = Enemy('ufo.png', 2, 300, -10, 100, 50)
e3= Enemy('ufo.png', 2, 500, -70, 100, 50)
e4 = Enemy('ufo.png', 2, 200, -30, 100, 50)
e5= Enemy('ufo.png', 2, 460, -40, 100, 50)
balnco=(255, 255, 255)
grupo1.add(e1, e2, e3, e4, e5)

font.init()
font=font.SysFont(None, 30) 




meteorito=Enemy('images.png', 2, 100, 100, 100, 100)


k2=0


def aas_perdio():
      if a>=1000:
            global game
            game=False
            texto3 = font.render("q malo", True, balnco)
            window.blit(texto3, (200,200))
      if sprite.collide_rect(meteorito, jugador):   
            game=False
      if sprite.spritecollide(jugador, grupo1, True):
            game=False
clock=time.Clock()
jugador = Player('rocket.png', 500, 500, 450, 100, 50)
ls =0
cooldown=2 
balass=5
recarga = False   
while game:
      texto1 = font.render("fallados:"+str(a), True, balnco)
      texto2 = font.render("nose_q_va_aqui:"+str(k2), True, balnco)
      
      for e in event.get():
            if e.type == QUIT:
                  game=False
            elif e.type==KEYDOWN:
                  if e.key==K_SPACE and not recarga:
                       
                        jugador.fire()
                        balass=balass-1 
                  if balass==0 and not recarga:
                        recarga=True
                        ls=timer()
      if recarga:
            if balass==0:
                  if timer() - ls > cooldown:
                        balass=balass+5
                        recarga=False

                               
            
                              
      collides=sprite.groupcollide(grupo1, bullets, True, True)
 
      

     
      for c in collides:

            k2=k2+1
            monster=Enemy('ufo.png',2, random.randint(1, 420), -100, 100, 50)
            grupo1.add(monster)
            print('hola')
      aaa=aaa+200
      window.blit(fondo,(0,0))
      
      window.blit(texto1, (0,0))
      window.blit(texto2, (0,40))
      jugador.reset()
      jugador.move()
      meteorito.reset()
      meteorito.update()
      clock.tick(60)

      aas_perdio()
     
      grupo1.draw(window)
      bullets.update()
      bullets.draw(window)
      grupo1.update()
      display.update()
          