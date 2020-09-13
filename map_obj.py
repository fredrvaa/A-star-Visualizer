import csv
import copy

from cell import Cell

def get_state(weight, start = False, goal = False):
    if start:
        return "START"
    elif goal:
        return "GOAL"
    elif weight == -1:
        return "BARRIER"
    else:
        return "STANDARD"

class MapObj(object):
    def __init__(self, rows = 20, cols = 20, start_id = None, goal_id = None, path_to_map = None):
        self.rows = rows
        self.cols = cols
        self.base_cells = None
        self.cells = None

        # ids to start and goal cells
        self.start_id = start_id
        self.goal_id = goal_id

        if not path_to_map: 
            self._set_blank_map()
        else:
            self._load_map(path_to_map)

    def _set_blank_map(self):
        self.cells = []
        for row in range(self.rows):
            row_cells = []
            for col in range(self.cols):
                row_cells.append(Cell("STANDARD",1))
            self.cells.append(row_cells)

    def _load_map(self, path_to_map):
        with open(path_to_map, "r") as csv_file:
            self.cells = []
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row, line in enumerate(csv_reader):
                row_cells = []
                for col, num in enumerate(line):
                    weight = int(num)
                    state = get_state(weight, self.start_id == (row,col), self.goal_id == (row,col))
                    row_cells.append(Cell(state,weight))
                self.cells.append(row_cells)

            self.rows = len(self.cells)
            self.cols = len(self.cells[0])

            self.base_cells = copy.deepcopy(self.cells)

    def reset_map(self):
        self.cells = copy.deepcopy(self.base_cells)

    def get_cell(self, row, col):
        return self.cells[row][col]

    def set_cell_state(self, row, col, state, weight):
        cell = self.cells[row][col]
        print(cell.state)
        if cell.state == "START":
            self.start_id = None
        elif cell.state == "GOAL":
            self.goal_id = None

        cell.set_state(state, weight)

        if state == "START":
            self.start_id = (row,col)
        elif state == "GOAL":
            self.goal_id = (row,col)

    def remove_critical_states(self):
        self.start_id = None
        self.goal_id = None