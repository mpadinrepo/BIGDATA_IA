#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def reducer():
    current_year = None
    max_rainfall = None

    for line in sys.stdin:
        year, rainfall = line.strip().split("\t")
        rainfall = float(rainfall)

        if current_year == year:
            max_rainfall = max(max_rainfall, rainfall)
        else:
            if current_year is not None:
                print(f"{current_year}\t{max_rainfall}")
            current_year = year
            max_rainfall = rainfall

    if current_year is not None:
        print(f"{current_year}\t{max_rainfall}")

if __name__ == "__main__":
    reducer()

