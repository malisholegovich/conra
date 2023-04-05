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

FPS =30        # число кадров в секунду
clock = pygame.time.Clock()
hp = pygame.image.load("helth.png")
HP = pygame.transform.scale( hp , (50,50))


class Turret(pygame.sprite.Sprite):
    def __init__(self,X,Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
        self.shot_count = 0
    def update(self):
        self.rect.x-=10
    def shot(self,u,l,):
        self.shot_count += 1
        xx = self.rect.centerx
        yy = self.rect.centery
        xx1 = u
        yy1 = l
        a1 = abs(xx1-xx)
        b1 = abs(yy1-yy)
        if b1 == 0 and a1 == 0:
            a = 0
            b = 0
        elif a1 == 0:
            a = 0
            if yy>yy1:
                b = -10
            else:
                b = 10
        elif b1 == 0:
            b = 0
            if xx1 > xx:
                a = 10
            else:
                a = -10
        else:
            z = ((a1**2)+(b1**2))**0.5
            a = 10*a1/z
            b = 10*b1/z
            if yy>yy1:
                b = b*(-1)
            if xx1 < xx:
                a = a*(-1)
        if self.shot_count == 40:
            newbullet = TurretBullet(xx,yy,a,b)
            all_bullet.add(newbullet)
            self.shot_count = 0

class TurretBullet(pygame.sprite.Sprite):
    def __init__(self,X,Y,a,b):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
        self.a = a
        self.b = b
    def update(self):
        self.rect.x-=10
class Block(pygame.sprite.Sprite):
    def __init__(self,W,H,X,Y,zvet):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((W, H))
        self.image.fill(zvet)
        self.rect = self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
        self.W=W
        self.H=H
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
class PulaK(pygame.sprite.Sprite):
    def __init__(self,W,H,X,Y,speed,jump):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((W, H))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
        self.speed=speed
        self.jump=jump      

block1=Block(150000,10,0,830,BLUE) #11600

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


block13=Block(3200,10,8600,550,GREEN)
# samiy verh

block14=Block(400,10,9400,740,GREEN)

block15=Block(1400,10,10000,700,GREEN)

block16=Block(1200,10,10800,830,GREEN)

block17=Block(2000,10,11600,650,GREEN)

block18=Block(400,10,12000,770,GREEN)

block19=Block(400,10,12600,770,GREEN)

block20=Block(400,10,13200,770,GREEN)

block21=Block(200,10,13800,730,GREEN)

block22=Block(600,10,14200,690,GREEN)

block23=Block(1000,10,13600,550,GREEN)

block24=Block(400,10,14600,630,GREEN)

block25=Block(200,10,15200,830,GREEN)

block26=Block(400,10,15200,630,GREEN)

block27=Block(600,10,15400,740,GREEN)

most=Block(800,10,4600,650,RED)

block28=Block( 400,10, 16000,650 ,GREEN )

block29=Block( 200,10, 16200,830,GREEN )

block30=Block( 200, 10,16400 ,750,GREEN)

block31=Block(400,10,16200,600,GREEN)

block32=Block(400,10,16800,700,GREEN)

block33=Block( 1000,10,17000,750,GREEN)

block34=Block( 600,10,17600,830,GREEN)

block35=Block(400,10,18300,740,GREEN)

block36=Block(400 ,10,18800,650, GREEN)

block37=Block(800,10,19200,600,GREEN)

block38=Block(600,10,19400,690,GREEN)

block39=Block(1500,10,19200,780,GREEN)

block40=Block(200,10,20000,650,GREEN)

block41=Block(200,10,20200,720,GREEN)

most1=Block(1000,10,6400,650,RED)


bashna=Block(900,630,20500,150,BLUE)

# 20700



# turret1=Turret(700,H//1.5)

# turret1=Turret(7800,710)

# turret2=Turret(10200,650)

# turret3=Turret(11400,650)

# turret4=Turret(12800,650)

# turret5=Turret(14400,430)

# turret6=Turret(17800,630)

# turret7=Turret(19000,740)

# turret8=Turret(19800,740)

turret9=Turret(20600,250)


all_npc=pygame.sprite.Group()
npc=NPC(40,50,1500,781,1,False,10,0,0)
npc1=NPC(40,50,1300,781,1,False,10,0,0)
npc2=NPC(40,50,1100,781,1,False,10,0,0)
all_sprites = pygame.sprite.Group()
all_pula = pygame.sprite.Group()
all_turret = pygame.sprite.Group()
all_bullet = pygame.sprite.Group()
all_k=pygame.sprite.Group()
all_sprites.add(block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,block15,block16,block17,block18,block19,block20,block21,block22,block23,block24,block25,block26,block27)
all_sprites.add(most,most1)
all_turret.add(turret9)
all_sprites.add(block28,block29,block30,block31,block32,block33,block34,block35,block36,block37,block38,block39,block40,block41,bashna)
all_npc.add(npc,npc1,npc2)

hero = pygame.image.load('hero1.png')
rect = hero.get_rect(centerx=W//2)

rect.bottom = block2.rect.top+1
rect.x=block2.rect.topleft[0]
rect1=rect[0]
 






moment=False                    #часть для прыжка
jump_count=20
jump_now=0
MaxHealth = 70
Health = 3



t=0        
u=1
vesomost=1 
mozno=0
polet=False
polozenie=1
fps_count=0
shot_count = 0
mozet=0
uniz=0
fps_count_for_most=0
iii=False
mosta=0
konez=False
fps_count_for_t=0


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
            
            if event.key==pygame.K_w and fps_count>5:
                pula=Pula(10,10,rect.center[0],rect.center[1],polozenie)
                all_pula.add(pula)
                
                polet=True
                fps_count=0
            


    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        mozet = True
    else:
        mozet = False



    for i in all_npc:
        i.speed=10        
    if keys[pygame.K_RIGHT]:
        polozenie=0
        if rect.center[0]>=W//2:
            for i in all_npc:
                if i.stolk==1:
                    i.speed=20
                else:
                        
                    i.speed=10

        
        if keys[pygame.K_LEFT]:
            polozenie=1
            rect.x-=10
            
            for i in all_npc:
                i.speed=10

    if keys[pygame.K_RIGHT]:
        hero = pygame.image.load('hero1.png')
        polozenie=0       
        if rect.center[0]>=W//2 and konez==False:
            all_sprites.update()
            all_turret.update()
            all_bullet.update()
        else:
            rect.x+=10
          
    if keys[pygame.K_LEFT]:
        polozenie=1
        rect.x-=10
        hero = pygame.image.load('hero2.png')     

    if keys[pygame.K_TAB]:
        FPS=900
    
    else:
        FPS=30
            
      
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
    for i in all_turret:
        i.shot(rect.centerx,rect.centery)
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
        if i.rect.colliderect(rect):
            i.kill()
            Health = Health-1
            rect.x=1
            rect.y=1
            if Health == 0:
                exit() 


        
           
    
    
    
    
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
            Health = Health-1
            rect.x=1
            rect.y=1
            if Health == 0:
                exit()
            
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








    if most.rect.x<=rect.x-90 and most.W!=0 and uniz==0:
        uniz=1
        most.image = pygame.Surface((most.W-200, most.H))
        most.rect.x+=200
        most.image.fill(RED)
        most.W-=200
        iii=True
    if fps_count_for_most%25==0 and uniz==1 and most.W!=0 and fps_count_for_most>0:
        most.image = pygame.Surface((most.W-200, most.H))
        most.rect.x+=200
        most.image.fill(RED)
        most.W-=200
    if most.W==0 and mosta==0 and konez==False:
        iii=False
        fps_count_for_most=0        
        uniz=0
        mosta=1
    if most1.rect.x<=rect.x-90 and most1.W!=0 and iii==False and uniz==0:
        uniz=1
        most1.image = pygame.Surface((most1.W-200,most1.H))
        most1.rect.x+=200
        most1.image.fill(RED)
        most1.W-=200
        mosta=2
        iii=True
    if fps_count_for_most%25==0 and uniz==1 and most1.W!=0 and fps_count_for_most>0 and mosta==2:
        most1.image = pygame.Surface((most1.W-200, most1.H))
        most1.rect.x+=200
        most1.image.fill(RED)
        most1.W-=200
    if most1.W==0 and konez==False:
        iii=False
        fps_count_for_most=0        
        uniz=0

     
     
     
               
    if rect.x>=block37.rect.x+200:
        konez=True
        iii=True
    if konez==True and fps_count_for_most==1 and iii==True:
        all_sprites.update()
        all_turret.update()
        all_bullet.update()
        fps_count_for_most=0
    if block37.rect.x<=-600:
        iii=False
        
    
    
    if fps_count_for_t==30 and konez==True and iii==False:
        pula=PulaK(10,10,900,600,random.randint(10,30),random.randint(2,5))
        all_k.add(pula)   
    if fps_count_for_t==45 and konez==True and iii==False:
        pula=PulaK(10,10,850,600,random.randint(10,30),random.randint(2,5))
        all_k.add(pula)
        fps_count_for_t=0 
    for i in all_k:          
        i.rect.x-=i.speed
        if i.jump<0:
            i.rect.y+=(i.jump**2)/2
        else:
            i.rect.y-=(i.jump**2)/2
        i.jump-=1
            
    
    if rect.y>900:
        rect.y=1
        rect.x=1           
        Health = Health-1
        if Health == 0:
                exit()        
                
 
    
    
    sc.fill(WHITE)
    all_sprites.draw(sc)
    all_pula.draw(sc)
    all_k.draw(sc)
    all_turret.draw(sc)
    all_bullet.draw(sc)
    all_npc.draw(sc)
    for i in range(Health):
        car_rect = HP.get_rect(center=(50*(i+1),25))
        sc.blit(HP, car_rect)
    sc.blit(hero, rect)
    pygame.display.update()
    shot_count+=1
    fps_count+=1
    if iii:
        fps_count_for_most+=1
    if konez and iii==False:
        fps_count_for_t+=1
    print(konez)
    print(iii)
    print(fps_count_for_t)
    clock.tick(FPS)





