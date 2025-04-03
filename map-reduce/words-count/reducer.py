#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

word2count = {}

for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)
    try:
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count
    except ValueError:
        pass

sorted_word2count = sorted(word2count.items(), key=itemgetter(1), reverse=True)

for word, count in sorted_word2count:
    if count > 1:
        print(f'{word}\t{count}')