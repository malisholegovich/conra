import pygame
 
pygame.init()
 
W = 1500
H = 900
 
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("contra")

 
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
FPS =30        # число кадров в секунду
clock = pygame.time.Clock()



class Turret(pygame.sprite.Sprite):
    def __init__(self,X,Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
    def update(self):
        self.rect.x-=10
    def shot(self,u,l):
        xx = self.rect.x
        yy = self.rect.y
        xx1 = u
        yy1 = l
        a1 = abs(xx1-xx)
        b1 = abs(yy1-yy)
        z = (a1**2+b1**2)**0.5
        a = 10*a1/z
        b = 10*b1/z
        if shot_count >=90:
            newbullet = TurretBullet(xx,yy,a,b)
            all_bullet.add(newbullet)
            shot_count = 0

class TurretBullet(pygame.sprite.Sprite):
    def __init__(self,X,Y,a,b):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
        self.a = a
        self.b = b
class Block(pygame.sprite.Sprite):
    def __init__(self,W,H,X,Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((W, H))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
    def update(self):
        self.rect.x-=10
class Pula(pygame.sprite.Sprite):
    def __init__(self,W,H,X,Y,k):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((W, H))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
        self.polozenie=k
    
    
block1=Block(100,10,1500//2,760)
block2=Block(100,10,750,710)
block3=Block(150000,10,0,830)
block4=Block(100,10,750,610)
block5=Block(100,10,1500,760)
turret1=Turret(W//2,H//2)


all_sprites = pygame.sprite.Group()
all_pula = pygame.sprite.Group()
all_turret = pygame.sprite.Group()
all_bullet = pygame.sprite.Group()
all_sprites.add(block1,block2,block3,block4,block5)
all_turret.add(turret1)





 
hero = pygame.Surface((40, 50))                        #в этой части я создаю героя и присваиваю ему нижние координаты, как координаты земли
hero.fill(BLUE)
rect = hero.get_rect(centerx=W//2)

rect.bottom = H-69



moment=False                    #часть для прыжка
jump_count=20
jump_now=0


t=0        
u=1
vesomost=1 
mozno=0
polet=False
polozenie=1
fps_count=0
shot_count = 0
mozet=0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and mozno==0:
                if mozet==True:
                    rect.y+=10
                else:
                    moment=True
            
            if event.key==pygame.K_w and fps_count>15:
                pula=Pula(10,10,rect.center[0],rect.center[1],polozenie)
                all_pula.add(pula)
                
                polet=True
                fps_count=0
            
        
    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        mozet = True
    else:
        mozet = False
        
        
    if keys[pygame.K_RIGHT]:
        
        if rect.center[0]==W//2:
            all_sprites.update()
            all_turret.update()
        else:
            rect.x+=10
          
    if keys[pygame.K_LEFT]:
        rect.x-=10
      
    if keys[pygame.K_RIGHT]:
        polozenie = 1
    if keys[pygame.K_UP]:
        polozenie = 3
    if keys[pygame.K_LEFT]:
        polozenie = 5
    if keys[pygame.K_DOWN]:
        polozenie = 7
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        polozenie = 2
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        polozenie = 4
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        polozenie = 6
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        polozenie = 8
    for i in all_bullet:
        i.shot(rect.x,rect.y)
    if polet==True :
        for i in all_pula:
            if i.polozenie==1:
                i.rect.x+=20
            elif i.polozenie==2:
                i.rect.x+=20
                i.rect.y-=20
            elif i.polozenie==3:
                i.rect.y-=20
            elif i.polozenie==4:
                i.rect.x-=20
                i.rect.y-=20
            elif i.polozenie==5:
                i.rect.x-=20
            elif i.polozenie==6:
                i.rect.x-=20
                i.rect.y+=20
            elif i.polozenie==7:
                i.rect.y+=20
            elif i.polozenie==8:
                i.rect.x+=20
                i.rect.y+=20
        
    for i in all_bullet:
        i.rect.x+=i.a
        i.rect.y+=i.b
     


        
           
    
    
    
    
    if moment is True:
        hero.fill(GREEN)
        
        if jump_now<=jump_count/2:
            if u==1:
                rect.y-=11
                u=0
            else:
                rect.y-=10
            jump_now+=1
        elif jump_now<=jump_count:
            
            
            
            rect.y+=10
            
            for i in all_sprites:
                if i.rect.top==rect.bottom :
                    rect.y+=1
                    jump_now=0
                    moment=False
                    u=1
                    
        
    for i in all_sprites:
        if pygame.Rect.colliderect(rect,i.rect) and i.rect.top==rect.bottom-1:
            vesomost=1
            
    if vesomost==0 and moment==False:
        rect.y+=10
        mozno=1
        hero.fill(GREEN)
    else:
        vesomost=0
        mozno=0
        if moment==False:
            hero.fill(BLUE)
            
        
               
        
        
    
               
                
                
 
    
    
    sc.fill(WHITE)
    all_sprites.draw(sc)
    all_pula.draw(sc)
    all_turret.draw(sc)
    all_bullet.draw(sc)
    sc.blit(hero, rect)
    pygame.display.update()
    shot_count+=1
    fps_count+=1
    print(fps_count)
    print(shot_count)
 
    clock.tick(FPS)
