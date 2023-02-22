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
block2=Block(100,10,750,710)                     #тут нужно создавать блоки (ширина, высота, x, y)
block3=Block(150000,10,0,830)
block4=Block(100,10,750,610)
block5=Block(100,10,1500,760)





all_sprites = pygame.sprite.Group()
all_pula = pygame.sprite.Group()
all_pulas=[]
all_sprite=[]



all_sprites.add(block1,block2,block3,block4,block5)                 #тут нужно добавлять в группу и в массив блоки 
all_sprite.append(block1)
all_sprite.append(block2)
all_sprite.append(block3)
all_sprite.append(block4) 
all_sprite.append(block5) 





 
hero = pygame.Surface((11, 59))                        #в этой части я создаю героя и присваиваю ему нижние координаты, как координаты земли
hero.fill(BLUE)
rect = hero.get_rect(centerx=W//2)

rect.bottom = H-69



moment=False                    #часть для прыжка, в основном нам нужен moment, который говорит в прыжке перс или нет
jump_count=28
jump_now=0


t=0        
u=1
vesomost=1 
mozno=0    #можно прыгнуть или нет 
polet=False 
polozenie=0  
fps_count=0 
mozet=0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:            
                mozet=True                    # тут проверка на нражатую нижнюю клавишу 
            if event.key==pygame.K_SPACE and mozno==0:                 
                if mozet==True:                #тут у нас, если mozet равно true, тогда при нажатии space он будет спускаться на 10 координат вниз       
                    rect.y+=10
                    mozet=False
                else:
                    moment=True           
            
            if event.key==pygame.K_w and fps_count>15:
                pula=Pula(100,10,rect.center[0],rect.center[1],polozenie)     #тут каждые 15 кадров при нажатии клавиши w создаем пулю ()
                all_pula.add(pula)
                all_pulas.append(pula)
                polet=True
                fps_count=0
            
        
    keys=pygame.key.get_pressed()
    
        
    #тут просто движениие вправо или влево с указанием движения пули, как положение     
    if keys[pygame.K_RIGHT]:
        polozenie=0
        if rect.center[0]==W//2:           #тут, если центр будет равна центру экрана, то движутся все блоки, в противном случае движется сам персонаж
            all_sprites.update()
        else:
            rect.x+=10
    if keys[pygame.K_LEFT]:
        polozenie=1                     
        rect.x-=10
    
    
    
    
    # тут перебираем каждую пулю и если положение 0, то она летит вправо, если 1, то влево
    if polet==True :
        for i in all_pulas:
            if i.polozenie==0:        
                i.rect.x+=20
            if i.polozenie==1:
                i.rect.x-=20
     
        
        
           
    
    
    
    
    if moment is True:
        hero.fill(GREEN)
        
        if jump_now<=jump_count/2:
            if u==1:
                rect.y-=11
                u=0                              # тут мы прыгаем на 11 координат, чтобы дальше лететь по координатам кратным 10 
            else:
                rect.y-=10
            jump_now+=1
        elif jump_now<=jump_count:
            
            
            
            rect.y+=10
            
            for i in all_sprite:
                if i.rect.top==rect.bottom :
                    rect.y+=1
                    jump_now=0
                    moment=False
                    u=1
                    
        
    for i in all_sprite:
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
            
        
               
        
        
    print("hfiergfgryfgu")
               
                
                
 
    
    
    sc.fill(WHITE)
    all_sprites.draw(sc)
    all_pula.draw(sc)
    sc.blit(hero, rect)
    pygame.display.update()
    fps_count+=1
    print(fps_count)
 
    clock.tick(FPS)

