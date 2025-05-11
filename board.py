import pygame
from constants import *
from symbol import Symbol
class Board:
    def __init__(self,screen, num_row,num_cul):
        self.screen=screen
        self.num_row=num_row
        self.num_cul=num_cul
        self.current_symbol_color=RED
        self.cells_content=[[None for _ in range(self.num_row)] for _ in range(self.num_cul)]

    def create_static_grid_surface(self):
        surface = pygame.Surface((self.num_cul * CELL_SIZE + 55, self.num_row * CELL_SIZE + 55))
        surface.fill(WHITE)  
        self.draw_board(surface)
        return surface

    def draw_board(self, surface):
        row_size = CELL_SIZE * self.num_row
        cul_size=CELL_SIZE * self.num_cul
        for i in range(self.num_row +1):
            x = PADDING + (i * CELL_SIZE)
            pygame.draw.line(surface,BLACK,(x, PADDING),(x , PADDING+row_size), LINE_THICKNESS)
        
        for i in range(self.num_cul +1):
            y = PADDING + (i * CELL_SIZE)
            pygame.draw.line(surface,BLACK,(PADDING , y),(PADDING + cul_size, y), LINE_THICKNESS)
    def place_symbol(self, kind, x, y ):
         if self.is_user_click_in_cell(x, y) and self.is_cell_empty(x, y):
            x_pos,y_pose = self.get_cell_from_mouse(x, y)
            self.cells_content[y_pose][x_pos]=Symbol(kind, PADDING + (x_pos * CELL_SIZE), PADDING +(y_pose * CELL_SIZE), CELL_SIZE)
            
    
    def is_user_click_in_cell(self, x, y):
        return PADDING <= x and x < (PADDING + (self.num_cul * CELL_SIZE)) and PADDING <= y and y < (PADDING + (self.num_row * CELL_SIZE))
    
    def is_cell_empty(self, x, y):
        col, row= self.get_cell_from_mouse(x, y)
        return self.cells_content[row][col] is None
    
    def get_cell_from_mouse(self, x, y):
        col = (x - PADDING) // CELL_SIZE
        row = (y - PADDING) // CELL_SIZE
        return col, row

    
    def check_winner(self):
        for i in range(self.num_row):
            if self.cells_content[i][0] == self.cells_content[i][1] == self.cells_content[i][2] !=None:
                return True
            if self.cells_content[0][i] == self.cells_content[1][i] == self.cells_content[2][i] !=None:
                return True
        if self.cells_content[0][0] == self.cells_content[1][1] == self.cells_content[2][2] !=None:
            return True
        if self.cells_content[0][2] == self.cells_content[1][1] == self.cells_content[2][0] !=None:
            return True
        self.current_symbol_color = BLUE if self.current_symbol_color == RED else RED
        return False
    
    def check_draw(self):
        for row in self.cells_content:
            for cell in row:
                if cell is None:
                    return False  
        return True  
    def display_message(self,message):
        x = SCREEN_WIDTH - (PADDING * 3)
        y= PADDING
        font = pygame.font.SysFont(TEXT_FONT, 30)
        score_text = font.render(message, True, self.current_symbol_color)
        self.screen.blit(score_text, (x, y)) 
        
