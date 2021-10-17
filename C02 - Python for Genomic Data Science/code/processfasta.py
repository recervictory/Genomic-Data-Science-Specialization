#! /usr/bin/python
"""
processfasta.py builds a dictionary with all sequences from a FASTA file.
"""

import sys
filename=sys.argv[1]

try:
    f = open("data\myfile.fasta")
except IOError:
    print("File  %s does not exist!!" % filename)
