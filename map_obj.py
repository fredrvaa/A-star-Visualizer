import csv
import copy
import sys

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
    def __init__(self, task):
        self.rows = None
        self.cols = None
        self.cells = None

        self.task = task

        # Position of start and goal cells
        self.start_pos = task.start_pos
        self.goal_pos = task.goal_pos
        self.end_goal_pos = task.end_goal_pos

        self.reset()
        
    def _set_blank_map(self):
        self.rows = self.task.rows
        self.cols = self.task.cols
        self.start_pos = None
        self.goal_pos = None
        self.end_goal_pos = None
        self.cells = []
        for row in range(self.rows):
            row_cells = []
            for col in range(self.cols):
                cell = Cell(row, col, "STANDARD",1)
                row_cells.append(cell)
            self.cells.append(row_cells)

    def _load_map(self):
        with open(self.task.path_to_map, "r") as csv_file:
            self.cells = []
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row, line in enumerate(csv_reader):
                row_cells = []
                for col, num in enumerate(line):
                    weight = int(num)
                    state = get_state(weight, self.start_pos == (row,col), self.goal_pos == (row,col))
                    cell = Cell(row, col, state, weight)
                    row_cells.append(Cell(row, col, state, weight))
                self.cells.append(row_cells)

            self.rows = len(self.cells)
            self.cols = len(self.cells[0])

    def clean(self):
        for cell_row in self.cells:
            for cell in cell_row:
                if cell.state not in ["BARRIER","STANDARD","START","GOAL"]:
                    cell.set_state("STANDARD")
                cell.reset_scores()
        self._update_all_neighbours()

    def reset(self):
        if not self.task.path_to_map: 
            self._set_blank_map()
        else:
            self._load_map()
        self._update_all_neighbours()

    def get_start_cell(self):
        return self.cells[self.start_pos[0]][self.start_pos[1]]

    def get_goal_cell(self):
        return self.cells[self.goal_pos[0]][self.goal_pos[1]]

    def set_cell_state(self, cell, state, weight=None):
        if cell.state == "START":
            self.start_pos = None
        elif cell.state == "GOAL":
            self.goal_pos = None

        cell.set_state(state, weight)

        if state == "START":
            self.start_pos = (cell.row, cell.col)
        elif state == "GOAL":
            self.goal_pos = (cell.row ,cell.col)
        
        self._update_neighbours(cell)

    def move_goal(self):
        if self.end_goal_pos and not self.goal_pos == self.end_goal_pos:
            goal_cell = self.cells[self.goal_pos[0]][self.goal_pos[1]]
            if self.goal_pos[0] < self.end_goal_pos[0]:
                new_goal_cell = self.cells[self.goal_pos[0] + 1][self.goal_pos[1]]
            elif self.goal_pos[0] > self.end_goal_pos[0]:
                new_goal_cell = self.cells[self.goal_pos[0] - 1][self.goal_pos[1]]
            elif self.goal_pos[1] < self.end_goal_pos[1]:
                new_goal_cell = self.cells[self.goal_pos[0]][self.goal_pos[1] + 1]
            else:
                new_goal_cell = self.cells[self.goal_pos[0]][self.goal_pos[1] - 1]

            self.set_cell_state(goal_cell, "STANDARD")
            self.set_cell_state(new_goal_cell, "GOAL")

    def _get_neighbour_cells(self, cell, connectivity = "4N"):
        neighbour_cells = []
        if connectivity == "4N": # Could implement 8N connectivity in the future
            if cell.row > 0: neighbour_cells.append(self.cells[cell.row - 1][cell.col])             # Above
            if cell.row < self.rows - 1: neighbour_cells.append(self.cells[cell.row + 1][cell.col]) # Below
            if cell.col > 0: neighbour_cells.append(self.cells[cell.row][cell.col - 1])             # Left
            if cell.col < self.cols - 1: neighbour_cells.append(self.cells[cell.row][cell.col + 1]) # Right  
        return neighbour_cells


    def _update_neighbours(self, cell):
        for neighbour in cell.neighbours:
            for n in neighbour.neighbours:
                if n == cell:
                    n = cell

    def _update_all_neighbours(self):
        for cell_row in self.cells:
            for cell in cell_row:
                cell.neighbours = self._get_neighbour_cells(cell)

    
        
            
