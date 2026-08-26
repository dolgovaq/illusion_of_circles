import pygame 
import random
print("!!EPILEPSY WARNING!!")

a = int(input("How many circles per frame? - "))
TIME =15
MAX_SIZE =100
MIN_SIZE = 10
MAX_DARKNESS =1
MIN_DARKNESS = 255
running = True
pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
clock = pygame.time.Clock()
while running and a:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            running = False
    pygame.mouse.set_visible(False)
    screen.fill((0,0,0))
    for i in range(0,a):
            POSITION = random.randint(1,2000),random.randint(1,2000)
            color1= random.randint(MAX_DARKNESS,MIN_DARKNESS)
            color2= random.randint(MAX_DARKNESS,MIN_DARKNESS)
            color3= random.randint(MAX_DARKNESS,MIN_DARKNESS)
            SIZE = random.randint(MIN_SIZE,MAX_SIZE)
            pygame.draw.circle(screen,
                               (color1,color2,color3),
                               POSITION,SIZE)
    pygame.display.flip()
    
    clock.tick(TIME)
pygame.quit()