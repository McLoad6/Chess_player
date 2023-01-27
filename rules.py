import chess_piece_class

pieces_list = chess_piece_class.pieces_list

def possible_step(pieces_list, movable_piece, coordinate):
    color = movable_piece.color    
    if type(movable_piece) == chess_piece_class.Pawn:
        kick_it = 0  # :)
        (x, y) = coordinate
        x = x//100
        y = y//100
        (self_x, self_y) = movable_piece.table_position
        if color == 1 and self_y == y - 1:
            if self_x == x + 1:
                kick_it = 1
            elif self_x == x - 1:
                kick_it = 1
        elif color == 0 and self_y == y + 1:
            if self_x == x + 1:
                kick_it = 1
            elif self_x == x - 1:
                kick_it = 1
        if kick_it == 1:
            for piece in pieces_list:
                if piece.inside_of_field(coordinate):
                    color_piece = piece.color
                    if color == color_piece:
                        return False
                    else:
                        pieces_list.remove(piece)
                        return True
    for piece in pieces_list:  # no piece on the way?
        if movable_piece.moving_range(piece, coordinate):
            continue
        else:
            return False
    
    for piece in pieces_list: # target position is it empty?
        if piece.inside_of_field(coordinate):
            color_piece = piece.color
            if color == color_piece:
                return False
            else:
                pieces_list.remove(piece)
                return True
    return True

