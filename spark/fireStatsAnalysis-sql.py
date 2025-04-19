
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
#   .load("data\\csv\\thermopoints.csv")

data.createOrReplaceTempView("fires")

# сколько пожаров было в 2020 г, по типам
spark.sql("select type_name, count(*) from fires where dt between '2020-01-01' and '2020-12-31' group by type_name")\
    .show()

# количество неконтролируемого пала по годам
spark.sql("select year(dt) as year, count(*) from fires where type_id = 1  group by year")\
    .show()
