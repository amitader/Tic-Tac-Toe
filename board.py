import pygame
from constants import *
from symbol import Symbol
class Board:
    def __init__(self,screen, num_row,num_cul, color=BLACK):
        self.screen=screen
        self.num_row=num_row
        self.num_cul=num_cul
        self.color=color
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
            pygame.draw.line(surface,self.color,(x, PADDING),(x , PADDING+row_size), LINE_THICKNESS)
        
        for i in range(self.num_cul +1):
            y = PADDING + (i * CELL_SIZE)
            pygame.draw.line(surface,self.color,(PADDING , y),(PADDING + cul_size, y), LINE_THICKNESS)
    def place_symbol(self, kind, x, y ):
         x_pos,y_pose = self.get_cell_from_mouse(x, y)
         if x_pos is not None and y_pose is not None and self.cells_content[y_pose][x_pos] is None:
            self.cells_content[y_pose][x_pos]=Symbol(kind, PADDING + (x_pos * CELL_SIZE), PADDING +(y_pose * CELL_SIZE), CELL_SIZE)
    
    def get_cell_from_mouse(self, x, y):
        if PADDING <= x and x < (PADDING + (self.num_cul * CELL_SIZE)) and PADDING <= y and y < (PADDING + (self.num_row * CELL_SIZE)):
            col = (x - PADDING) // CELL_SIZE
            row = (y - PADDING) // CELL_SIZE
            return col, row
        return None, None
    
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
        return False
    def display_message(self,message, color):
        x = SCREEN_WIDTH - (PADDING * 2)
        y= PADDING
        font = pygame.font.SysFont(TEXT_FONT, 30)
        score_text = font.render(message, True, color)
        self.screen.blit(score_text, (x, y)) 
        
