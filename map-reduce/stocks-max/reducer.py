#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

sector2max = {}

for line in sys.stdin:
    line = line.strip()

    sector, max_price = line.split('\t', 1)
    try:
        sector2max[sector] = max(sector2max.get(sector, 0), float(max_price))
    except ValueError:
        pass

sorted_sector2max = sorted(sector2max.items(), key=itemgetter(1), reverse=True)

for sector, sector_max_price in sorted_sector2max:
    print(f'{sector}\t{sector_max_price}')
