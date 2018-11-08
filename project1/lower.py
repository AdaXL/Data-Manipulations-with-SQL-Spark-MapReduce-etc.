#!/usr/bin/env python

"""
A filter that _________.
"""

import fileinput


def process(line):
    """For each line of input, _____."""
    line = line[:-1]
    # Do something more here!
    print(line.lower())


for line in fileinput.input():
    process(line)
