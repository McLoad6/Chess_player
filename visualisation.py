import pygame
import chess_piece_class
import rules

pieces_list = chess_piece_class.pieces_list

def chess_picture_position(piece):
    pp = piece.picture_position
    x = 83.33     
    y = 83.33     
    row = pp // 6
    column = pp % 6
    coordinate = [column*x - 5, row*y - 4 ,x ,y]
    return coordinate

def visualisation():
    pygame.init()
    
    table_color = ['burlywood1', 'saddle brown']
    
    table_size = 800  
    field_size=table_size //8  
    
    table=pygame.display.set_mode((table_size, table_size))

    picture=pygame.image.load("chess_pieces.png")
    picture=pygame.transform.scale(picture,(500,166.67))

    marked = 0
    steps = 0
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                return 
            elif event.type == pygame.MOUSEBUTTONDOWN and marked == 0:
                click_location = event.dict["pos"]
                for piece in pieces_list:
                    if piece.inside_of_field(click_location):
                        color = steps % 2
                        if piece.color == color:
                            marked = 1
                            object_location = pieces_list.index(piece)
                            break
            elif event.type == pygame.MOUSEBUTTONDOWN and marked == 1:
                click_location = event.dict["pos"]
                piece = pieces_list[object_location]
                if rules.possible_step(pieces_list, piece, click_location):
                    piece.move(click_location)
                    steps += 1
                marked = 0
                break            

        for row in range(8):  #creating the chess table         
            color_index = row % 2       
            for column in range(8):    
                field = (column*field_size, row*field_size, field_size, field_size)
                table.fill(table_color[color_index], field)
                color_index = (color_index + 1) % 2 #color changing

        for piece in pieces_list: #setting the pieces on the table
            picture_position = chess_picture_position(piece)
            table_coordinates = piece.table_position
            x = table_coordinates[0] * 100
            y = table_coordinates[1] * 100
            table.blit(picture, (x,y), picture_position)

        pygame.display.flip()

    pygame.quit()

visualisation()

