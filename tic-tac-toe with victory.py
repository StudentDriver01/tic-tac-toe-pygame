import pygame

from pygame.locals import *

GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255,66, 66)

pygame.init()

win = pygame.display.set_mode((550, 550))

pygame.display.set_caption('Tic-Tac-Toe')

pygame.display.flip()

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

first = pygame.draw.rect(win, (255,255,255), (25,25,150,150))
second = pygame.draw.rect(win, (255,255,255), (200,25,150,150))
third = pygame.draw.rect(win, (255,255,255), (375,25,150,150))

forth = pygame.draw.rect(win, (255,255,255), (25,200,150,150))
fifth = pygame.draw.rect(win, (255,255,255), (200,200,150,150))
sixth = pygame.draw.rect(win, (255,255,255), (375,200,150,150))

seventh = pygame.draw.rect(win, (255,255,255), (25,375,150,150))
eighth = pygame.draw.rect(win, (255,255,255), (200,375,150,150))
ninth = pygame.draw.rect(win, (255,255,255), (375,375,150,150))

#board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def win_check(num):
    for row in board:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True

    for tile in range(3):
        if board[tile][tile] == num:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if board[tile][2-tile] == num:
            continue
        else:
            break
    else:
        return True
    
space_allow = True

draw_object = 'rect'

first_open = True
second_open = True
third_open = True
forth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

text = 'Square Wins'
font = pygame.font.SysFont('JetBrains Mono', 72)
img = font.render(text, True, RED)

rect = img.get_rect()
rect.topleft = (110, 100)

text1 = 'Circle Wins'
img1 = font.render(text1, True, RED)

rect1 = img.get_rect()
rect1.topleft = (129, 100)


run = True
won = False
while run:

    pygame.time.delay(100)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and space_allow == True :
                
                

                board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

                first_open = True
                second_open = True
                third_open = True
                forth_open = True
                fifth_open = True
                sixth_open = True
                seventh_open = True
                eighth_open = True
                ninth_open = True
                
                first = pygame.draw.rect(win, (255,255,255), (25,25,150,150))
                second = pygame.draw.rect(win, (255,255,255), (200,25,150,150))
                third = pygame.draw.rect(win, (255,255,255), (375,25,150,150))

                forth = pygame.draw.rect(win, (255,255,255), (25,200,150,150))
                fifth = pygame.draw.rect(win, (255,255,255), (200,200,150,150))
                sixth = pygame.draw.rect(win, (255,255,255), (375,200,150,150))

                seventh = pygame.draw.rect(win, (255,255,255), (25,375,150,150))
                eighth = pygame.draw.rect(win, (255,255,255), (200,375,150,150))
                ninth = pygame.draw.rect(win, (255,255,255), (375,375,150,150))

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if won != True:
                if first.collidepoint(pos) and first_open :
                    if draw_object == 'rect':
                        pygame.draw.rect(win, (255,0,0), (50,50, 100,100))
                        draw_object = 'circle'
                        board[0][0] = 2
                    else:
                        pygame.draw.circle(win, (0,255,0), (100,100), 50)
                        draw_object = 'rect'
                        board[0][0] = 1
                    first_open = False
                    
                    
                if second.collidepoint(pos) and second_open :
                    if draw_object == 'rect':
                        pygame.draw.rect(win, (255,0,0), (225,50, 100,100))
                        draw_object = 'circle'
                        board[0][1] = 2
                    else:
                        pygame.draw.circle(win, (0,255,0), (275,100), 50)
                        draw_object = 'rect'
                        board[0][1] = 1
                    second_open = False
                    
                    
                if third.collidepoint(pos) and third_open :
                    if draw_object == 'rect':
                        pygame.draw.rect(win, (255,0,0), (400,50, 100,100))
                        draw_object = 'circle'
                        board[0][2] = 2
                    else:
                        pygame.draw.circle(win, (0,255,0), (450,100), 50)
                        draw_object = 'rect'
                        board[0][2] = 1
                    third_open = False
                    

                if forth.collidepoint(pos) and forth_open :
                    if draw_object == 'rect':
                        pygame.draw.rect(win, (255,0,0), (50,225, 100,100))
                        draw_object = 'circle'
                        board[1][0] = 2
                    else:
                        pygame.draw.circle(win, (0,255,0), (100,275), 50)
                        draw_object = 'rect'
                        board[1][0] = 1
                    forth_open = False
                    
                        
                if fifth.collidepoint(pos) and fifth_open :
                    if draw_object == 'rect':
                        pygame.draw.rect(win, (255,0,0), (225,225, 100,100))
                        draw_object = 'circle'
                        board[1][1] = 2
                    else:
                        pygame.draw.circle(win, (0,255,0), (275,275), 50)
                        draw_object = 'rect'
                        board[1][1] = 1
                    fifth_open = False
                    
                        
                if sixth.collidepoint(pos) and sixth_open :
                    if draw_object == 'rect':
                        pygame.draw.rect(win, (255,0,0), (400,225, 100,100))
                        draw_object = 'circle'
                        board[1][2] = 2
                    else:
                        pygame.draw.circle(win, (0,255,0), (450,275), 50)
                        draw_object = 'rect'
                        board[1][2] = 1
                    sixth_open = False
                    
                        
                if seventh.collidepoint(pos) and seventh_open :
                    if draw_object == 'rect':
                        pygame.draw.rect(win, (255,0,0), (50,400, 100,100))
                        draw_object = 'circle'
                        board[2][0] = 2
                    else:
                        pygame.draw.circle(win, (0,255,0), (100,450), 50)
                        draw_object = 'rect'
                        board[2][0] = 1
                    seventh_open = False
                    
                        
                if eighth.collidepoint(pos) and eighth_open :
                    if draw_object == 'rect':
                        pygame.draw.rect(win, (255,0,0), (225,400, 100,100))
                        draw_object = 'circle'
                        board[2][1] = 2
                    else:
                        pygame.draw.circle(win, (0,255,0), (275,450), 50)
                        draw_object = 'rect'
                        board[2][1] = 1
                    eighth_open = False
                    
                        
                if ninth.collidepoint(pos) and ninth_open :
                    if draw_object == 'rect':
                        pygame.draw.rect(win, (255,0,0), (400,400, 100,100))
                        draw_object = 'circle'
                        board[2][2] = 2
                    else:
                        pygame.draw.circle(win, (0,255,0), (450,450), 50)
                        draw_object = 'rect'
                        board[2][2] = 1
                    ninth_open = False

    if win_check(2):
        won = True
        win.fill(GRAY)
        win.blit(img, rect)
        if won == True:
            space_allow = False    
        

    if win_check(1):
        won = True
        win.fill(GRAY)
        win.blit(img1, rect1)
        if won == True:
            space_allow = False
            
            
    pygame.display.update()
    
pygame.quit()
