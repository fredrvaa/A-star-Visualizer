import argparse
import sys
sys.setrecursionlimit(100000)

from map_obj import MapObj
from visualizer import Visualizer

parser = argparse.ArgumentParser()
parser.add_argument("--task", type=int, default=1)
parser.add_argument("--cell_size", type=int, default=16)
args = parser.parse_args()

#map_obj = MapObj(10,10)
visualizer = Visualizer(cell_size = args.cell_size)
