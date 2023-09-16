import pygame

def main():
    pygame.init()

    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Chess")

    #Initalize screen with dimensions (640,640)
    screen = pygame.display.set_mode((640,640))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__== "__main__":
    main()