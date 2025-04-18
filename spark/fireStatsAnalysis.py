
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, IntegerType, DoubleType

#local[*] - испольуется локальный мастер(в памяти приложения) с максимально возможным количеством потоков

spark = SparkSession.builder\
        .master("local[*]")\
        .appName('PySpark_Example')\
        .getOrCreate()

from pyspark.sql import functions as f
from pyspark.sql.types import *

fireFileschema = StructType([
 StructField("dt", DateType(), False),
 StructField("type_name", StringType(), False),
 StructField("type_id", IntegerType(), False),
 StructField("lon", DoubleType(), False),
 StructField("lat", DoubleType(), False),
])

# data = spark.read.csv("data\csv\sample_202.csv",sep=";",header=True)

data = spark.read.format("csv") \
    .option("delimiter", ";")\
    .options(header="true", multiline="true")\
    .option("dateFormat", "yyyy-M-d")\
    .schema(fireFileschema)\
    .load("data\\csv\\sample_202.csv")
  #  .load("data\\csv\\thermopoints.csv")

from pyspark.sql.functions import col, lit, year

# сколько пожаров было в 2020 г
data.filter( (col('dt') >= lit('2020-01-01')) & (col('dt') <= lit('2020-12-31')) ).show()

# сколько пожаров было в 2020 г, по типам
types = data.select('type_name','type_id').distinct()
# data.filter( (col('dt') >= lit('2012-01-01')) & (col('dt') <= lit('2020-12-31')) )\
#    .groupby('type_id')\
#    .count()\
#    .show()

data.select(year('dt').alias('year'),'type_id')\
     .filter(col('year')==2020)\
     .groupby('type_id', 'year')\
     .count()\
     .join(types,on='type_id')\
     .select('count','type_name')\
     .show()

# количество неконтролируемого пала по годам
data.select(year('dt').alias('year'),'type_id').filter(data.type_id==1).groupby('year')\
    .count().orderBy('year').show()