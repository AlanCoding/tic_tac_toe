import pygame

# initialize pygame
pygame.init()

# set up the display
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic-Tac-Toe")

# define colors
white = (255, 255, 255)
black = (0, 0, 0)

# create a 2D array to represent the game board
board = [[0 for x in range(3)] for y in range(3)]

whos_turn = 1
game_over = False

# define the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif game_over:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:  # BEGIN response from second question
            # get the coordinates of the click
            x, y = event.pos
            # calculate the corresponding cell on the game board
            cell_x = x // 133
            cell_y = y // 133
            # check if the cell is empty
            if board[cell_y][cell_x] == 0:
                # draw an X
                board[cell_y][cell_x] = whos_turn
                if whos_turn == 1:
                    whos_turn = 2
                else:
                    whos_turn = 1
                # update the display
                pygame.display.flip()
        # END response from second question

    # clear the screen
    screen.fill(white)

    # draw the game board
    for y in range(3):
        for x in range(3):
            pygame.draw.rect(screen, black, (x*133, y*133, 133, 133), 2)
            if board[y][x] == 0:
                pass
            elif board[y][x] == 1:
                pygame.draw.line(screen, black, (x*133, y*133), ((x+1)*133, (y+1)*133), 2)
                pygame.draw.line(screen, black, ((x+1)*133, y*133), (x*133, (y+1)*133), 2)
            else:
                pygame.draw.circle(screen, black, (int((x+0.5)*133), int((y+0.5)*133)), int(133/2), 2)

    if not game_over:
        # BEGIN response from third question
        # check rows
        for row in board:
            if all(val == 1 for val in row):
                # draw a line across the top of the row
                pygame.draw.line(screen, black, (0, board.index(row)*133), (400, board.index(row)*133), 5)
                print("X wins!")
                game_over = True
            elif all(val == 2 for val in row):
                # draw a line across the top of the row
                pygame.draw.line(screen, black, (0, board.index(row)*133), (400, board.index(row)*133), 5)
                print("O wins!")
                game_over = True

        # check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == 1:
                # draw a line down the left side of the column
                pygame.draw.line(screen, black, (col*133, 0), (col*133, 400), 5)
                print("X wins!")
                game_over = True
            elif board[0][col] == board[1][col] == board[2][col] == 2:
                # draw a line down the left side of the column
                pygame.draw.line(screen, black, (col*133, 0), (col*133, 400), 5)
                print("O wins!")
                game_over = True

        # check diagonals
        if board[0][0] == board[1][1] == board[2][2] == 1:
            # draw a line from top-left to bottom-right
            pygame.draw.line(screen, black, (0, 0), (400, 400), 5)
            print("X wins!")
            game_over = True
        elif board[0][0] == board[1][1] == board[2][2] == 2:
            # draw a line from top-left to bottom-right
            pygame.draw.line(screen, black, (0, 0), (400, 400), 5)
            print("O wins!")
            game_over = True

        if board[0][2] == board[1][1] == board[2][0] == 1:
            # draw a line from top-right to bottom-left
            pygame.draw.line(screen, black, (400, 0), (0, 400), 5)
            print("X wins!")
            game_over = True
        elif board[0][2] == board[1][1] == board[2][0] == 2:
            # draw a line from top-right to bottom-left
            pygame.draw.line(screen, black, (400, 0), (0, 400), 5)
            print("O wins!")
            game_over = True
        # END response from third question

    # update the display
    pygame.display.flip()

# close the game
pygame.quit()
