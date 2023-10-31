import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 300, 300
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# Fonts
FONT = pygame.font.Font(None, 100)

# Initialize game variables
board = [["" for _ in range(3)] for _ in range(3)]
player_turn = "X"
game_over = False

# Draw the grid
def draw_grid():
    for row in range(1, 3):
        pygame.draw.line(win, LINE_COLOR, (0, row * HEIGHT // 3), (WIDTH, row * HEIGHT // 3), 5)
        pygame.draw.line(win, LINE_COLOR, (row * WIDTH // 3, 0), (row * WIDTH // 3, HEIGHT), 5)

# Draw X and O symbols
def draw_symbols():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(win, LINE_COLOR, (col * WIDTH // 3, row * HEIGHT // 3), ((col + 1) * WIDTH // 3, (row + 1) * HEIGHT // 3), 5)
                pygame.draw.line(win, LINE_COLOR, ((col + 1) * WIDTH // 3, row * HEIGHT // 3), (col * WIDTH // 3, (row + 1) * HEIGHT // 3), 5)
            elif board[row][col] == "O":
                pygame.draw.circle(win, LINE_COLOR, (col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6), WIDTH // 6, 5)

# Check for a win or draw
def check_winner():
    for row in range(3):
        if all(cell == player_turn for cell in board[row]):
            return True

    for col in range(3):
        if all(board[row][col] == player_turn for row in range(3)):
            return True

    if all(board[i][i] == player_turn for i in range(3)) or all(board[i][2 - i] == player_turn for i in range(3)):
        return True

    if all(cell != "" for row in board for cell in row):
        return "draw"

    return False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // (HEIGHT // 3)
            clicked_col = mouseX // (WIDTH // 3)

            if board[clicked_row][clicked_col] == "":
                board[clicked_row][clicked_col] = player_turn
                winner = check_winner()
                if winner:
                    if winner == "draw":
                        print("It's a draw!")
                    else:
                        print(f"Player {player_turn} wins!")
                    game_over = True
                else:
                    player_turn = "O" if player_turn == "X" else "X"

    win.fill(WHITE)
    draw_grid()
    draw_symbols()
    pygame.display.update()
