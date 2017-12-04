""" Generates a leaf-like fractal structure """

from math import sqrt, pi
import numpy as np
import svgwrite

LEFT_SIDE_SHIFT_RATIO = 1 / 9
SUBLEAF_LENGTH_RATIO = 3 / 9
SUBLEAF_ANGLE = pi / 6  # 30 degrees

STROKE = svgwrite.rgb(0, 0, 0, '%')
TOTAL_ITERATION = 7

THSQ = sqrt(3) / 2


def make_tuple(arr):
    """ Convert the numpy array to a tuple (to be a dwg.line argument). """
    return (float(arr[0]), float(arr[1]))


def do_leaf(svg, start_point: np.ndarray, end_point: np.ndarray, iteration, n_subleaves_one_side):
    """ Draw the leaf (recursive) """
    delta = end_point - start_point
    # draw a straight main line
    svg.add(svg.line(make_tuple(start_point), make_tuple(end_point), stroke=STROKE, stroke_width=1))

    if iteration > 1:
        # draw the subleaves
        vector = delta * SUBLEAF_LENGTH_RATIO
        leaf_left = np.array([THSQ * vector[0] + 0.5*vector[1], -0.5*vector[0] + THSQ * vector[1]])
        leaf_right = np.array([THSQ * vector[0] - 0.5*vector[1], 0.5*vector[0] + THSQ * vector[1]])

        for i in range(n_subleaves_one_side):
            shift = i * delta * (1 / n_subleaves_one_side) + (delta / (2 * n_subleaves_one_side))

            sub_start_point = start_point + shift
            sub_end_point = sub_start_point + leaf_left

            do_leaf(svg, sub_start_point, sub_end_point, iteration - 1, n_subleaves_one_side)

        for i in range(n_subleaves_one_side):
            shift = i * delta * (1 / n_subleaves_one_side)

            sub_start_point = start_point + shift
            sub_end_point = sub_start_point + leaf_right

            do_leaf(svg, sub_start_point, sub_end_point, iteration - 1, n_subleaves_one_side)

drawing = svgwrite.Drawing('svg_leaves/leaf-{}.svg'.format(TOTAL_ITERATION), profile='tiny')
do_leaf(drawing, np.array([500, 0]), np.array([500, 500]), TOTAL_ITERATION, 4)
drawing.save()
