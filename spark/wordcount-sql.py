
from pyspark.sql import SparkSession

#local[*] - испольуется локальный мастер(в памяти приложения) с максимально возможным количеством потоков

spark = SparkSession.builder\
        .master("local[*]")\
        .appName('PySpark_Example')\
        .getOrCreate()

from pyspark.sql import functions as f

data = spark.read.text("data\input-words.txt")

df = data.withColumn('word', f.explode(f.split(f.col('value'), ' ')))
df.createOrReplaceTempView("words")

spark.sql("select word, count(word) as count from words group by word order by count(word) desc") \
     .show()

data.withColumn('word', f.explode(f.split(f.col('value'), ' ')))\
    .groupBy('word')\
    .count()\
    .sort('count', ascending=False)\
    .show()