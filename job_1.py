from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("app_1_deploy") \
                    .getOrCreate()
					
df = spark.read.format("csv") \
    .option("inferschema","true") \
    .option("header","true") \
    .load("gs://sapient-sanjeevsaini/input/1MB/customers.csv")
	
df_final = df.groupBy("state","city").agg(count_distinct("*").alias("total_customers"))

df_final.write\
.option("header","true")\
.option("mode","overwrite")\
.csv("gs://sapient-sanjeevsaini/output/1MB/customers_final_new.csv")
#adding comment to test workflow re-run
