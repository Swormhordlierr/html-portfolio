import pygame
from sys import exit
from random import randint as ra
time=0

def scoreshow():
    global score
    global scorerect
    global time
    time = pygame.time.get_ticks() - lscore
    score = text.render(str(int(time)),False,"Red")
    scorerect = score.get_rect(center = (1400, 100))
    screen.blit(score,scorerect)
    
def enimov (enilist):
    if enilist:
        for enirct in enilist:
            enirct.x-=a
            if enirct.bottom==500:screen.blit(villian,enirct)
            else: screen.blit(herovillian,enirct)
        enilist=[eni for eni in enilist if enirct.x>-400]
        return enilist
    
    else:return[]
    
def hitbox(player_rect,enilist):
    if enilist:
        for enirct in enilist:
            if player_rect.colliderect(enirct):
                return False
                
    return True
    

pygame.init()               #starts the pygame

screen = pygame.display.set_mode((1550,800))     #size of display screen
pygame.display.set_caption('SUMMA game')        #name of game

clock = pygame.time.Clock()  #to run the game smooth

lscore= 0

a=9

sky=pygame.Surface((1550,500))
sky.fill('aquamarine')

clouds=pygame.transform.scale(pygame.image.load(r"C:\Users\91915\OneDrive\Desktop\SnakeBabu\learningpygame_game\images\clouds.png").convert_alpha(),(150,130))
clorct1=clouds.get_rect(center=(200,200))
clorct2=clouds.get_rect(center=(1000,200))

base = pygame.Surface((1550,300))
base.fill('olive')

basegrass = pygame.Surface((1550,50))
basegrass.fill('darkgreen')

text = pygame.font.Font(r"C:\Users\91915\OneDrive\Desktop\SnakeBabu\learningpygame_game\text\BAD_GRUNGE.ttf",70)
textdisp = text.render('MD',False,'Black')
textrect = textdisp.get_rect(center=(775,75 ))

latscore=0

gamendtxt= text.render("GAME OVER",False,"White")
gamendrect= gamendtxt.get_rect(center=(775,300))

startgametxt = text.render("Start Game",False,"White")
startgamerect = startgametxt.get_rect(center=(775,400))

box=pygame.Rect(10,10,1530,770)

gravity=0

variable=False

jumpsound= pygame.mixer.Sound(r"C:\Users\91915\OneDrive\Desktop\SnakeBabu\learningpygame_game\musics\jump.mp3")
BG=pygame.mixer.Sound(r"C:\Users\91915\OneDrive\Desktop\SnakeBabu\learningpygame_game\musics\BG.mp3")
BG.set_volume(0.5)
BG.play(loops=-1)

enitmr= pygame.USEREVENT + 1  
pygame.time.set_timer(enitmr,1600)

#enemies
villian =pygame.transform.scale(pygame.image.load(r"C:\Users\91915\OneDrive\Desktop\SnakeBabu\learningpygame_game\images\snake.png").convert_alpha(),(180,45))
herovillian = pygame.transform.scale(pygame.image.load(r"C:\Users\91915\OneDrive\Desktop\SnakeBabu\learningpygame_game\images\herovillian.png").convert_alpha(),(303,122))
#villian_rect=villian.get_rect(midbottom=(1650,500)) 

enilist=[]

player=pygame.transform.scale(pygame.image.load(r"C:\Users\91915\OneDrive\Desktop\SnakeBabu\learningpygame_game\images\player.png").convert_alpha(),(90,153))
player_rect=player.get_rect(midbottom=(150,555))

#all elements and everything is put inside the loop to run it continuously 

while True:   
    #to get all types of input                              
    for event in pygame.event.get():  
        #to quit          
        if event.type==pygame.QUIT:         
            pygame.quit()   
            #exits the while loop
            exit      
        if event.type==pygame.MOUSEBUTTONDOWN:
            print("usin mouse")
        if event.type==pygame.KEYDOWN: 
            if player_rect.top<250: gravity=0
            elif event.key==pygame.K_SPACE and variable:
                gravity=-25
                jumpsound.play()
        
        if startgamerect.collidepoint(pygame.mouse.get_pos()):
            if event.type==pygame.MOUSEBUTTONDOWN:
                variable = True
                #villian_rect.left = 1650
                lscore=pygame.time.get_ticks()
                
        
        if event.type==enitmr and variable:
            if ra(0,5)==0:
                 enilist.append(herovillian.get_rect(midbottom=(ra(1550,2000),350)))
                
            else:
                enilist.append(villian.get_rect(midbottom=(ra(1550,1900),500)))
               
    if variable:
        screen.blit(sky,(0,0))
        screen.blit(base,(0,500))
        screen.blit(basegrass,(0,500))

        pygame.draw.rect(screen,'White',textrect,100,11)
        pygame.draw.rect(screen,'#ef5609',textrect,11,11)
        pygame.draw.line(screen,"White",(0,0),(1550,0),10)

        screen.blit(textdisp,textrect) 
        screen.blit(clouds,clorct1)
        screen.blit(clouds,clorct2)
        #screen.blit(villian,villian_rect)
        
        scoreshow()
        
        #if villian_rect.right<=0:
        #    villian_rect.left=1600
        #villian_rect.x-=a

        enilist=enimov(enilist)
        
        gravity+=1
        player_rect.y+=gravity

        if player_rect.bottom>=565: player_rect.bottom=555
        screen.blit(player,player_rect)                
    

        #if villian_rect.colliderect(player_rect):
            #latscore = pygame.time.get_ticks() - lscore
            #string = "Score = " + str(latscore)
            #scoretxt = text.render(string,False, "White")
            #scoretxtrct = scoretxt.get_rect(center=(775, 500))
            #a=8           
            #variable=False
        
        if ((pygame.time.get_ticks()/100)-lscore)%5==0 and (pygame.time.get_ticks()-lscore)/5!=0: a+=2

        if (pygame.time.get_ticks()/100)-lscore==0: a=9

        
        variable= hitbox(player_rect,enilist)

        if variable==False:
            enilist.clear()
            a=9
            
        
    else:
        player_rect.midbottom=(150,555)
        screen.fill("Black")
        pygame.draw.rect(screen,"Orange",box,5,4)
        
        screen.blit(startgametxt,startgamerect)
        pygame.draw.rect(screen,"Orange",startgamerect,3,13)

        if time==0:
            pass

        else:
            scorerect.center=(775,500)
            screen.blit(gamendtxt,gamendrect)
            screen.blit(score,scorerect)
            pygame.draw.rect(screen,"Orange",scorerect,2,5)

    #updates the display
    pygame.display.update()                
    clock.tick(60)