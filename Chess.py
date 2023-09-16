import pygame

class Piece:
    def __init__(self, colour, x, y, piece_type):
        self.colour = colour
        self.x =x
        self.y = y
        self.type = piece_type
    
    def draw(self, surface):
        img = pygame.image.load(f"images/{self.colour}_{self.type}.png")
        surface.blit(img, (self.x * 75, self.y * 75))

def main():
    pieces = []
    for i in range(8):
        pieces.append(Piece("black", i, 1, "pawn"))
        pieces.append(Piece("white", i, 6, "pawn"))

    pieces.extend([Piece("black", 7, 0, "rook"), 
                   Piece("black", 6, 0, "knight"), 
                   Piece("black", 5, 0, "bishop"), 
                   Piece("black", 4, 0, "king"), 
                   Piece("black", 3, 0, "queen"), 
                   Piece("black", 2, 0, "bishop"), 
                   Piece("black", 1, 0, "knight"), 
                   Piece("black", 0, 0, "rook"),
                   
                   Piece("white", 7, 7, "rook"), 
                   Piece("white", 6, 7, "knight"), 
                   Piece("white", 5, 7, "bishop"), 
                   Piece("white", 4, 7, "king"), 
                   Piece("white", 3, 7, "queen"), 
                   Piece("white", 2, 7, "bishop"), 
                   Piece("white", 1, 7, "knight"), 
                   Piece("white", 0, 7, "rook")])
    pygame.init()

    logo = pygame.image.load("images/logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Chatting with Chess")

    #Initalize screen with dimensions (640,640)
    screen = pygame.display.set_mode((640, 640))

    #Create surface with dimensions (640,640)
    board = pygame.Surface((600, 600))
    
    running = True
    
    piece_clicked_coords = [-1, -1]
    piece_clicked = pieces[0]

    while running:
        illegal_move = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if piece_clicked_coords == [-1, -1]:
                    mouse_pos = pygame.mouse.get_pos()

                    x = (mouse_pos[0] - 20) // 75
                    y = (mouse_pos[1] - 20) // 75

                    for piece in pieces:
                        if piece.x == x and piece.y == y:
                            piece_clicked_coords = [x, y]
                            piece_clicked = piece
                else:
                    new_mouse_pos = pygame.mouse.get_pos()

                    x = (new_mouse_pos[0] - 20) // 75
                    y = (new_mouse_pos[1] - 20) // 75

                    if (x > 7 or y > 7) or (x < 0 or y < 0):
                        piece_clicked_coords = [-1, -1]
                        break

                    if piece_clicked.type == "rook":
                        if not (piece_clicked.x == x or piece_clicked.y == y):
                            illegal_move = True
                    
                    for piece in pieces:
                        if piece.x == x and piece.y == y:
                            if piece.colour != piece_clicked.colour:
                                pieces.remove(piece)
                            elif piece.colour == piece_clicked.colour:
                                illegal_move = True
                                break
                    
                    if illegal_move == True:
                        piece_clicked_coords = [-1, -1]
                        break

                    piece_clicked.x = x
                    piece_clicked.y = y

                    piece_clicked_coords = [-1, -1]

            if event.type == pygame.QUIT:
                running = False

        #Fill board with colour
        board.fill((150, 111, 51))
        #Make every other rectangle light
        for x in range(0, 8, 2):
            for y in range(0, 8, 2):
                pygame.draw.rect(board, (210, 180, 140), (x * 75, y * 75, 75, 75))
                pygame.draw.rect(board, (210, 180, 140), ((x+1) * 75, (y+1) * 75, 75, 75))

        for piece in pieces:
            piece.draw(board)

        #Draws board onto screen, positioned at (20,20)
        screen.blit(board, (20, 20))

        #Update screen
        pygame.display.flip()

if __name__== "__main__":
    main()