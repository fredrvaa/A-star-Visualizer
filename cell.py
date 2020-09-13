import math

COLORS = {
    "STANDARD":(255, 255, 255),
    "BARRIER":(0, 0, 0),
    "START":(255, 102, 102),
    "GOAL":(102, 255, 153),
    "OPEN":(255, 153, 0),
    "CLOSED":(0, 153, 204),
    "PATH":(255, 204, 102)
}

# Darkens shade of cells with higher weight. Best results in range 0.2-0.5
DARKEN_FACTOR = 0.2

def set_color(state, weight):
    # Darken color for higher weighted standard cells
    if weight > 1 and state == "STANDARD":
        color = tuple([c * (1 - DARKEN_FACTOR)**weight for c in COLORS[state]])
    else:
        color = COLORS[state]
    return color

class Cell(object):
    def __init__(self, row, col, state, weight):
        self.row = row
        self.col = col
        self.state = state
        self.weight = weight
        self.color = set_color(self.state, self.weight)

        # A* dependent variables
        self.neighbours = []
        self.parent = None
        self.g = math.inf
        self.h = math.inf
        self.f = self.g + self.h

    def set_state(self, state, weight = None):
        self.state = state
        if weight is not None:
            self.weight = weight
        self.color = set_color(self.state, self.weight)

    def reset_scores(self):
        self.g = math.inf
        self.h = math.inf
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
