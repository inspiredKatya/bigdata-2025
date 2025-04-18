
from pyspark.sql import SparkSession

#local[*] - испольуется локальный мастер(в памяти приложения) с максимально возможным количеством потоков

spark = SparkSession.builder\
        .master("local[*]")\
        .appName('PySpark_Example')\
        .getOrCreate()

from pyspark.sql.functions import col

dataFrame = spark.read.json("people.json", multiLine=True)

# null are filtered out
dataFrame.filter(col('age')>30).show()
