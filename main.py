import argparse
import sys
sys.setrecursionlimit(100000)

from map_obj import MapObj
from visualizer import Visualizer

parser = argparse.ArgumentParser()
parser.add_argument("--task", type=int, default=1)
parser.add_argument("--cell_size", type=int, default=16)
args = parser.parse_args()

if args.task == 1:
    start_pos = (27, 18)
    goal_pos = (40, 32)
    end_goal_pos = goal_pos
    path_to_map = 'csv_maps/Samfundet_map_1.csv'
elif args.task == 2:
    start_pos = (40, 32)
    goal_pos = (8, 5)
    end_goal_pos = goal_pos
    path_to_map = 'csv_maps/Samfundet_map_1.csv'
elif args.task == 3:
    start_pos = (28, 32)
    goal_pos = (6, 32)
    end_goal_pos = goal_pos
    path_to_map = 'csv_maps/Samfundet_map_2.csv'
elif args.task == 4:
    start_pos = (28, 32)
    goal_pos = (6, 32)
    end_goal_pos = goal_pos
    path_to_map = 'csv_maps/Samfundet_map_Edgar_full.csv'
elif args.task == 5:
    start_pos = (14, 18)
    goal_pos = (6, 36)
    end_goal_pos = (6, 7)
    path_to_map = 'csv_maps/Samfundet_map_2.csv'

map_obj = MapObj(start_pos = start_pos, goal_pos = goal_pos, path_to_map = path_to_map)
#map_obj = MapObj(10,10)
visualizer = Visualizer(map_obj, args.cell_size)
