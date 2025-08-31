import unittest
from funcs.maze import Maze
from funcs.cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1.cells), num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)

    def test_maze_cell_type(self):
        m = Maze(0, 0, 5, 5, 10, 10)
        for col in m.cells:
            for cell in col:
                self.assertIsInstance(cell, Cell)

    def test_maze_cell_draw_coordinates(self):
        m = Maze(5, 10, 2, 2, 20, 30)
        # Check coordinates of top-left cell after draw
        cell = m.cells[0][0]
        self.assertEqual(cell.x1, 5)
        self.assertEqual(cell.y1, 10)
        self.assertEqual(cell.x2, 25)
        self.assertEqual(cell.y2, 40)

    def test_maze_no_window(self):
        m = Maze(0, 0, 2, 2, 10, 10, win=None)
        # Should not raise any exceptions and cells should be created
        self.assertEqual(len(m.cells), 2)
        self.assertEqual(len(m.cells[0]), 2)

    def test_maze_cell_size(self):
        m = Maze(0, 0, 3, 4, 15, 25)
        self.assertEqual(m.cell_size_x, 15)
        self.assertEqual(m.cell_size_y, 25)

    def test_maze_cell_positions(self):
        m = Maze(2, 3, 2, 2, 5, 7)
        cell = m.cells[1][1]
        self.assertEqual(cell.x1, 2 + 5 * 1)
        self.assertEqual(cell.y1, 3 + 7 * 1)
        self.assertEqual(cell.x2, 2 + 5 * 1 + 5)
        self.assertEqual(cell.y2, 3 + 7 * 1 + 7)

    def test_maze_cells_are_unique(self):
        m = Maze(0, 0, 2, 2, 10, 10)
        self.assertIsNot(m.cells[0][0], m.cells[1][1])
        self.assertIsNot(m.cells[0][1], m.cells[1][0])

    def test_maze_animate_no_window(self):
        m = Maze(0, 0, 1, 1, 10, 10, win=None)
        try:
            m.animate()  # Should not raise
        except Exception as e:
            self.fail(f"animate() raised an exception with win=None: {e}")

    def test_maze_single_row(self):
        m = Maze(0, 0, 1, 10, 5, 5)
        self.assertEqual(len(m.cells), 10)
        self.assertEqual(len(m.cells[0]), 1)

    def test_maze_single_column(self):
        m = Maze(0, 0, 10, 1, 5, 5)
        self.assertEqual(len(m.cells), 1)
        self.assertEqual(len(m.cells[0]), 10)

    def test_maze_zero_offset(self):
        m = Maze(0, 0, 3, 3, 10, 10)
        cell = m.cells[2][2]
        self.assertEqual(cell.x1, 20)
        self.assertEqual(cell.y1, 20)
        self.assertEqual(cell.x2, 30)
        self.assertEqual(cell.y2, 30)

    def test_maze_nonzero_offset(self):
        m = Maze(7, 13, 2, 2, 8, 9)
        cell = m.cells[1][1]
        self.assertEqual(cell.x1, 7 + 8 * 1)
        self.assertEqual(cell.y1, 13 + 9 * 1)
        self.assertEqual(cell.x2, 7 + 8 * 1 + 8)
        self.assertEqual(cell.y2, 13 + 9 * 1 + 9)
        
    def test_maze_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Check the directions dictionary for entrance and exit
        self.assertFalse(m1.cells[0][0].directions["top"])
        self.assertFalse(m1.cells[num_cols-1][num_rows-1].directions["bottom"])
        
    def test_maze_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0,0,num_rows,num_cols,1,1)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(m1.cells[i][j].visited)

if __name__ == "__main__":
    unittest.main()