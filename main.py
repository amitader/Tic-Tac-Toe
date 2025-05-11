import pygame
from constants import *
from board import Board
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()
    symbols=[]
    current_player=X
    color = RED
    board= Board(screen, 3, 3)
    grid_surface = board.create_static_grid_surface()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
            if event.type == pygame.MOUSEBUTTONUP and not board.check_winner():
                x,y = event.pos
                board.place_symbol(current_player, x, y)
                if not board.check_winner():
                    current_player = O if current_player == X else X
                    color = BLUE if color == RED else RED

        for row in board.cells_content:
            for cell in row:
                if cell:
                    cell.draw(grid_surface)
        screen.fill("white")
        screen.blit(grid_surface, (0, 0))
        if not board.check_winner():
            board.display_message(f"{current_player} turn", color)
        else:
            board.display_message(f"{current_player} win!!", color)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        



if __name__ == "__main__":
    main()