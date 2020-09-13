import csv

from cell import Cell

def get_state(x):
    if x == -1:
        return "BARRIER"
    else:
        return "STANDARD"

class MapObj(object):
    def __init__(self, rows = 20, cols = 20, path_to_map = None):
        self.rows = rows
        self.cols = cols
        self.cells = None

        if not path_to_map: 
            self.set_blank()
        else:
            self.load_map(path_to_map)


    def set_blank(self):
        self.cells = []
        for row in range(self.rows):
            row_cells = []
            for col in range(self.cols):
                row_cells.append(Cell("STANDARD",1))
            self.cells.append(row_cells)

    def load_map(self, path_to_map):
        with open(path_to_map, "r") as csv_file:
            self.cells = []
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row, line in enumerate(csv_reader):
                row_cells = []
                for col, num in enumerate(line):
                    row_cells.append(Cell(get_state(int(num)),int(num)))
                self.cells.append(row_cells)

            self.rows = len(self.cells)
            self.cols = len(self.cells[0])

    def set_cell_state(self, pos, state, weight):
        self.cells[pos[0]][pos[1]].set_state(state, weight)