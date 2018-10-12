"""
parser_util.py               2.0, 2018-09-22

Copyright (c) 2018, Nicholas Bennett (nickb@nickbenn.com).
All rights reserved. Usage is subject to license terms as stated in license.txt.

Usage: from parser_utility import TableFileParser
       str_data = TableFileParser(file_name, delimiter, skip_lines).strings()
       int_data = TableFileParser(file_name, delimiter, skip_lines).ints()
       float_data = TableFileParser(file_name, delimiter, skip_lines).floats()

"""

__author__="Nicholas Bennett"
__date__ ="$Sep 22, 2018$"

class TableFileParser(object):
    """The TableFileParser class implements a simple text file parser that can
    be used to read and parse a text data file, where each record is on its own
    line, and all values within records are delimited by a common delimiter."""

    def __init__(self, file_name, delimiter, skip=0):
        """Creates a new TableFileParser object by reading the contents of the
        specified file and parsing them into a list of string lists."""
        with open(file_name) as file:
            table = [line.strip().split(delimiter) for line in file
                if 0 != len(line.strip())]
            self._table = table[skip:]

    def strings(self):
        """Returns a copy of the table contents as a list of string lists."""
        return [row[:] for row in self._table]

    def ints(self):
        """Returns a copy of the table contents as a list of integer lists."""
        return [[int(col) for col in row] for row in self._table]

    def floats(self):
        """Returns a copy of the table contents as a list of float lists."""
        return [[float(col) for col in row] for row in self._table]
