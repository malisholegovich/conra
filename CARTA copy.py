import pygame
import random
pygame.init()
 
W = 1500
H = 900
 
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("contra")



WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK=(0,0,0)
 
FPS =30      # число кадров в секунду
clock = pygame.time.Clock()



class Block(pygame.sprite.Sprite):
    def __init__(self,W,H,X,Y,zvet):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((W, H))
        self.image.fill(zvet)
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
class NPC(pygame.sprite.Sprite):
    def __init__(self,W,H,X,Y,stolk,moment,speed,jump_now,jump_force):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((W, H))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y 
        self.stolk=stolk
        self.moment=moment  
        self.speed=speed 
        self.jump_now=jump_now
        self.jump_force=jump_force
class Turel(pygame.sprite.Sprite):
    def __init__(self,W,H,X,Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((W, H))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
        
    def update(self):
        self.rect.x-=10
class PulaT(pygame.sprite.Sprite):
    def __init__(self,W,H,X,Y,k):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((W, H))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
        self.polozenie=k
                
        

block1=Block(150000,10,0,830,BLUE)

block2=Block(4400,10,200,650,GREEN)

block3=Block(600,10, 800, 740,GREEN)

block4=Block(200,10,1400,780,GREEN )

block5=Block(400,10,1600,830,GREEN)

block6=Block(200,10,2000,780,GREEN)

block7=Block(400,10,2400,740,GREEN)

block8=Block(400,10,3600,830, GREEN) 

block9=Block(600,10,3800,740,GREEN)
# cherez 800 5400

block10=Block(1000,10,5400,650,GREEN) 
# most



block11=Block(1600,10,7400,650,GREEN)

block12=Block(600,10,8800,830,GREEN)


block13=Block(3200,10,8600,590,GREEN)
# samiy verh

block14=Block(400,10,9400,740,GREEN)

block15=Block(1400,10,10000,700,GREEN)

block16=Block(1200,10,10800,830,GREEN)

block17=Block(1400,10,11600,650,GREEN)

block18=Block(400,10,12000,770,GREEN)

block19=Block(400,10,12600,770,GREEN)

block20=Block(400,10,13200,770,GREEN)





all_sprites = pygame.sprite.Group()
all_pula = pygame.sprite.Group()
all_npc=pygame.sprite.Group()
all_pulat=pygame.sprite.Group()
all_turel=pygame.sprite.Group()
npc=NPC(40,50,1200,711,1,False,10,0,0)
npc1=NPC(40,50,1300,711,1,False,10,0,0)
npc2=NPC(40,50,1100,711,1,False,10,0,0)
turel=Turel(100,100,750,510)
all_npc.add(npc,npc1,npc2)
all_sprites.add(block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,block15,block16,block17,block18,block19,block20)
all_turel.add(turel)







 
hero = pygame.image.load('hero1.png')
rect = hero.get_rect(centerx=W//2)

rect.bottom = block2.rect.top+1
rect.x=block2.rect.topleft[0]



moment=False
jump_count=20
jump_now=0



speed_npc=5














t=0        
u=1
vesomost=1 
mozno=0
polet=False
polozenie=0
fps_count=0
fps_count_for_turel=0
mozet=0
smert=1
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                mozet=True
            if event.key==pygame.K_SPACE and mozno==0:
                if mozet==True:
                    rect.y+=10
                    mozet=False
                else:
                    moment=True
            if event.key==pygame.K_DOWN and mozet==1 and moment==False:
                rect
            if event.key==pygame.K_w and fps_count>15:
                pula=Pula(10,10,rect.center[0],rect.center[1],polozenie)
                all_pula.add(pula)    
                polet=True
                fps_count=0
            if event.key==pygame.K_r:
                all_npc=pygame.sprite.Group()
                npc=NPC(40,50,1200,711,1,False,10,0,0)
                npc1=NPC(40,50,1300,711,1,False,10,0,0)
                npc2=NPC(40,50,1100,711,1,False,10,0,0)
                all_npc.add(npc,npc1,npc2)
            
        
    keys=pygame.key.get_pressed()
    
    
    if fps_count_for_turel>=30:
        for i in all_turel:
            if rect.x<i.rect.bottomleft[0] and rect.y>i.rect.bottomleft[1]:
                pula=PulaT(10,10,i.rect.center[0],i.rect.center[1],0)
                all_pulat.add(pula)
        fps_count_for_turel=0
        
    for i in all_pulat:
        if i.polozenie==0:
            i.rect.x-=20
            i.rect.y+=20        
            
    
    
    for i in all_npc:
        i.speed=10        
    if keys[pygame.K_RIGHT]:
        hero = pygame.image.load('hero1.png')
        polozenie=0
        if rect.center[0]==W//2:
            for i in all_npc:
                if i.stolk==1:
                    i.speed=20
                else:
                    
                    i.speed=0
            all_sprites.update()
            all_turel.update()
        else:
            rect.x+=10
            
            
    
    if keys[pygame.K_LEFT]:
        polozenie=1
        rect.x-=10
        hero = pygame.image.load('hero2.png')
        
        for i in all_npc:
            i.speed=10
            
    if keys[pygame.K_TAB]:
        FPS=60 
    else:
        FPS=30       
            
            
    if polet==True :
        for i in all_pula:
            if i.polozenie==0:
                i.rect.x+=20
            if i.polozenie==1:
                i.rect.x-=20
     
        
        
           
    
    
    
    
    if moment is True:

        
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

    else:
        vesomost=0
        mozno=0


    for i in all_npc:
        for ii in all_sprites:
            if pygame.Rect.colliderect(i.rect,ii.rect) and ii.rect.top==i.rect.bottom-1:
                i.moment=False
                i.jump_now=0
                
            
                
                
            if ((i.rect.bottomleft[0]==ii.rect.topleft[0] and i.rect.bottomleft[1]==ii.rect.topleft[1]+1) or (i.rect.bottomright[0]==ii.rect.topright[0] and i.rect.bottomright[1]==ii.rect.topright[1]+1)) :
                u1=random.randint(0,1)
                
                if u1==0 and i.stolk==1:
                    i.moment=True
                    i.jump_force=random.randint(5,15)
                else:
                    i.stolk=1
                if u1==1:
                    
                    if i.rect.bottomleft[0]==ii.rect.topleft[0] and i.rect.bottomleft[1]==ii.rect.topleft[1]+1:
                        i.stolk=0 
                    if i.rect.bottomright[0]==ii.rect.topright[0] and i.rect.bottomright[1]==ii.rect.topright[1]+1:
                        i.stolk=1
    for i in all_npc:
        if i.stolk==0:
            i.rect.x+=i.speed
        elif i.stolk==1:
            i.rect.x-=i.speed
    for i in all_npc:        
        if i.moment==True:
            if i.jump_now<=i.jump_force:
                
                i.rect.y-=10
                i.jump_now+=1
            else:
                i.rect.y+=10
        if pygame.Rect.colliderect(i.rect,rect):
            smert=0
        if i.rect.x<-40:
            i.kill()    
    for i in all_npc:
        for ii in all_pula:
            if pygame.Rect.colliderect(i.rect,ii.rect):
                i.kill()
                ii.kill()            
                
    for i in all_pula:
        if i.rect.x<-10 or i.rect.x>1510:
            i.kill()

    sc.fill(WHITE)
    all_sprites.draw(sc)
    all_pula.draw(sc)
    all_npc.draw(sc)
    all_turel.draw(sc)
    all_pulat.draw(sc)
    if smert==1:
        sc.blit(hero, rect)
    pygame.display.update()
    fps_count+=1
    fps_count_for_turel+=1
    
    clock.tick(FPS)