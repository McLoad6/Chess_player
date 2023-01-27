import pygame

class Chess_pieces:

    def __init__(self, picture_position, table_position, color, value):
        self.picture_position = picture_position
        self.table_position = table_position
        self.color = color  # 0=white 1=black
        self.value = value
    
    def inside_of_field(self, click_point):
        (self_x, self_y) = self.table_position
        width = 99
        height = 99
        (x, y) = click_point
        return ( x >= self_x*100 and x < self_x*100 + width and y >= self_y*100 and y < self_y*100 + height)

    def move(self, click_location):
        (x,y) = click_location
        self_x = x // 100
        self_y = y // 100
        self.table_position = (self_x,self_y)

class King(Chess_pieces):
    def __init__(self, picture_position = 0, table_position = (4,7), color=0, value = 1000):
        self.picture_position = picture_position
        self.table_position = table_position
        self.color = color 
        self.value = value

    def moving_range(self, obstacle, coordinates):
        (self_x, self_y) = self.table_position
        (x, y) = coordinates
        x = x//100
        y = y//100
        x_dif = abs(self_x - x)
        y_dif = abs(self_y - y)
        return x_dif <= 1 and y_dif <= 1

       
class Queen(Chess_pieces):
    def __init__(self, picture_position = 1, table_position = (3,7), color=0, value = 20):
        self.picture_position = picture_position
        self.table_position = table_position
        self.color = color 
        self.value = value 
    
    def moving_range(self, obstacle, coordinates):
        (obs_x, obs_y) = obstacle.table_position
        (self_x, self_y) = self.table_position
        (x, y) = coordinates
        x = x//100
        y = y//100
        x_dif = self_x - x
        y_dif = self_y - y
        if (abs(x_dif) == 0 and abs(y_dif) <= 7):
            if obs_x == x:
                return (obs_y <= y and obs_y <= self_y) or (obs_y >= y and obs_y >= self_y)
            else:
                return True
        elif (abs(x_dif) <= 7 and abs(y_dif) == 0):
            if obs_y == y:
                return (obs_x <= x and obs_x <= self_x) or (obs_x >= x and obs_x >= self_x)
            else:
                return True
        elif (abs(x_dif) == abs(y_dif)):
            if x_dif >= 0:
                if y_dif >= 0:
                    return (x - y != obs_x - obs_y) or (obs_x >= self_x or obs_x <= x)
                else:
                    return (x + y != obs_x + obs_y) or (obs_x >= self_x or obs_x <= x)
            else:
                if y_dif >= 0:
                    return (x + y != obs_x + obs_y) or (obs_x <= self_x or obs_x >= x)
                else:
                    return (x-y != obs_x - obs_y) or (obs_x <= self_x or obs_x >= x)
        else:
            return False

class Rook(Chess_pieces):
    def __init__(self, picture_position = 4, table_position = (0,7), color=0, value = 10):
        self.picture_position = picture_position
        self.table_position = table_position
        self.color = color 
        self.value = value 
    
    def moving_range(self, obstacle, coordinates):
        (obs_x, obs_y) = obstacle.table_position
        (self_x, self_y) = self.table_position
        (x, y) = coordinates
        x = x//100
        y = y//100
        x_dif = abs(self_x - x)
        y_dif = abs(self_y - y)
        if (x_dif == 0 and y_dif <= 7):
            if obs_x == x:
                return (obs_y <= y and obs_y <= self_y) or (obs_y >= y and obs_y >= self_y)
            else:
                return True
        elif (x_dif <= 7 and y_dif == 0):
            if obs_y == y:
                return (obs_x <= x and obs_x <= self_x) or (obs_x >= x and obs_x >= self_x)
            else:
                return True
        else:
            return False

class Bishop(Chess_pieces):
    def __init__(self, picture_position = 2, table_position = (2,7), color=0, value = 5):
        self.picture_position = picture_position
        self.table_position = table_position
        self.color = color 
        self.value = value 
    
    def moving_range(self, obstacle, coordinates):
        (obs_x, obs_y) = obstacle.table_position
        (self_x, self_y) = self.table_position
        (x, y) = coordinates
        x = x//100
        y = y//100
        x_dif = self_x - x
        y_dif = self_y - y
        if (abs(x_dif) == abs(y_dif)):
            if x_dif >= 0:
                if y_dif >= 0:
                    return (x - y != obs_x - obs_y) or (obs_x >= self_x or obs_x <= x)
                else:
                    return (x + y != obs_x + obs_y) or (obs_x >= self_x or obs_x <= x)
            else:
                if y_dif >= 0:
                    return (x + y != obs_x + obs_y) or (obs_x <= self_x or obs_x >= x)
                else:
                    return (x-y != obs_x - obs_y) or (obs_x <= self_x or obs_x >= x)
        else:
            return False

class Knight(Chess_pieces):
    def __init__(self, picture_position = 3, table_position = (1,7), color=0, value = 4):
        self.picture_position = picture_position
        self.table_position = table_position
        self.color = color 
        self.value = value 
    
    def moving_range(self, obstacle, coordinates):
        (self_x, self_y) = self.table_position
        (x, y) = coordinates
        x = x//100
        y = y//100
        x_dif = abs(self_x - x)
        y_dif = abs(self_y - y)
        return (x_dif == 1 and y_dif == 2) or (x_dif == 2 and y_dif == 1)

class Pawn(Chess_pieces):
    def __init__(self, picture_position = 5, table_position = (0,6), color=0, value = 1):
        self.picture_position = picture_position
        self.table_position = table_position
        self.color = color 
        self.value = value
    
    def moving_range(self, obstacle, coordinates):
        (obs_x, obs_y) = obstacle.table_position        
        (self_x, self_y) = self.table_position
        (x, y) = coordinates
        x = x//100
        y = y//100
        x_dif = abs(self_x - x)
        y_dif = y - self_y
        color = self.color
        if color == 1:
            if self_y == 1 and y_dif == 2:
                return x_dif == 0 and y_dif <= 2 and y_dif >= 0 and (obs_x != x or (obs_y != 2 and obs_y != 3))
            else:
                return x_dif == 0 and y_dif == 1 and (obs_x != x or obs_y != y)
        else:
            if self_y == 6 and y_dif == -2:
                return x_dif == 0 and y_dif <= 0 and y_dif >= -2 and (obs_x != x or (obs_y != 5 and obs_y != 4))
            else:
                return x_dif == 0 and y_dif == -1 and (obs_x != x or obs_y != y)

wking = King()
bking = King(6,(4,0),1)
wqueen = Queen()
bqueen = Queen(7,(3,0),1)
wrook1 = Rook()
wrook2 = Rook(4,(7,7))
brook1 = Rook(10,(0,0),1)
brook2 = Rook(10,(7,0),1)
wbishop1 = Bishop()
wbishop2 = Bishop(2,(5,7))
bbishop1 = Bishop(8,(2,0),1)
bbishop2 = Bishop(8,(5,0),1)
wknight1 = Knight()
wknight2 = Knight(3,(6,7))
bknight1 = Knight(9,(1,0),1)
bknight2 = Knight(9,(6,0),1)
wpawn1 = Pawn()
wpawn2 = Pawn(5,(1,6))
wpawn3 = Pawn(5,(2,6))
wpawn4 = Pawn(5,(3,6))
wpawn5 = Pawn(5,(4,6))
wpawn6 = Pawn(5,(5,6))
wpawn7 = Pawn(5,(6,6))
wpawn8 = Pawn(5,(7,6))
bpawn1 = Pawn(11,(0,1),1)
bpawn2 = Pawn(11,(1,1),1)
bpawn3 = Pawn(11,(2,1),1)
bpawn4 = Pawn(11,(3,1),1)
bpawn5 = Pawn(11,(4,1),1)
bpawn6 = Pawn(11,(5,1),1)
bpawn7 = Pawn(11,(6,1),1)
bpawn8 = Pawn(11,(7,1),1)
pieces_list = [wking, bking, wqueen, bqueen, wrook1, wrook2, brook1, brook2, wbishop1, wbishop2, bbishop1, bbishop2, wknight1, wknight2, bknight1, bknight2, wpawn1, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7, wpawn8, bpawn1, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7, bpawn8]
