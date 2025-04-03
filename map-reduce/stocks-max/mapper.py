#!/usr/bin/env python3
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    print(f'{words[10]}\t{words[4]}')
