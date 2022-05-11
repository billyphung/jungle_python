import pygame
from jungle.constants import *
from jungle.game import *

FPS = 60

#objet texte gagnant
pygame.font.init()
font= pygame.font.Font(pygame.font.get_default_font(),36)
text= font.render('You win',True,BLACK,WHITE)
textRect= text.get_rect()
textRect.center = (WIDTH//2,HEIGHT//2)

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jungle chess')

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row,col


# test
#fonction principale
def main():
    run = True
    flag_endgame = False
    clock = pygame.time.Clock()
    game = Game(WIN)



    while run:
        clock.tick(FPS)

        if game.winner() != None:
            flag_endgame = True
            WIN.fill(WHITE)
            WIN.blit(text,textRect)
            pygame.display.update()


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not flag_endgame:
                    pos = pygame.mouse.get_pos()
                    row,col= get_row_col_from_mouse(pos)
                    game.select(row,col)
                else:
                    run = False

        if not flag_endgame:
            game.update()
    
    pygame.quit()


main()
