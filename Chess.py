import pygame

class Piece:
    def __init__(self, colour, x, y, piece_type):
        self.colour = colour
        self.x =x
        self.y = y
        self.type = piece_type
    
    def draw(self, surface):
        img = pygame.image.load(f"images/{self.colour}_{self.type}.png")
        surface.blit(img, (self.x*75, self.y*75))

pieces = []
for i in range(8):
    pieces.append(Piece("black", i, 1, "pawn"))
    pieces.append(Piece("white", i, 6, "pawn"))

def main():
    pygame.init()

    logo = pygame.image.load("images/logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Chess")

    #Initalize screen with dimensions (640,640)
    screen = pygame.display.set_mode((640,640))

    #Create surface with dimensions (640,640)
    board = pygame.Surface((600, 600))
    #Fill board with colour
    board.fill((150, 111, 51))

    #Make every other rectangle light
    for x in range(0, 8, 2):
        for y in range(0, 8, 2):
            pygame.draw.rect(board, (210, 180, 140), (x*75, y*75, 75, 75))
            pygame.draw.rect(board, (210, 180, 140), ((x+1)*75, (y+1)*75, 75, 75))

    for piece in pieces:
        piece.draw(board)

    #Draws board onto screen, positioned at (20,20)
    screen.blit(board, (20, 20))

    #Update screen
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__== "__main__":
    main()