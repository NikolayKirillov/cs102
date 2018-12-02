import random
from copy import deepcopy

import pygame
from pygame.locals import *


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        self.clist = deepcopy(self.cell_list (randomize = True))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.draw_cell_list(self.clist)

            # рисуется сетка
            self.draw_grid()

            # обновить клетки
            self.update_cell_list(self.clist)

            # обновить полный экран
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize: bool = True) -> tuple:
        """ Создание списка клеток.

        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        self.clist = []
        for row in range(self.cell_height):
        	list_width = []
        	for col in range(self.cell_width):
        		if randomize:
        			value = random.randint(0, 1)
        		else:
        			value = 0
        		list_width.append(value)
        	self.clist.append(list_width)
        return self.clist

    def draw_cell_list(self, rects: list) -> None:
        """ Отображение списка клеток
        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        x = 0
        y = 0
        for row in range(self.cell_height):
            x = 0
            # перебор элементов внутреннего списка
            for col in range(self.cell_width):
                # создание ячейки rect для внутреннего списка
                rect1 = pygame.Rect((x, y, self.cell_size, self.cell_size))
                # закрасить ячейку нужным цветом
                if rects[row][col]:
                    pygame.draw.rect(self.screen, pygame.Color('green'), rect1)
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), rect1)

                # увеличение значения по оси x
                x += self.cell_size

            # увеличение значения по оси y
            y += self.cell_size
    def get_neighbours(self, cell: tuple) -> list:
        """ Вернуть список соседей для указанной ячейки
        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        neighbours = []
        row = cell[0]
        col = cell[1]

        if col < (self.cell_width - 1):
            neighbours.append(self.clist[row][col + 1])
        if row > 0:
            neighbours.append(self.clist[row - 1][col])
        if row < (self.cell_height - 1):
            neighbours.append(self.clist[row + 1][col])
        if row < (self.cell_height - 1) and col > 0:
            neighbours.append(self.clist[row + 1][col - 1])
        if row < (self.cell_height - 1) and col < (self.cell_width - 1):
            neighbours.append(self.clist[row + 1][col + 1])
        if col > 0:
            neighbours.append(self.clist[row][col - 1])
        if row > 0 and col > 0:
            neighbours.append(self.clist[row - 1][col - 1])
        if row > 0 and col < (self.cell_width - 1):
            neighbours.append(self.clist[row - 1][col + 1])

        return neighbours


    def update_cell_list(self, cell_list) -> object:
        """ Выполнить один шаг игры.

        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.

        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = deepcopy(cell_list)
        for row in range(self.cell_height):
        	for col in range(self.cell_width):
        		cell = (row, col)
        		lst_neigh = self.get_neighbours(cell)
        		if sum(lst_neigh) < 2 or (sum(lst_neigh) > 3):
        			new_clist[row][col] = 0
        		elif sum(lst_neigh) == 3:
        			new_clist[row][col] = 1
        self.clist = new_clist
        return self.clist

if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()