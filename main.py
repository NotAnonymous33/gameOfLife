import pygame
from game import Game

game = Game()

length = 20 # pixels across of each cell
num_rows = 40
border = 2
grey = (30, 30, 30)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)


class Cell:
    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.on = False
        self.window = window
        self.xpos = 0
        self.ypos = 0
        # self.on = (x+y)%2==1

    def draw(self, mouse_position, x):
        self.xpos = (length + border) * self.x
        self.ypos = (length + border) * self.y
        color = ()
        # if mouse_position is not None:
        if self.hover(mouse_position) and x:
            color = green
        else:
            color = [black, white][self.on]
        pygame.draw.rect(self.window, color, [self.xpos, self.ypos, length, length])

    def hover(self, mouse_position):
        return self.xpos <= mouse_position[0] <= self.xpos + length and self.ypos <= mouse_position[1] <= self.ypos + length

    def change(self):
        self.on = ~self.on

    def __repr__(self):
        return f"{self.x=} {self.y=} {self.on=}"


pygame.init()

fps = 60
gameDisplay = pygame.display.set_mode((895, 895))
clock = pygame.time.Clock()

gameOn = True
gameDisplay.fill(grey)

# starting loop
# game loop

cells = [[Cell(i, j, gameDisplay) for i in range(num_rows)] for j in range(num_rows)]

start = False

while gameOn:
    if not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for row in cells:
                    for cell in row:
                        if cell.hover(pygame.mouse.get_pos()):
                            cell.change()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fps = 10
                    start = True
                if event.key == pygame.K_c:
                    for row in cells:
                        for cell in row:
                            cell.on = False
        pos = pygame.mouse.get_pos()

        for row in cells:
            for cell in row:
                cell.draw(pos, True)

    else:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = False
                    fps = 60
            if event.type == pygame.QUIT:
                gameOn = False
        cells = game.next_cells(cells)
        for row in cells:
            for cell in row:
                cell.draw((0, 0), False)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
