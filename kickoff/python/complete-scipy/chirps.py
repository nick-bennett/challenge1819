"""
chirps.py                    2.0, 2018-10-09

Copyright (c) 2018, Nicholas Bennett (nickbenn@g-r-c.com).
All rights reserved. Usage is subject to license terms as stated in license.txt.

Loads cricket chirp and temperature data using TableFileParser. Then
instantiates SimpleLinear and uses it to perform a simple linear least squares
regression on crickets chirps vs. temperature. Finally, uses matplotlib to plot
observations and fitted line, and to display equation of fitted line and value
of R-squared.

"""

import sys

import matplotlib.pyplot as pyplot
from parser_util import TableFileParser
from simple_linear import SimpleLinear


__author__="Nicholas Bennett"
__date__ ="$Oct 9, 2018$"

DEFAULT_DATA_FILE = "chirps.csv"
DEFAULT_DELIMITER = ","
DEFAULT_SKIP_LINES = 1

CHART_TITLE = "Cricket Chirp Rate vs. Temperature"
X_AXIS_TITLE = "Temperature in $^{\circ}$F"
Y_AXIS_TITLE = "Cricket Chirps per 14sec"
MODEL_SPEC = "$\hat{Y} = %8.6f + %8.6fX, \; R^2 = %8.6f$"


def load(args):
    """Loads data from a CSV (default) file and transposes it."""
    default_params = [DEFAULT_DATA_FILE, DEFAULT_DELIMITER, DEFAULT_SKIP_LINES]
    data_file, delimiter, skip = list(map(lambda default, actual:
            actual if actual is not None else default,
            default_params, args))[:3]
    observations = TableFileParser(data_file, delimiter, skip).floats()
    x, y = zip(*observations)
    return (x, y)

    
def plot(model):
    """Uses Matplotlib to plot the input data and the fitted line from linear
    least-squares regression."""
    pyplot.title(CHART_TITLE)
    pyplot.xlabel(X_AXIS_TITLE)
    pyplot.ylabel(Y_AXIS_TITLE)
    pyplot.plot(model.x, model.y, marker='o', linestyle='None', color='red')
    if model.r2 >= 0:
        x_bounds = (min(model.x), max(model.x))
        y_fit = [model.intercept + model.slope * x for x in x_bounds]
        fit, = pyplot.plot(x_bounds, y_fit, marker='None', linestyle='-',
                color='blue')
        pyplot.legend([fit],
                [MODEL_SPEC % (model.intercept, model.slope, model.r2)],
                loc='upper left', frameon=False)
    pyplot.show()

    
if __name__ == "__main__":
    x, y = load((sys.argv + [None] * 3)[1:4])
    model = SimpleLinear(x, y)
    model.regress()
    plot(model)
