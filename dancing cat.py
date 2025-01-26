import pygame

# makes it go
pygame.init()
screen = pygame.display.set_mode((682, 376))
pygame.display.set_caption('THE DANCING CATINATOR')

# loads image
W = pygame.image.load('w key.png')
A = pygame.image.load('a key.png')
S = pygame.image.load('s key.png')
D = pygame.image.load('d key.png')
default = pygame.image.load('no key.png').convert()
    
# main part
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # exit game when done
        
    # make sure it knows which key is pressed
    keys = pygame.key.get_pressed()
    screen.fill((255, 255, 255))  # fill screen with white background
    
    if keys[pygame.K_w]:
        screen.blit(W, (0, 0)) #there should be an easy way to do this
    elif keys[pygame.K_a]:
        screen.blit(A, (0, 0))
    elif keys[pygame.K_s]:
        screen.blit(S, (0, 0))
    elif keys[pygame.K_d]:
        screen.blit(D, (0, 0))
    else:
        screen.blit(default, (0, 0))
    
    pygame.display.flip()  # update screen
    
# honestly i shouldnt even have to put this
pygame.quit()