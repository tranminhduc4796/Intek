#!/usr/bin/env python3
from sys import argv
from station import Station
from route import Route
from graph import RGraph
from algo import BruteForce

if __name__ == '__main__':
    algo = BruteForce()
    algo.build(argv[-1])
    algo.run_algo()
