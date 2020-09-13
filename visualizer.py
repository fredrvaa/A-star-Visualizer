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

        self.main()

    def main(self):
        #Put all variables up here
        stopped = False

        while not stopped:
             #Tuple for filling display... Current is white

            #Event Tasking
            #Add all your event tasking things here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    stopped = True

            #Add things like player updates here
            #Also things like score updates or drawing additional items
            # Remember things on top get done first so they will update in the order yours is set at
            self.draw()
            # Remember to update your clock and display at the end
            
            pygame.display.update()
            self.windowclock.tick(60)

    def draw(self):
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


    def get_clicked_pos(self, x, y):
        pass


if __name__ == "__main__":
    CELL_SIZE = 16
    m = MapObj(path_to_map = "csv_maps/Samfundet_map_Edgar_full.csv")
    #m = MapObj(10,10)
    v = Visualizer(m, CELL_SIZE)

    
    
    
