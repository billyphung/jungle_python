import pygame
from .constants import *
from .piece import Piece

class Board:
    def __init__(self):
        #définir le tableau comme un tableau 2D
        self.board = []
        
        #nb de pieces restantes sur le plateau(il y a 8 pieces au début : elephant,lion,tigre,leopard,chien,loup,chat,rat)
        self.red_left= 8 
        self.blue_left= 8

        self.create_board()
        

    #dessines cases du plateau
    def draw_squares(self,win):
        win.fill(WHITE) #on remplit la fenêtre de noir
        for x in range(0,WIDTH,SQUARE_SIZE):
            for y in range(0,HEIGHT,SQUARE_SIZE):
                pygame.draw.rect(win, BLACK, (x, y, SQUARE_SIZE, SQUARE_SIZE),1) #on dessine des carrés blancs avec 10px de bordure
    
    def draw_pieges(self,win,row,col):
        x=col*SQUARE_SIZE
        y=row*SQUARE_SIZE
        win.blit(trap,(x,y))
    
    def draw_river(self,win,row,col):
        x=col*SQUARE_SIZE
        y=row*SQUARE_SIZE
        win.blit(river,(x,y))

    def draw_caves(self,win,row,col):
        x=col*SQUARE_SIZE
        y=row*SQUARE_SIZE
        win.blit(cave,(x,y))


    def create_board(self):
        #-1 : trap
        #-2 : river
        #-3 : cave
        self.board = [[Piece(0,0,BLUE,8),0,0,0,0,0,Piece(0,7-1,BLUE,8)] ,
                     [0,Piece(1,1,BLUE,8),0,0,0,Piece(1,6-1,BLUE,8),0],
                     [Piece(3-1,1-1,BLUE,8),0,Piece(3-1,3-1,BLUE,8),0,Piece(3-1,5-1,BLUE,8),0,Piece(3-1,7-1,BLUE,8)],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [Piece(7-1,1-1,RED,8),0,Piece(7-1,3-1,RED,8),0,Piece(7-1,5-1,RED,8),0,Piece(7-1,7-1,RED,8)],
                     [0,Piece(8-1,2-1,RED,8),0,0,0,Piece(8-1,6-1,RED,8),0],
                     [Piece(9-1,1-1,RED,8),0,0,0,0,0,Piece(9-1,7-1,RED,8)] ] #liste de listes = liste de lignes (chaque élément est une ligne)

    def draw_board(self,win):
        self.draw_squares(win)
        for row in range(0,ROWS,1):
            for col in range(0,COLS,1):
                piece = self.board[row][col]
                if (row,col) in Pieges:
                    self.draw_pieges(win,row,col)
                if (row,col) in Rivieres:
                    self.draw_river(win,row,col)
                if (row,col) in Caves:
                    self.draw_caves(win,row,col)
                if piece !=0:
                    piece.piece_display(win)

    def remove(self,piece):
        self.board[piece.row][piece.col]=0
        if piece !=0:
            if piece.team==RED:
                self.red_left -= 1
            if piece.team==BLUE:
                self.blue_left -= 1
    
    def move(self,piece,row,col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)

    def get_piece(self,row,col):
        return self.board[row][col] 

    def get_valid_moves(self,piece):
        moves = []
        moves.append((piece.row+1,piece.col))
        moves.append((piece.row-1,piece.col))
        moves.append((piece.row,piece.col+1))
        moves.append((piece.row,piece.col-1))

        if(piece.force!=1):

            if( (piece.row+1,piece.col) in Rivieres ):
                moves.remove((piece.row+1,piece.col))

            if( (piece.row-1,piece.col) in Rivieres ):
                moves.remove((piece.row-1,piece.col))

            if( (piece.row,piece.col+1) in Rivieres ):
                moves.remove((piece.row+1,piece.col))

            if( (piece.row,piece.col-1) in Rivieres ):
                moves.remove((piece.row+1,piece.col))
            

        return moves
    
    def winner(self):
        if self.red_left<=0:
            return BLUE
        if self.blue_left<=0:
            return RED
        if self.board[0][3]!=0:
            return RED
        if self.board[8][3]!=0:
            return BLUE
        return None 
    