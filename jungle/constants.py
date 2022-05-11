import pygame
import os

SQUARE_SIZE = 75
ROWS,COLS = 9,7
WIDTH,HEIGHT = COLS*SQUARE_SIZE,ROWS*SQUARE_SIZE

#constantes RGB des couleurs
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)


#positions cases spéciales
Pieges = [(0,2),(0,4),(1,3),(7,3),(8,2),(8,4)]
Caves = [(0,3),(8,3)] #cave blue, cave red
Rivieres = [(3,1),(3,2),(4,1),(4,2),(5,1),(5,2),(3,4),(3,5),(4,4),(4,5),(5,4),(5,5)]


#chemin vers dossier images
Path_images = "jungle\images"

#blue pieces
blue_elephant = pygame.transform.scale(pygame.image.load(os.path.join(Path_images,"bEL.png")), (SQUARE_SIZE,SQUARE_SIZE))

#red pieces
red_elephant = pygame.transform.scale(pygame.image.load(os.path.join(Path_images,"rEL.png")), (SQUARE_SIZE,SQUARE_SIZE))


#river
river = pygame.transform.scale(pygame.image.load(os.path.join(Path_images,"river.png")), (SQUARE_SIZE,SQUARE_SIZE))

#pièges
trap = pygame.transform.scale(pygame.image.load(os.path.join(Path_images,"trap.png")), (SQUARE_SIZE,SQUARE_SIZE))

#cave
cave = pygame.transform.scale(pygame.image.load(os.path.join(Path_images,"cave.png")), (SQUARE_SIZE,SQUARE_SIZE))