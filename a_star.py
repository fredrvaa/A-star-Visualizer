class AStar(object):
    def __init__(self, map_obj):
        self.map_obj = map_obj

        self.open = []
        self.closed = []
        self.path = []

        # Add start node into open list
        start_cell = self.map_obj.get_start_cell()
        start_cell.f = 0
        start_cell.g = 0
        start_cell.h = self._h(start_cell, self.map_obj.get_goal_cell())
        self.open.append(self.map_obj.get_start_cell())

    def update(self):
        if len(self.open):
            current_cell = self.open[0]
            current_index = 0
            for i, cell in enumerate(self.open):
                if cell.f < current_cell.f:
                    current_cell = cell
                    current_index = i

            self.open.pop(current_index)

            if current_cell.state not in ["START", "GOAL"]:
                self.map_obj.set_cell_state(current_cell, "CLOSED")  
            
            if current_cell == self.map_obj.get_goal_cell():
                c = current_cell
                while c is not None:
                    if c.state not in ["START", "GOAL"]:
                        self.map_obj.set_cell_state(c, "PATH")
                    self.path.append(c)
                    c = c.parent
                return False

            for neighbour in current_cell.neighbours:
                if neighbour.state in ["CLOSED", "BARRIER", "START"]: continue

                g = current_cell.g + neighbour.weight
                if g < neighbour.g:
                    neighbour.parent = current_cell
                    neighbour.g = g
                    neighbour.h = self._h(neighbour, self.map_obj.get_goal_cell())
                    neighbour.f = neighbour.g + neighbour.h

                    in_open = False
                    for open_cell in self.open:
                        if neighbour == open_cell:
                            in_open = True
                            break

                    if not in_open:
                        self.open.append(neighbour)
                        if neighbour.state not in ["START", "GOAL"]:
                            self.map_obj.set_cell_state(neighbour, "OPEN")  
        
            return True
        else:
            return False
            

    def _h(self, cell1, cell2):
        # Heuristic returning manhatten distance
        return abs(cell1.row - cell2.row) + abs(cell1.col - cell2.col)
