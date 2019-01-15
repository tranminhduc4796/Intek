#!/usr/bin/env python3
import sys
from station import Station
from route import Route
from graph import RGraph
from algo import BruteForce

if __name__ == '__main__':
    algo = BruteForce()
    try:
        algo.build(sys.argv[-1])
    except Exception:
        print('Invalid File', file=sys.stderr)
    algo.run_algo()
