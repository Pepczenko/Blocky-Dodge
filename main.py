import pygame
from pygame import mouse
from pygame.constants import MOUSEBUTTONDOWN
from pygame.event import clear, get
import random




    
class Text:
    def score_text():
        font = pygame.font.Font("freesansbold.ttf",32)
        text = font.render(str(Game.score),True,(255,255,255))
        Game.screen.blit(text,(25,25))
    
    def floating_text():
        font = pygame.font.Font("External-sources/Font.ttf",75)
        text = font.render(str("Blocky Dodge"),True,(255,255,255))
        Game.screen.blit(text,(200,Game.textY))
    
    def play_text():
        font = pygame.font.Font("freesansbold.ttf",32)
        text = font.render(str("Play"),True,(154,205,200))
        Game.screen.blit(text,(275,380))
    
    def exit_text():
        font = pygame.font.Font("freesansbold.ttf",32)
        text = font.render(str("Exit"),True,(154,205,200))
        Game.screen.blit(text,(450,380))
    
    def exit_text_for_death_screen():
        font = pygame.font.Font("freesansbold.ttf",32)
        text = font.render(str("Exit"),True,(154,205,200))
        Game.screen.blit(text,(450,380))
    
    def try_again_text():
        font = pygame.font.Font("freesansbold.ttf",32)
        text = font.render(str("Retry"),True,(154,205,200))
        Game.screen.blit(text,(270,380))




class Game:
    # Initialization    
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    title = pygame.display.set_caption("Blocky dodge")
    icon = pygame.image.load("External-sources/block.png")
    pygame.display.set_icon(icon)
    # movement and coords
    PlayerY = 50
    PlayerX = 100
    velocity = 0
    acceleration = 0.003
    enemyX = 1200
    random_height = random.randint(-50 ,400)
    textY = 100
    increment = 1
    # Time and other related
    clock = pygame.time.Clock()
    time_elapsed = 0
    dt = clock.tick()
    # technical
    score = 0
    death_screen = False
    main_menu = True
    main_game = True
    running = True
    # Game objects
    play_button = pygame.draw.rect(screen,(0,0,0),pygame.Rect(235,350,150,100))
    exit_button = pygame.draw.rect(screen,(0,0,0),pygame.Rect(410,350,150,100))
    player = pygame.draw.rect(screen,(255,255,255),pygame.Rect(PlayerX,PlayerY,25,25))
    enemy = pygame.draw.rect(screen,(255,69,0),pygame.Rect(enemyX,random_height,100,200))
    test = pygame.draw.rect(screen,(255,255,255),pygame.Rect(100,100,200,100))
    backround_screen = pygame.draw.rect(screen,(200,200,200),pygame.Rect(185,300,425,200))
    exit_button_for_deathscreen = pygame.draw.rect(screen,(0,0,0),pygame.Rect(410,350,150,100))
    try_again_button = pygame.draw.rect(screen,(0,0,0),pygame.Rect(235,350,150,100))
    
    
    
    
    
    
    # Functions for game etc start end
    def increment_speed():
        Game.enemyX += -Game.increment
            
               
    def start_screen():
        Game.screen.fill((200,200,200))
        play_button = pygame.draw.rect(Game.screen,(0,0,0),pygame.Rect(235,350,150,100))
        exit_button = pygame.draw.rect(Game.screen,(0,0,0),pygame.Rect(410,350,150,100))
        Text.floating_text()
        Text.play_text()
        Text.exit_text()
    
    
    def death_menu():
        backround_screen = pygame.draw.rect(Game.screen,(200,200,200),pygame.Rect(185,300,425,200))
        exit_button = pygame.draw.rect(Game.screen,(0,0,0),pygame.Rect(410,350,150,100))
        try_again_button = pygame.draw.rect(Game.screen,(0,0,0),pygame.Rect(235,350,150,100))
        Text.exit_text_for_death_screen()
        Text.try_again_text()
   
        
    def collision():
        player = pygame.draw.rect(Game.screen,(255,255,255),pygame.Rect(Game.PlayerX,Game.PlayerY,25,25))
        enemy = pygame.draw.rect(Game.screen,(255,69,0),pygame.Rect(Game.enemyX,Game.random_height,100,200))
        
        if player.colliderect(enemy):
            return True
    
            
    def maingameupdate():
        Game.PlayerY += Game.velocity
        Game.velocity += Game.acceleration
        Game.increment_speed()
        
    # check for position to move back 
        if Game.enemyX < -150:
            Game.enemyX = 800
            Game.score += 1
            Game.random_height = random.randint(-50,400)
            Game.increment += 0.05
            enemy = pygame.draw.rect(Game.screen,(255,69,0),pygame.Rect(Game.enemyX,Game.random_height,300,200))
    # Boundry and collision for the player
        if Game.PlayerY > 625 or Game.PlayerY < -25:
            Game.death_screen = True
            Game.main_game = False
        if Game.collision() == True:
            Game.death_screen = True
            Game.main_game = False
        pygame.display.flip()
        pygame.display.update()
        
    
    def double_rendering():
        Game.screen.fill((0,0,0))
        Text.score_text()
        player = pygame.draw.rect(Game.screen,(255,255,255),pygame.Rect(Game.PlayerX,Game.PlayerY,25,25))
        enemy = pygame.draw.rect(Game.screen,(255,69,0),pygame.Rect(Game.enemyX,Game.random_height,100,200))
        
        
def gameloop():
    
    
    
    while Game.running:
        if Game.main_menu == True:
            Game.start_screen()
            
        elif Game.main_game == True:
            Game.maingameupdate()  
            Game.double_rendering()
            
        elif Game.death_screen == True and Game.main_game == False:
            Game.death_menu()
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if Game.exit_button_for_deathscreen.collidepoint(mouse_position):
                    Game.running = False
                if Game.try_again_button.collidepoint(mouse_position):
                    Game.death_screen = False
                    Game.score = 0
                    Game.enemyX = 800
                    Game.score = 0
                    Game.PlayerY = 50
                    Game.PlayerX = 100
                    Game.main_game = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.running = False
            if Game.main_menu == True:
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    if Game.play_button.collidepoint(mouse_pos):
                        Game.main_menu = False
                    
                    if Game.exit_button.collidepoint(mouse_pos):
                        Game.running = False
                        print("hello")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game.velocity =- 0.6
        
        
        pygame.display.flip()
        
gameloop()