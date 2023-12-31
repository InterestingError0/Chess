# Chatting with Chess - HTN 2023
# A chess program made with an entertaining assistant named Chester
# DH & RC
# September 17th 2023, ~3:30 A.M

# All necessary imports
import pygame
import pygame_textinput
import ptext
import openai

# OpenAI API Key (DON'T REMOVE!!!)
openai.api_key = "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"

# Class for chess pieces
class Piece:
    def __init__(self, colour, x, y, piece_type):
        self.colour = colour
        self.x = x
        self.y = y
        self.type = piece_type

    def draw(self, surface):
        img = pygame.image.load(f"images/{self.colour}_{self.type}.png")
        surface.blit(img, (self.x * 75, self.y * 75))


def main():
    pieces = []
    # Organizes the chess pieces on the board
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

    # All necessary variables needed
    pygame.init()

    message = ""

    logo = pygame.image.load("images/logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Chatting with Chess")

    textinput = pygame_textinput.TextInputVisualizer()

    textinput.font_color = (255, 255, 255)

    textinput.cursor_color = (255, 255, 255)

    textinput.cursor_width = 3

    textinput.font_object = pygame.font.Font(None, 25)

    # Initialize screen with dimensions (1240,640)
    screen = pygame.display.set_mode((1240, 640))

    # Create surface with dimensions (600,600)
    board = pygame.Surface((600, 600))

    textback = pygame.Surface((600, 60))

    outputback = pygame.Surface((580, 400))

    textback.fill((150, 150, 150))

    running = True

    piece_clicked_coords = [-1, -1]
    piece_clicked = pieces[0]

    keydown = True

    drawing = 20

    whites_move = True

    # Main loop
    while running:
        screen.fill((100, 100, 100))

        events = pygame.event.get()

        illegal_move = False

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if piece_clicked_coords == [-1, -1]:
                    mouse_pos = pygame.mouse.get_pos()

                    x = (mouse_pos[0] - 20) // 75
                    y = (mouse_pos[1] - 20) // 75

                    for piece in pieces:
                        if piece.x == x and piece.y == y:
                            if whites_move and piece.colour == "black" or not whites_move and piece.colour == "white":
                                break
                            piece_clicked_coords = [x, y]
                            piece_clicked = piece
                else:
                    new_mouse_pos = pygame.mouse.get_pos()

                    x = (new_mouse_pos[0] - 20) // 75
                    y = (new_mouse_pos[1] - 20) // 75

                    if (x > 7 or y > 7) or (x < 0 or y < 0):
                        illegal_move = True

                    if piece_clicked.type == "rook":
                        if not (piece_clicked.x == x or piece_clicked.y == y):
                            break

                        if x > piece_clicked.x:
                            for i in range(piece_clicked.x + 1, x):
                                if illegal_move:
                                    break

                                for piece in pieces:
                                    if piece.x == i and piece.y == y:
                                        illegal_move = True
                                        break
                        elif x < piece_clicked.x:
                            for i in range(x, piece_clicked.x - 1):
                                if illegal_move:
                                    break

                                for piece in pieces:
                                    if piece.x == i and piece.y == y:
                                        illegal_move = True
                                        break
                        elif y > piece_clicked.y:
                            for i in range(piece_clicked.y + 1, y):
                                if illegal_move:
                                    break

                                for piece in pieces:
                                    if piece.y == i and piece.x == x:
                                        illegal_move = True
                                        break
                        elif y < piece_clicked.y:
                            for i in range(y + 1, piece_clicked.y):
                                if illegal_move:
                                    break

                                for piece in pieces:
                                    if piece.y == i and piece.x == x:
                                        illegal_move = True
                                        break
                    if piece_clicked.type == "bishop":
                        for i in range(1, 8):
                            if (piece_clicked.x + i == x or piece_clicked.x - i == x) and (
                                    piece_clicked.y + i == y or piece_clicked.y - i == y):
                                break
                        else:
                            illegal_move = True
                        if x > piece_clicked.x and y > piece_clicked.y:
                            for i in range(1, 8):
                                if illegal_move:
                                    break

                                for piece in pieces:
                                    if piece.x == piece_clicked.x + (x - i) and piece.y == piece_clicked.y + (x - i):
                                        illegal_move = True
                                        break
                        elif x > piece_clicked.x and y < piece_clicked.y:
                            for i in range(1, 8):
                                if illegal_move:
                                    break

                                for piece in pieces:
                                    if piece.x == piece_clicked.x + (x - i) and piece.y == piece_clicked.y - (x - i):
                                        illegal_move = True
                                        break
                        elif x < piece_clicked.x and y > piece_clicked.y:
                            for i in range(1, 8):
                                if illegal_move:
                                    break

                                for piece in pieces:
                                    if piece.x == piece_clicked.x - i and piece.y == piece_clicked.y + i:
                                        illegal_move = True
                                        break
                        elif x < piece_clicked.x and y < piece_clicked.y:
                            for i in range(1, 8):
                                if illegal_move:
                                    break

                                for piece in pieces:
                                    if piece.x == piece_clicked.x - i and piece.y == piece_clicked.y - i:
                                        illegal_move = True
                                        break

                    if piece_clicked.type == "knight":
                        if not (((piece_clicked.x + 2 == x or piece_clicked.x - 2 == x) and (
                                piece_clicked.y + 1 == y or piece_clicked.y - 1 == y)) or (
                                        (piece_clicked.x + 1 == x or piece_clicked.x - 1 == x) and (
                                         piece_clicked.y + 2 == y or piece_clicked.y - 2 == y))):
                            illegal_move = True
                    if piece_clicked.type == "king":
                        if not ((piece_clicked.x + 1 == x or piece_clicked.x - 1 == x or piece_clicked.x == x) and (
                                piece_clicked.y + 1 == y or piece_clicked.y - 1 == y or piece_clicked.y == y)):
                            illegal_move = True
                    if piece_clicked.type == "queen":
                        if not (piece_clicked.x == x or piece_clicked.y == y):
                            for i in range(1, 8):
                                if (piece_clicked.x + i == x or piece_clicked.x - i == x) and (
                                        piece_clicked.y + i == y or piece_clicked.y - i == y):
                                    break
                            else:
                                illegal_move = True
                        if piece_clicked.x == x or piece_clicked.y == y:
                            if x > piece_clicked.x:
                                for i in range(piece_clicked.x + 1, x):
                                    if illegal_move:
                                        break

                                    for piece in pieces:
                                        if piece.x == i and piece.y == y:
                                            illegal_move = True
                                            break
                            elif x < piece_clicked.x:
                                for i in range(x, piece_clicked.x - 1):
                                    if illegal_move:
                                        break

                                    for piece in pieces:
                                        if piece.x == i and piece.y == y:
                                            illegal_move = True
                                            break
                            elif y > piece_clicked.y:
                                for i in range(piece_clicked.y + 1, y):
                                    if illegal_move:
                                        break

                                    for piece in pieces:
                                        if piece.y == i and piece.x == x:
                                            illegal_move = True
                                            break
                            elif y < piece_clicked.y:
                                for i in range(y + 1, piece_clicked.y):
                                    if illegal_move:
                                        break

                                    for piece in pieces:
                                        if piece.y == i and piece.x == x:
                                            illegal_move = True
                                            break
                        else:
                            if x > piece_clicked.x and y > piece_clicked.y:
                                for i in range(1, 8):
                                    if illegal_move:
                                        break

                                    for piece in pieces:
                                        if piece.x == piece_clicked.x + (x - i) and piece.y == piece_clicked.y + (
                                                x - i):
                                            illegal_move = True
                                            break
                            elif x > piece_clicked.x and y < piece_clicked.y:
                                for i in range(1, 8):
                                    if illegal_move:
                                        break

                                    for piece in pieces:
                                        if piece.x == piece_clicked.x + (x - i) and piece.y == piece_clicked.y - (
                                                x - i):
                                            illegal_move = True
                                            break
                            elif x < piece_clicked.x and y > piece_clicked.y:
                                for i in range(1, 8):
                                    if illegal_move:
                                        break

                                    for piece in pieces:
                                        if piece.x == piece_clicked.x - i and piece.y == piece_clicked.y + i:
                                            illegal_move = True
                                            break
                            elif x < piece_clicked.x and y < piece_clicked.y:
                                for i in range(1, 8):
                                    if illegal_move:
                                        break

                                    for piece in pieces:
                                        if piece.x == piece_clicked.x - i and piece.y == piece_clicked.y - i:
                                            illegal_move = True
                                            break

                    if piece_clicked.type == "pawn":
                        if piece_clicked.colour == "white":
                            if piece_clicked.y == 6:
                                # Allow pawn to move 2 squares on it's first move
                                if not (piece_clicked.y - 2 == y and piece_clicked.x == x):
                                    for piece in pieces:
                                        # Allow pawn to capture pieces that are one square away and diagonal to it on
                                        # it's first move
                                        if piece_clicked.y - 1 == y and (
                                                piece.x == piece_clicked.x + 1 or piece.x == piece_clicked.x - 1):
                                            break
                                    else:
                                        illegal_move = True
                            else:
                                # Prevent a pawn from moving more than one square if it had already moved
                                if not piece_clicked.y - 1 == y:
                                    illegal_move = True
                                for piece in pieces:
                                    # Prevent pawn from capturing a piece in front of it
                                    if piece_clicked.y - 1 == piece.y and piece_clicked.x == piece.x:
                                        illegal_move = True
                                # Allow pawn to capture pieces that are one square away and diagonal to it
                                for piece in pieces:
                                    if piece_clicked.y - 1 == y and (
                                            piece.x == piece_clicked.x + 1 or piece.x == piece_clicked.x - 1):
                                        break

                        elif piece_clicked.colour == "black":
                            if piece_clicked.y == 1:
                                # Allow pawn to move 2 squares on it's first move
                                if not (piece_clicked.y + 2 == y and piece_clicked.x == x or piece_clicked.y + 1 == y):
                                    for piece in pieces:
                                        # Allow pawn to capture pieces that are one square away and diagonal to it on
                                        # it's first move
                                        if piece_clicked.y + 1 == y and (
                                                piece.x == piece_clicked.x + 1 or piece.x == piece_clicked.x - 1):
                                            break
                                    else:
                                        illegal_move = True
                            else:
                                # Prevent a pawn from moving more than one square if it had already moved
                                if not piece_clicked.y + 1 == y:
                                    illegal_move = True
                                for piece in pieces:
                                    # Prevent pawn from capturing a piece in front of it
                                    if piece_clicked.y + 1 == piece.y and piece_clicked.x == piece.x and y == piece.y and x == piece.x:
                                        illegal_move = True
                                # Allow pawn to capture pieces that are one square away and diagonal to it
                                for piece in pieces:
                                    if piece_clicked.y + 1 == y and (
                                            piece.x == piece_clicked.x + 1 or piece.x == piece_clicked.x - 1):
                                        break

                    if illegal_move:
                        piece_clicked_coords = [-1, -1]
                        break

                    for piece in pieces:
                        if piece.x == x and piece.y == y:
                            if piece.colour != piece_clicked.colour:
                                pieces.remove(piece)
                            elif piece.colour == piece_clicked.colour:
                                illegal_move = True
                                break

                    if illegal_move:
                        piece_clicked_coords = [-1, -1]
                        break

                    whites_move = not whites_move

                    piece_clicked.x = x
                    piece_clicked.y = y

                    piece_clicked_coords = [-1, -1]

            if event.type == pygame.QUIT:
                running = False

            # Used for textbox inputting
            if event.type == pygame.KEYDOWN and keydown:
                if event.key == pygame.K_RETURN:
                    message = textinput.value
                    textinput.value = ""
                    drawing += 40
                keydown = False
            if event.type == pygame.KEYUP and not keydown:
                keydown = True

        # Fill board with colour
        board.fill((150, 111, 51))
        # Make every other rectangle light
        for x in range(0, 8, 2):
            for y in range(0, 8, 2):
                pygame.draw.rect(board, (210, 180, 140), (x * 75, y * 75, 75, 75))
                pygame.draw.rect(board, (210, 180, 140), ((x + 1) * 75, (y + 1) * 75, 75, 75))

        for piece in pieces:
            piece.draw(board)

        # ChatGPT query to get a response based on a question that someone asks
        if message != "":
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Stick to the topic of chess and provide commentary given chess-related information. Otherwise, ignore it. As well, keep commentary to 10 words or less and be spicy. Your name is Chester and don't let anyone tell you otherwise!"},
                    {"role": "user", "content": message}
                ]
            )
            # Draws the text in the text box and clears the message so no duplicate messages are sent
            ptext.draw("\nYou: %s \n Chester: %s" % (message, (response["choices"][0]["message"]["content"])),
                       (20, drawing), fontsize=20, surf=outputback)

            message = ""

        # Writes everything to screen and refreshes
        textinput.update(events)

        screen.blit(outputback, (650, 50))

        screen.blit(textback, (630, 550))

        screen.blit(textinput.surface, (630, 550))

        # Draws board onto screen, positioned at (20,20)
        screen.blit(board, (20, 20))

        # Update screen
        pygame.display.flip()


def is_king_under_attack(whites_move, pieces):
    if whites_move:
        whites_king_x = -1
        whites_king_y = -1
        for x in pieces:
            if x.type == "king" and x.colour == "white":
                whites_king_x = x.x
                whites_king_y = x.y
                break
        for piece in pieces:
            if piece.type == "rook" and piece.colour == "black":
                if piece.x == whites_king_x:
                    return True
                elif piece.y == whites_king_y:
                    return True
            elif piece.type == "bishop" and piece.colour == "black":
                for i in range(8):
                    if (piece.x + i == whites_king_x or piece.x - i == whites_king_x) and (
                            piece.y + i == whites_king_y or piece.y - i == whites_king_y):
                        return True
            elif piece.type == "knight" and piece.colour == "black":
                if ((piece.x + 2 == whites_king_x or piece.x - 2 == whites_king_x) and (
                        piece.y + 1 == whites_king_y or piece.y - 1 == whites_king_y)) or (
                        (piece.x + 1 == whites_king_x or piece.x - 1 == whites_king_x) and (
                        piece.y + 2 == whites_king_y or piece.y - 2 == whites_king_y)):
                    return True
            elif piece.type == "queen" and piece.colour == "black":
                if not (piece.x == whites_king_x or piece.y == whites_king_y):
                    for i in range(1, 8):
                        if (piece.x + i == whites_king_x or piece.x - i == whites_king_x) and (
                                piece.y + i == whites_king_y or piece.y - i == whites_king_y):
                            return True
            elif piece.type == "pawn" and piece.colour == "black":
                if piece.y + 1 == whites_king_y and (whites_king_x == piece.x + 1 or piece.x == whites_king_x - 1):
                    return True
    elif not whites_move:
        black_king_x = -1
        black_king_y = -1
        for x in pieces:
            if x.type == "king" and x.colour == "black":
                black_king_x = x.x
                black_king_y = x.y
                break
        for piece in pieces:
            if piece.type == "rook" and piece.colour == "white":
                if piece.x == black_king_x:
                    return True
                elif piece.y == black_king_y:
                    return True
            elif piece.type == "bishop" and piece.colour == "white":
                for i in range(8):
                    if (piece.x + i == black_king_x or piece.x - i == black_king_x) and (
                            piece.y + i == black_king_y or piece.y - i == black_king_y):
                        return True
            elif piece.type == "knight" and piece.colour == "white":
                if ((piece.x + 2 == black_king_x or piece.x - 2 == black_king_x) and (
                        piece.y + 1 == black_king_y or piece.y - 1 == black_king_y)) or (
                        (piece.x + 1 == black_king_x or piece.x - 1 == black_king_x) and (
                        piece.y + 2 == black_king_y or piece.y - 2 == black_king_y)):
                    return True
            elif piece.type == "queen" and piece.colour == "white":
                if not (piece.x == black_king_x or piece.y == black_king_y):
                    for i in range(1, 8):
                        if (piece.x + i == black_king_x or piece.x - i == black_king_x) and (
                                piece.y + i == black_king_y or piece.y - i == black_king_y):
                            return True
            elif piece.type == "pawn" and piece.colour == "white":
                if piece.y - 1 == black_king_y and (black_king_x == piece.x - 1 or piece.x == black_king_x + 1):
                    return True


if __name__ == "__main__":
    main()
