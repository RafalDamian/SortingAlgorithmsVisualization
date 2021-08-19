import pygame
from pygame.constants import MOUSEBUTTONDOWN
from random import randint
from time import sleep

from Algorithms.list_generator import list_generator
from Algorithms.bubble_sort import bubble_sort
from Algorithms.insertion_sort import insertion_sort




class AlgorithmsVisualization:

    def __init__(self) -> None:
        '''game initialization and resources creation'''
        pygame.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption("Sorting Algorithms")
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.bg_color = (255,255,255)
        self.button_color = (0,0,255)
        self.text_color = (0,0,0)
        self.colums_color = (0,255,0)
        self.plus_color = (0,255,0)
        self.minus_color = (255,0,0)

        self.running = True
        self.sorting = False
        self.click = False
        
        self.algorithm = None
        self.number_of_colums = 10
        self.min_colums = 1
        self.max_colums = 25
        self.min_colums_h = 1
        self.max_colums_h = 99
        self.colums = list_generator(self.number_of_colums, self.min_colums_h, self.max_colums_h)

    def run_program(self):
        ''' main game loop initialization (opens main manu)'''
        x = self.screen_width / 2
        y = self.screen_height
        while self.running:
            (mx, my) = pygame.mouse.get_pos()
            self.screen.fill(self.bg_color)
            self._draw_text('CHOOSE ALGORITHM', 60, self.text_color, x, y*0.2)
            button_bubble = pygame.Rect((0.8*x, y*0.3), (0.4*x, 0.1*y))
            button_insertion = pygame.Rect((0.8*x, y*0.5), (0.4*x, 0.1*y))
            button_exit = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_bubble, self.button_color, 'BUBBLE SORT', 40, self.text_color)
            self._draw_button(button_insertion, self.button_color, 'INSERTION SORT', 40, self.text_color)
            self._draw_button(button_exit, self.button_color, 'EXIT', 40, self.text_color)

            if button_bubble.collidepoint((mx, my)):
                if self.click:
                    self.sorting = True
                    self.algorithm = bubble_sort
                    self._create_colums()
            
            if button_insertion.collidepoint((mx, my)):
                if self.click:
                    self.sorting = True
                    self.algorithm = insertion_sort
                    self._create_colums()

            if button_exit.collidepoint((mx, my)):
                if self.click:
                    self.running = False

            self._check_events()

            pygame.display.update()
        
        pygame.display.quit()
        pygame.quit()
        exit()

    def _create_colums(self):
        '''creating of colums that will be sorted by height'''
        x = self.screen_width / 2
        y = self.screen_height
        while self.sorting:
            (mx, my) = pygame.mouse.get_pos()

            self.screen.fill(self.bg_color)

            self._draw_text('CREATE COLUMS TO SORT BY THEIR HEIGHT', 60, self.text_color, x, y*0.15)

            self._draw_all_colums(self.colums)
        
            button_add_column = pygame.Rect((1.02*x, y*0.70), (0.15*x, 0.15*x))
            button_delete_column = pygame.Rect((0.83*x, y*0.70), (0.15*x, 0.15*x))
            self._draw_button(button_add_column, self.bg_color, '+', 190, self.plus_color)
            self._draw_button(button_delete_column, self.bg_color, '-', 190, self.minus_color)
            self._draw_button_circuit(button_add_column, self.plus_color)
            self._draw_button_circuit(button_delete_column, self.minus_color)
            button_randomize = pygame.Rect((0.8*x, y*0.85), (0.4*x, 0.1*y))
            self._draw_button(button_randomize, self.button_color, 'RANDOMIZE HEIGHT', 40, self.text_color)

            if button_add_column.collidepoint((mx, my)):
                if self.click and len(self.colums) < self.max_colums:
                    self.number_of_colums += 1
                    self.max_colums_h = self.number_of_colums * 2
                    self.colums.append(randint(self.min_colums_h,self.max_colums_h))
                    

            if button_delete_column.collidepoint((mx, my)):
                if self.click and len(self.colums) > self.min_colums:
                    self.number_of_colums -= 1
                    self.colums =  self.colums[:-1]
                    self.max_colums_h = self.number_of_colums * 2

            if button_randomize.collidepoint((mx, my)):
                if self.click:
                    self.colums = list_generator(len(self.colums), self.min_colums_h, self.max_colums_h)

            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            button_sort = pygame.Rect((1.5*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_menu, self.button_color, 'BACK TO MENU', 40, self.text_color)
            self._draw_button(button_sort, self.button_color, 'SORT THEM!', 40, self.text_color)

            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.sorting = False

            if button_sort.collidepoint((mx, my)):
                if self.click:
                    self._sort()



            self._check_events()

            pygame.display.update()

    def _sort(self):
        '''sorting algorithm visualization'''

        x = self.screen_width / 2
        y = self.screen_height
        to_sort = self.colums.copy()
        while self.sorting:

            (mx, my) = pygame.mouse.get_pos()

            self.screen.fill(self.bg_color)

            self._draw_text(f'SORTIG USING: SORT', 60, self.text_color, x, y*0.15)

            self._draw_all_colums(to_sort)

            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_menu, self.button_color, 'BACK TO MENU', 40, self.text_color)
            
            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.sorting = False

            button_next = pygame.Rect((1.5*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_next, self.button_color, 'NEXT', 40, self.text_color)
        

            if button_next.collidepoint((mx, my)):
                if self.click:
                    try:
                        next(self.algorithm(to_sort))
                    except StopIteration:
                        self._after_sorting(to_sort)

            self._check_events()
            pygame.display.update()

    def _after_sorting(self, to_sort):
        '''sorting algorithm visualization'''
        x = self.screen_width / 2
        y = self.screen_height
        while self.sorting:

            (mx, my) = pygame.mouse.get_pos()

            self.screen.fill(self.bg_color)

            self._draw_text(f'SORTIG COMPLETED USING: SORT', 60, self.text_color, x, y*0.15)

            self._draw_all_colums(to_sort)

            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_menu, self.button_color, 'BACK TO MENU', 40, self.text_color)
            
            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.sorting = False

            self._check_events()
            pygame.display.update()
        
    
    def _check_events(self):
        '''reaction to events generated by the keyboard and mouse inside menu'''
        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button:
                    self.click = True

    def _draw_text(self, text, font_size, color, x, y):
        '''draws given text in the given position'''
        font = pygame.font.SysFont(None, font_size)
        gen_text = font.render(text, 1, color)
        rect = gen_text.get_rect()
        rect.center = (x, y)
        self.screen.blit(gen_text, rect)

    def _draw_button(self, button, color, text, font_size, text_color):
        '''draws square with given text in the position of given button'''
        pygame.draw.rect(self.screen, color, button)
        (x, y) = button.center
        self._draw_text(text, font_size, text_color, x, y)

    def _draw_button_circuit(self, button, color):
        '''draws circuit of given button'''
        pygame.draw.rect(self.screen, color, button, 2, 8)

    def _draw_all_colums(self, colums):
        column_width = self.screen_width / 61
        starting_point = 30 * (column_width - len(colums) +1)
        for index, column in enumerate(colums):
            h = column*(0.50*self.screen_height)/100
            y = 0.65*self.screen_height-h
            x = starting_point+2*index*column_width
            self._draw_column(x, y, column_width, h, self.colums_color, str(column))

    def _draw_column(self, x, y, w, h, color, text=None):
        pygame.draw.rect(self.screen, color, pygame.Rect((x, y), (w, h)))
        if text:
            self._draw_text(text, 60, self.text_color, x+w*0.5, 0.67*self.screen_height)

if __name__ == '__main__':
    visual = AlgorithmsVisualization()
    visual.run_program()