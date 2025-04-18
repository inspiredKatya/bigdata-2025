from operator import add

import os
import sys
from pyspark.sql import SparkSession
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder\
        .master("local[*]")\
        .appName('PySpark_Example')\
        .getOrCreate()

lines = spark.read.text("data\input-words.txt").rdd.map(lambda r: r[0])
counts = lines.flatMap(lambda x: x.split(' ')) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(add)\
        .filter(lambda x: x[1]>1)

output = counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))

spark.stop()
