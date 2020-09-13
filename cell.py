COLORS = {
    "STANDARD":(255,200,255),
    "BARRIER":(0,0,0),
    "START":(204,102,0),
    "GOAL":(0,204,102),
    "OPEN":(51,153,255),
    "CLOSED":(153,255,51),
    "PATH":(122,153,51)
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
    def __init__(self, state, weight):
        self.state = state
        self.weight = weight
        self.color = set_color(self.state, self.weight)
        self.neighbors = []

    def set_state(self, state, weight):
        self.state = state
        self.weight = weight
        self.color = set_color(self.state, self.weight)

if __name__ == "__main__":
    c = Cell(1,1,1,"STANDARD",2)
    print(c.color)