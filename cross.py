""" Recursive fractal 'cross' generation code """

import numpy as np
import svgwrite

CROSSBAR_POSITION_RATIO = 1 / 3
CROSSBAR_RADIUS_RATIO = 1 / 3
TOTAL_ITERATION = 10
STROKE = svgwrite.rgb(0, 0, 0, '%')


def make_tuple(arr):
    """ Convert the numpy array to a tuple (to be a dwg.line argument). """
    return (float(arr[0]), float(arr[1]))


def do_cross(svg, start_point: np.ndarray, end_point: np.ndarray, iteration):
    """ Draw the cross """
    delta = end_point - start_point

    middle_point = start_point + delta * CROSSBAR_POSITION_RATIO

    middle_left_point = middle_point + np.array([-delta[1], delta[0]]) * CROSSBAR_RADIUS_RATIO
    middle_right_point = middle_point + np.array([delta[1], -delta[0]]) * CROSSBAR_RADIUS_RATIO

    if iteration > 1:
        do_cross(svg, start_point, middle_point, iteration - 1)
        do_cross(svg, middle_left_point, middle_point, iteration - 1)
        do_cross(svg, middle_right_point, middle_point, iteration - 1)
        do_cross(svg, end_point, middle_point, iteration - 1)
    else:
        svg.add(svg.line(make_tuple(start_point), make_tuple(end_point), stroke=STROKE, stroke_width=1))
        svg.add(svg.line(make_tuple(middle_left_point), make_tuple(middle_right_point), stroke=STROKE, stroke_width=1))

drawing = svgwrite.Drawing('cross_{}.svg'.format(TOTAL_ITERATION), profile='tiny')
do_cross(drawing, np.array([2500, 5000]), np.array([2500, 0]), TOTAL_ITERATION)
drawing.save()








