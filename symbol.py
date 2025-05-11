import pygame
from constants import *
class Symbol:
    def __init__(self,kind, x_pos, y_pos, size):
        self.kind = kind
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
        self.color = None

    def __eq__(self, other_symbol):
        if other_symbol is None:
            return False
        return self.kind == other_symbol.kind
        
    def draw(self, surface):
        cx, cy = self.x_pos + self.size // 2, self.y_pos + self.size // 2  

        if self.kind == 'X':
            self.color = RED
            offset = self.size // 3
            pygame.draw.line(surface, self.color, (cx - offset, cy - offset), (cx + offset, cy + offset), width=LINE_THICKNESS)
            pygame.draw.line(surface, self.color, (cx + offset, cy - offset), (cx - offset, cy + offset), width=LINE_THICKNESS)

        elif self.kind == 'O':
            self.color = BLUE
            radius = self.size // 3
            pygame.draw.circle(surface, self.color, (cx, cy), radius, LINE_THICKNESS)
