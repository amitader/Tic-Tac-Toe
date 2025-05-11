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
    not_win=True
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
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = event.pos
                if not_win and board.is_user_click_in_cell(x, y) and board.is_cell_empty(x, y):
                    
                    board.place_symbol(current_player, x, y)
                    not_win= not board.check_winner()
                    if not_win and board.get_cell_from_mouse(x,y):
                        current_player = O if current_player == X else X               
                        
                

        for row in board.cells_content:
            for cell in row:
                if cell:
                    cell.draw(grid_surface)
        screen.fill("white")
        screen.blit(grid_surface, (0, 0))
        if not_win:
            board.display_message(f"{current_player} turn")
        else:
            board.display_message(f"{current_player} win!!")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        



if __name__ == "__main__":
    main()