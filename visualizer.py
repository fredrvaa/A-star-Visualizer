import pygame

from map_obj import MapObj

class Visualizer(object):
    def __init__(self, map_obj, cell_size = 16):
        self.map_obj = map_obj
        self.cell_size = cell_size
        self.win_width = self.cell_size * self.map_obj.cols
        self.win_height = self.cell_size * self.map_obj.rows

        self.window = pygame.display.set_mode((self.win_width,self.win_height))
        pygame.display.set_caption("A* Visualizer")
        self.windowclock = pygame.time.Clock()

        self._main()

    def _main(self):
        
        running = True
        drawing_weight = 1

        while running:
            #Event Tasking
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    # If 1,2,3,4 is pressed, the drawing weight is updated accordingly
                    if pygame.key.name(event.key) == "1":
                        drawing_weight = 1
                    elif pygame.key.name(event.key) == "2":
                        drawing_weight = 2
                    elif pygame.key.name(event.key) == "3":
                        drawing_weight = 3
                    elif pygame.key.name(event.key) == "4":
                        drawing_weight = 4
                
                # Draws weighted "STANDARD" cells
                if pygame.mouse.get_pressed()[0]: # Left mouse click
                    pos = pygame.mouse.get_pos()
                    row, col = self._get_grid_pos(pos)
                    self.map_obj.set_cell_state(row, col, "STANDARD", drawing_weight)
                
                # Draws "START" and "GOAL" cells
                elif pygame.mouse.get_pressed()[1]: # Middle mouse click
                    pos = pygame.mouse.get_pos()
                    row, col = self._get_grid_pos(pos)
                    cell = self.map_obj.get_cell(row, col)
                    if self.map_obj.start_id is None and cell.state not in ["START", "GOAL"]:
                        self.map_obj.set_cell_state(row, col, "START", cell.weight)
                    elif self.map_obj.goal_id is None and cell.state not in ["START", "GOAL"]:
                        self.map_obj.set_cell_state(row, col, "GOAL", cell.weight)

                # DRAWS "BARRIER" cells
                elif pygame.mouse.get_pressed()[2]: # Right mouse click
                    # Gets cell from mouseclick
                    pos = pygame.mouse.get_pos()
                    row, col = self._get_grid_pos(pos)

                    # Set cell state to barrier
                    self.map_obj.set_cell_state(row, col, "BARRIER", -1)
                
            # Draw window
            self._draw()
            
            # Update display and clock
            pygame.display.update()
            self.windowclock.tick(60)

    def _draw(self):
        self.window.fill((255,255,255))

        # Draws all cells
        for j, row_cells in enumerate(self.map_obj.cells):
            for i, cell in enumerate(row_cells):
                x = i * self.cell_size
                y = j * self.cell_size
                pygame.draw.rect(self.window, cell.color, (x, y, self.cell_size, self.cell_size))
                
        # Draws grid on top of cells
        for col in range(self.map_obj.cols):
            x1 = x2 = col * self.cell_size
            y1 = 0
            y2 = self.win_height
            pygame.draw.line(self.window, (100,100,100), (x1,y1), (x2,y2))
            
        for row in range(self.map_obj.rows):
            x1 = 0
            x2 = self.win_width
            y1 = y2 = row * self.cell_size
            pygame.draw.line(self.window, (100,100,100), (x1,y1), (x2,y2))

        # Draw legend


    def _get_grid_pos(self, pos):
        row = pos[1] // self.cell_size
        col = pos[0] // self.cell_size
        return row, col



if __name__ == "__main__":
    CELL_SIZE = 16
    m = MapObj(path_to_map = "csv_maps/Samfundet_map_Edgar_full.csv")
    #m = MapObj(10,10)
    v = Visualizer(m, CELL_SIZE)

    
    
    
