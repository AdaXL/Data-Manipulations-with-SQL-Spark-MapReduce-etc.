#!/usr/bin/env python

"""
A filter that _________.
"""

import fileinput

def process(line):
    """For each line of input, _____."""
    line = line[:-1]
    
    # read the stop-word-list.txt file
    file = open("stop-word-list.txt", "r")
    stopwords = file.read()

    # replace each stop words with None
    stop_list = stopwords.split("\r\n")
    for word in stop_list:
        if word == line:
            line = None
            
    print(line)

for line in fileinput.input():
    process(line)
