#!/usr/bin/env python3

import sys

"""
data_schema = [
               StructField('_c0', IntegerType(), True),
               StructField('symbol', StringType(), True),
               StructField('data', DateType(), True),
               StructField('open', DoubleType(), True),
               StructField('high', DoubleType(), True),        #4 - max
               StructField('low', DoubleType(), True),
               StructField('close', DoubleType(), True),
               StructField('volume', IntegerType(), True),
               StructField('adjusted', DoubleType(), True),
               StructField('market.cap', StringType(), True),
               StructField('sector', StringType(), True),       #10 - sector
               StructField('industry', StringType(), True),
               StructField('exchange', StringType(), True),
            ]
"""

for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    print(f'{words[10]}\t{words[4]}')
