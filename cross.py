from random import randint
from math import sqrt
import numpy as np
import svgwrite

CROSSBAR_POSITION_RATIO = 1 / 3
CROSSBAR_RADIUS_RATIO = 1 / 3

def make_tuple(arr):
    return (float(arr[0]), float(arr[1]))

def do_cross(dwg, start_point: np.ndarray, end_point: np.ndarray, iteration):
    delta = end_point - start_point

    middle_point = start_point + delta * CROSSBAR_POSITION_RATIO

    middle_left_point = middle_point + np.array([-delta[1], delta[0]]) * CROSSBAR_RADIUS_RATIO
    middle_right_point = middle_point + np.array([delta[1], -delta[0]]) * CROSSBAR_RADIUS_RATIO

    if iteration > 1:
        do_cross(dwg, start_point, middle_point, iteration - 1)
        do_cross(dwg, middle_left_point, middle_point, iteration - 1)
        do_cross(dwg, middle_right_point, middle_point, iteration - 1)
        do_cross(dwg, end_point, middle_point, iteration - 1)
    else:
        dwg.add(dwg.line(make_tuple(start_point), make_tuple(end_point), stroke=svgwrite.rgb(0,0,0,'%'), stroke_width=1))
        dwg.add(dwg.line(make_tuple(middle_left_point), make_tuple(middle_right_point), stroke=svgwrite.rgb(0,0,0,'%'), stroke_width=1))

iteration = 8

dwg = svgwrite.Drawing('cross_{}.svg'.format(iteration), profile='tiny')
# dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
# dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
do_cross(dwg, np.array([2500,5000]), np.array([2500,0]), iteration)
dwg.save()








