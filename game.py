class Game:
    def next_cells(self, cells):
        new_cells = cells
        grid = [(len(cells) + 2) * [0]] + [[0] + [abs(int(cell.on)) for cell in row] + [0] for row in cells] + [
            (len(cells) + 2) * [0]]
        grid = self.next_grid(grid)
        for row_num in range(len(cells)):
            for col_num in range(len(cells[row_num])):
                new_cells[row_num][col_num].on = grid[row_num + 1][col_num + 1]
        return new_cells

    def next_grid(self, grid):
        new_grid = [list(map(abs,i[:])) for i in grid]
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[row]) - 1):
                new_grid[row][col] = int(self.alive(grid, row, col))
        return new_grid

    def alive(self, grid, row, col):
        count = 0
        # add from row before
        # add cell before and after
        # add from row after
        count += sum(grid[row - 1][col - 1:col + 2])
        count += grid[row][col - 1] + grid[row][col + 1]
        count += sum(grid[row + 1][col - 1:col + 2])

        if grid[row][col] == 1 and 2 <= count <= 3: return True
        if grid[row][col] == 0 and count == 3: return True
        return False