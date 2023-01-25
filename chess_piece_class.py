import pygame

class Chess_pieces:

    def __init__(self, picture_position, table_position, value):
        self.picture_position = picture_position
        self.table_position = table_position
        self.value = value

class King(Chess_pieces):
    def __init__(self, picture_position = 0, table_position = (4,7), value = 1000):
        self.picture_position = picture_position
        self.table_position = table_position

class Queen(Chess_pieces):
    def __init__(self, picture_position = 1, table_position = (3,7), value = 20):
        self.picture_position = picture_position
        self.table_position = table_position 

class Rook(Chess_pieces):
    def __init__(self, picture_position = 4, table_position = (0,7), value = 10):
        self.picture_position = picture_position
        self.table_position = table_position 

class Bishop(Chess_pieces):
    def __init__(self, picture_position = 2, table_position = (2,7), value = 5):
        self.picture_position = picture_position
        self.table_position = table_position 

class Knight(Chess_pieces):
    def __init__(self, picture_position = 3, table_position = (1,7), value = 4):
        self.picture_position = picture_position
        self.table_position = table_position 

class Pawn(Chess_pieces):
    def __init__(self, picture_position = 5, table_position = (0,6), value = 1):
        self.picture_position = picture_position
        self.table_position = table_position 
        self.value = value

wking = King()
bking = King(6,(4,0))
wqueen = Queen()
bqueen = Queen(7,(3,0))
wrook1 = Rook()
wrook2 = Rook(4,(7,7))
brook1 = Rook(10,(0,0))
brook2 = Rook(10,(7,0))
wbishop1 = Bishop()
wbishop2 = Bishop(2,(5,7))
bbishop1 = Bishop(8,(2,0))
bbishop2 = Bishop(8,(5,0))
wknight1 = Knight()
wknight2 = Knight(3,(6,7))
bknight1 = Knight(9,(1,0))
bknight2 = Knight(9,(6,0))
wpawn1 = Pawn()
wpawn2 = Pawn(5,(1,6))
wpawn3 = Pawn(5,(2,6))
wpawn4 = Pawn(5,(3,6))
wpawn5 = Pawn(5,(4,6))
wpawn6 = Pawn(5,(5,6))
wpawn7 = Pawn(5,(6,6))
wpawn8 = Pawn(5,(7,6))
bpawn1 = Pawn(11,(0,1))
bpawn2 = Pawn(11,(1,1))
bpawn3 = Pawn(11,(2,1))
bpawn4 = Pawn(11,(3,1))
bpawn5 = Pawn(11,(4,1))
bpawn6 = Pawn(11,(5,1))
bpawn7 = Pawn(11,(6,1))
bpawn8 = Pawn(11,(7,1))
pieces_list = (wking, bking, wqueen, bqueen, wrook1, wrook2, brook1, brook2, wbishop1, wbishop2, bbishop1, bbishop2, wknight1, wknight2, bknight1, bknight2, wpawn1, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7, wpawn8, bpawn1, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7, bpawn8)
