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

pieces = []
for i in range(8):
    pieces.append(Piece("black", i, 1, "pawn"))
    pieces.append(Piece("white", i, 6, "pawn"))

pieces.append(Piece("black", 7, 0, "rook"))
pieces.append(Piece("black", 6, 0, "knight"))
pieces.append(Piece("black", 5, 0, "bishop"))
pieces.append(Piece("black", 4, 0, "king"))
pieces.append(Piece("black", 3, 0, "queen"))
pieces.append(Piece("black", 2, 0, "bishop"))
pieces.append(Piece("black", 1, 0, "knight"))
pieces.append(Piece("black", 0, 0, "rook"))

pieces.append(Piece("white", 7, 7, "rook"))
pieces.append(Piece("white", 6, 7, "knight"))
pieces.append(Piece("white", 5, 7, "bishop"))
pieces.append(Piece("white", 4, 7, "king"))
pieces.append(Piece("white", 3, 7, "queen"))
pieces.append(Piece("white", 2, 7, "bishop"))
pieces.append(Piece("white", 1, 7, "knight"))
pieces.append(Piece("white", 0, 7, "rook"))

def main():
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

                    piece_clicked.x = x
                    piece_clicked.y = y

                    for piece in pieces:
                        print(piece.type)
                        print(piece.x)
                        print(piece.y)

                    piece_clicked_coords = [-1, -1]
                    piece_clicked = pieces[0]
                            

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