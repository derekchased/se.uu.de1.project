# Imports
# from operator import add
# import re
# from collections import OrderedDict
# from operator import itemgetter 
# import itertools
# from operator import add
from pyspark.sql import SparkSession
from pyspark.sql.functions import count, desc, udf#,mean,col
from pyspark.sql.types import DoubleType, StringType

# New API Sesion
spark_session = SparkSession\
        .builder\
        .master("spark://1d5f9923626e:7077") \
        .appName("derek_a3_2e")\
        .config("spark.cores.max",8)\
        .config("spark.executor.cores",4)\
        .config("spark.dynamicAllocation.enabled", True)\
        .config("spark.dynamicAllocation.shuffleTracking.enabled", True)\
        .config("spark.shuffle.service.enabled", False)\
        .config("spark.dynamicAllocation.executorIdleTimeout","30s")\
        .getOrCreate()
        # .config("spark.driver.port",9998)\
        # .config("spark.blockManager.port",10005)\
        # .config('spark.ui.showConsoleProgress', False)\
        # .getOrCreate()


# Old API (RDD) - Get context from session
spark_context = spark_session.sparkContext

spark_context.setLogLevel("ERROR")

# Read CSV from HDFS
df = spark_session.read\
    .option("header", "true")\
    .csv("hdfs://192.168.2.119:9000/parking-citations.csv")\
    .cache()

# Preview data
print(df.show())

df.printSchema()

print(df.count())

print(df.rdd.getNumPartitions())

data = spark_session.read.csv(path="uk-macroeconomic-data.csv", sep=",", header=True)

print(data)