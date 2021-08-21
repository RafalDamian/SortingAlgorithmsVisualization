import pygame
from pygame.constants import MOUSEBUTTONDOWN
from random import randint
from time import sleep

from Algorithms.list_generator import list_generator
from Algorithms.bubble_sort import bubble_sort
from Algorithms.insertion_sort import insertion_sort
from Algorithms.merge_sort import merge_sort
from settings import Settings


class AlgorithmsVisualization:

    def __init__(self) -> None:
        '''game initialization and resources creation'''
        pygame.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption("Sorting Algorithms")
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.running = True
        self.sorting = False
        self.click = False
        self.action = False
        self.typing = False
        self.temporary_number_of_colums = None

        self.settings = Settings()
        
        self.algorithm = None
        self.algorithm_name = None
        self.number_of_colums = 100
        self.colums = list_generator(self.number_of_colums, self.settings.min_colums_h, self.settings.max_colums_h)

    def run_program(self):
        ''' main game loop initialization (opens main manu)'''
        x = self.screen_width / 2
        y = self.screen_height
        while self.running:
            (mx, my) = pygame.mouse.get_pos()
            self.screen.fill(self.settings.bg_color)
            self._draw_text('CHOOSE AN ALGORITHM', 60, self.settings.text_color, x, y*0.20)
            button_bubble = pygame.Rect((0.8*x, y*0.25), (0.4*x, 0.1*y))
            button_insertion = pygame.Rect((0.8*x, y*0.4), (0.4*x, 0.1*y))
            button_merge = pygame.Rect((0.8*x, y*0.55), (0.4*x, 0.1*y))
            button_exit = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_bubble, self.settings.button_color, 'BUBBLE SORT', 40, self.settings.text_color)
            self._draw_button(button_insertion, self.settings.button_color, 'INSERTION SORT', 40, self.settings.text_color)
            self._draw_button(button_merge, self.settings.button_color, 'MERGE SORT', 40, self.settings.text_color)
            self._draw_button(button_exit, self.settings.button_color, 'EXIT', 40, self.settings.text_color)

            if button_bubble.collidepoint((mx, my)):
                if self.click:
                    self.sorting = True
                    self.algorithm = bubble_sort
                    self.algorithm_name = 'bubble sort'
                    self._create_colums()
            
            if button_insertion.collidepoint((mx, my)):
                if self.click:
                    self.sorting = True
                    self.algorithm = insertion_sort
                    self.algorithm_name = 'insertion sort'
                    self._create_colums()

            if button_merge.collidepoint((mx, my)):
                if self.click:
                    self.sorting = True
                    self.algorithm = merge_sort
                    self.algorithm_name = 'merge sort'
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
            self.screen.fill(self.settings.bg_color)

            if self.typing:
                self._change_number_of_colums(self.temporary_number_of_colums)
                self.action = False
        
            button_add_column = pygame.Rect((1.15*x, y*0.78), (0.15*x, 0.15*x))
            button_delete_column = pygame.Rect((0.70*x, y*0.78), (0.15*x, 0.15*x))
            self._draw_button(button_add_column, self.settings.bg_color, '+', 190, self.settings.plus_color)
            self._draw_button(button_delete_column, self.settings.bg_color, '-', 190, self.settings.minus_color)
            self._draw_button_circuit(button_add_column, self.settings.plus_color)
            self._draw_button_circuit(button_delete_column, self.settings.minus_color)
            button_randomize = pygame.Rect((0.87*x, y*0.79+0.075*x), (0.26*x, 0.070*x))
            self._draw_button(button_randomize, self.settings.button_color, 'RANDOMIZE HEIGHT', 30, self.settings.text_color)
            button_number_of_colums = pygame.Rect((0.87*x, y*0.78), (0.26*x, 0.075*x))
            if not self.typing:
                self._draw_button(button_number_of_colums, self.settings.bg_color, f'{self.number_of_colums}', 100, self.settings.text_color)
            else:
                self._draw_button(button_number_of_colums, self.settings.bg_color, f'{self.temporary_number_of_colums}', 100, self.settings.text_color)
            self._draw_button_circuit(button_number_of_colums, self.settings.text_color)

            if button_add_column.collidepoint((mx, my)):
                if self.click and len(self.colums) < self.settings.max_colums:
                    self.number_of_colums += 1
                    self.colums.append(randint(self.settings.min_colums_h,self.settings.max_colums_h))
                    
            if button_delete_column.collidepoint((mx, my)):
                if self.click and len(self.colums) > self.settings.min_colums:
                    self.number_of_colums -= 1
                    self.colums =  self.colums[:-1]

            if button_randomize.collidepoint((mx, my)):
                if self.click:
                    self.colums = list_generator(len(self.colums), self.settings.min_colums_h, self.settings.max_colums_h)

            if button_number_of_colums.collidepoint((mx, my)):
                if self.click:
                    self.temporary_number_of_colums = self.number_of_colums
                    self.typing = True

            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            button_sort = pygame.Rect((1.5*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_menu, self.settings.button_color, 'BACK TO MENU', 40, self.settings.text_color)
            self._draw_button(button_sort, self.settings.button_color, 'SORT THEM!', 40, self.settings.text_color)

            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.sorting = False

            if button_sort.collidepoint((mx, my)):
                if self.click:
                    self._sort()

            self._draw_text('CREATE COLUMS TO SORT BY THEIR HEIGHT', 60, self.settings.text_color, x, y*0.15)
            self._draw_all_colums(self.colums)
            self._check_events()
            pygame.display.update()

    def _sort(self):
        '''sorting algorithm visualization'''
        x = self.screen_width / 2
        y = self.screen_height
        to_sort = self.colums.copy()
        sorted = False
        self.algorithm = self.algorithm(to_sort)
        while self.sorting:
            (mx, my) = pygame.mouse.get_pos()
            self.screen.fill(self.settings.bg_color)

            if not sorted:
                try:
                    next(self.algorithm)
                    sleep(1/self.number_of_colums)
                except StopIteration:
                    sorted = True
                header= f'SORTIG USING: {self.algorithm_name.upper()}'
            else:
                header= f'SORTIG COMPLETED USING: {self.algorithm_name.upper()}'

            button_menu = pygame.Rect((0.1*x, y*0.8), (0.4*x, 0.1*y))
            self._draw_button(button_menu, self.settings.button_color, 'BACK TO MENU', 40, self.settings.text_color)
            if button_menu.collidepoint((mx, my)):
                if self.click:
                    self.sorting = False

            self._draw_all_colums(to_sort)
            self._draw_text(header, 60, self.settings.text_color, x, y*0.15)
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
        column_width = 0.95 * self.screen_width / (2 * self.number_of_colums + 1)
        starting_point = column_width + 0.025 * self.screen_width
        for index, column in enumerate(colums):
            h = column * 0.50 * self.screen_height / self.settings.max_colums_h
            y = 0.68 * self.screen_height - h
            x = starting_point + 2 * index * column_width
            self._draw_column(x, y, column_width, h, self.settings.colums_color)

    def _draw_column(self, x, y, w, h, color, text=None):
        pygame.draw.rect(self.screen, color, pygame.Rect((x, y), (w, h)))
        if text:
            self._draw_text(text, 20, self.settings.text_color, x+w*0.5, 0.67*self.screen_height)

    def _change_number_of_colums(self, number):
        '''changes number of colums'''
        number = str(number)
        number_keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
        pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,]
        while self.action == False:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                            if event.button:
                                self.typing = False
                                self.action = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.typing = False
                        self.action = True
                    elif event.key == pygame.K_BACKSPACE:
                        if len(number) > 0:
                            number = number[:-1]
                            self.action = True
                            self.temporary_number_of_colums = number
                    elif len(number) <= 3 and event.key in number_keys: 
                        number += event.unicode
                        self.action = True
                        self.temporary_number_of_colums = number
        if not self.typing:
            try:
                colums = int(self.temporary_number_of_colums)
                if colums < self.settings.min_colums:
                    colums = self.settings.min_colums
                elif colums > self.settings.max_colums:
                    colums = self.settings.max_colums
                if colums < self.number_of_colums:
                    self.colums = self.colums[:colums]
                    self.number_of_colums = colums
                else:
                    for _ in range(colums-self.number_of_colums):
                        self.colums.append(randint(self.settings.min_colums_h, self.settings.max_colums_h))
                    self.number_of_colums = colums
            except ValueError:
                pass


if __name__ == '__main__':
    visual = AlgorithmsVisualization()
    visual.run_program()