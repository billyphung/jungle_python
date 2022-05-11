
import pygame
from jungle.constants import *


class Piece:
    def __init__(self,row,col,team,force):
        self.row =row #int
        self.col=col #int

        self.x=0
        self.y=0
        self.calc_pos()
        
        self.team= team #RED ou BLUE
        self.force=force #int entre 0 et 8
        self.available_moves=[]
        
    def piece_move(self,row,col):
        self.row=row 
        self.col=col
        self.calc_pos()
    
    def calc_pos(self):
        self.x=self.col*SQUARE_SIZE
        self.y=self.row*SQUARE_SIZE

    def clear_available_moves(self):
        self.available_moves = []
    
    def piece_display(self,win):
        if self.team == BLUE:
            win.blit(blue_elephant,(self.x,self.y))
        if self.team == RED:
            win.blit(red_elephant,(self.x,self.y))
            

    def move(self,row,col):
        self.row = row
        self.col = col
        self.calc_pos()



    


