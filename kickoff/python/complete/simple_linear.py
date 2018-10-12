"""
simple_linear.py             2.0, 2018-10-09

Copyright (c) 2018, Nicholas Bennett (nick@nickbenn.com).
All rights reserved. Usage is subject to license terms as stated in license.txt.

Usage: from simple_linear import SimpleLinear
       model = SimpleLinear(data_file, delimiter, skip)
       model.regress()

When regress() is called, regression properties are assigned values from linear
least squares computations.

"""

__author__="Nicholas Bennett"
__date__ ="$Oct 9, 2018$"


class SimpleLinear(object):
    """The SimpleLinear class implements a simple linear regression model,
    including computation of slope, intercept, and coefficient of
    determination."""

    def __init__(self, x, y):
        """Creates a new SimpleLinear, taking data from observations."""
        self._n = len(x)
        self._x = tuple(x)
        self._y = tuple(y)
        self._intercept = 0
        self._slope = 0
        self._r2 = -1

    def regress(self):
        """Perform least squares regression on data."""
        self._compute_sums()
        self._estimate_parameters()
        self._measure_fit()

    @property
    def n(self):
        """Number of data points."""
        return self._n

    @property
    def x(self):
        """List of x values."""
        return self._x

    @property
    def y(self):
        """List of actual y values."""
        return self._y

    @property
    def intercept(self):
        """Intercept of regression equation."""
        return self._intercept

    @property
    def slope(self):
        """Slope of regression equation."""
        return self._slope

    @property
    def r2(self):
        """Coefficient of determination."""
        return self._r2

    def _compute_sums(self):
        """Computes intermediate sums for regression."""
        self._sum_x = sum(self._x)
        self._sum_y = sum(self._y)
        self._sum_xy = sum(map(lambda x, y: x * y, self._x, self._y))
        self._sum_x2 = sum(x * x for x in self._x)
        self._sum_y2 = sum(y * y for y in self._y)

    def _estimate_parameters(self):
        """Computes intercept and slope from sums."""
        self._intercept = (
                (self._sum_x2 * self._sum_y - self._sum_x * self._sum_xy)
                / (self._n * self._sum_x2 - self._sum_x * self._sum_x))
        self._slope = (
                (self._n * self._sum_xy - self._sum_x * self._sum_y)
                / (self._n * self._sum_x2 - self._sum_x * self._sum_x))

    def _measure_fit(self):
        """Computes fitted values and goodness-of-fit statistic(s)."""
        fitted = [self._intercept + self._slope * x for x in self._x]
        sst = self._sum_y2 - self._sum_y * self._sum_y / self._n;
        sse = sum(map(lambda y, y_hat: (y - y_hat) ** 2, self._y, fitted))
        self._r2 = 1 - sse / sst
