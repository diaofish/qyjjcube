import pygame
import sys 

pygame.init()


screen = pygame.display.set_mode((600,800))
screen_rect = screen.get_rect()
bg_image = pygame.image.load('.\images\bg.png')
bg_rect = bg_image.get_rect()

cube_image = pygame.image.load('.\images\cube_01.png')
# cube_image = pygame.image.load(r'c:\Users\wsgsb\Desktop\qycube\images\cube_01.png')
cube_rect = cube_image.get_rect()  
screen.blit(cube_image,cube_rect)
is_moving = False

def is_in_rect(pos, rect):
    x, y = pos
    rx, ry, rw, rh = rect
    if (rx <= x <= rx+rw) and (ry <= y <= ry+rh):
        return True
    return False



while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_in_rect(event.pos,cube_rect) :
                is_moving = True
        if event.type == pygame.MOUSEMOTION and is_moving == True:
            mouse_x,mouse_y = event.pos
            cube_rect.x = mouse_x
            cube_rect.y = mouse_y
        if event.type == pygame.MOUSEBUTTONUP :   
            is_moving = False

        screen.blit(bg_image,bg_rect)   
        screen.blit(cube_image,cube_rect) 
        pygame.display.flip()       
        
