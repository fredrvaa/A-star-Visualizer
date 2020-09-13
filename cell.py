COLORS = {
    "STANDARD":(255,255,255),
    "BARRIER":(0,0,0),
    "START":(0,204,102),
    "GOAL":(102,204,0),
    "OPEN":(51,153,255),
    "CLOSED":(255,153,51),
    "PATH":(255,153,51)
}

def set_color(state, weight):
    # Darken color for higher weighted standard cells
    if weight > 1 and state == "STANDARD":
        color = tuple([c - 25*weight for c in COLORS[state]])
    else:
        color = COLORS[state]
    return color

class Cell(object):
    def __init__(self, state, weight):
        self.state = state
        self.weight = weight
        self.color = set_color(self.state, self.weight)
        self.neighbors = []
    
    def is_standard(self):
        return self.state == "STANDARD"

    def is_barrier(self):
        return self.state == "BARRIER"

    def is_start(self):
        return self.state == "START"

    def is_goal(self):
        return self.state == "GOAL"

    def is_open(self):
        return self.state == "OPEN"

    def is_closed(self):
        return self.state == "CLOSED"
    
    def is_path(self):
        return self.state == "PATH"

    def set_state(self, state, weight):
        self.state = state
        self.weight = weight
        self.color = set_color(self.state, self.weight)

if __name__ == "__main__":
    c = Cell(1,1,1,"STANDARD",2)
    print(c.color)