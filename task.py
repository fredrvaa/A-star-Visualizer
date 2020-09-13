class Task(object):
    def __init__(self, start_pos = None, goal_pos = None, end_goal_pos = None, path_to_map = None, rows = None, cols = None):
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.end_goal_pos = end_goal_pos if end_goal_pos is not None else self.goal_pos
        self.path_to_map = path_to_map
        self.rows = rows
        self.cols = cols