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

# define the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # BEGIN response from second question
            # get the coordinates of the click
            x, y = event.pos
            # calculate the corresponding cell on the game board
            cell_x = x // 133
            cell_y = y // 133
            # check if the cell is empty
            if board[cell_y][cell_x] == 0:
                # draw an X
                board[cell_y][cell_x] = 1
                # update the display
                pygame.display.flip()

    # clear the screen
    screen.fill(white)

    # draw the game board
    for y in range(3):
        for x in range(3):
            if board[y][x] == 0:
                pygame.draw.rect(screen, black, (x*133, y*133, 133, 133), 2)
            elif board[y][x] == 1:
                pygame.draw.line(screen, black, (x*133, y*133), ((x+1)*133, (y+1)*133), 2)
                pygame.draw.line(screen, black, ((x+1)*133, y*133), (x*133, (y+1)*133), 2)
            else:
                pygame.draw.circle(screen, black, (int((x+0.5)*133), int((y+0.5)*133)), int(133/2), 2)

    # update the display
    pygame.display.flip()

# close the game
pygame.quit()
