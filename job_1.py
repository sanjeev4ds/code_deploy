from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("app_1_deploy") \
                    .getOrCreate()
					
df = spark.read.format("csv") \
    .option("inferschema","true") \
    .option("header","true") \
    .load("gs://sanjeev-bucket-name-issue/input/1MB/customers.csv")
	
df_final = df.groupBy("state","city").agg(count_distinct("*").alias("total_customers"))

df_final.write \
.mode("overwrite") \
.option("header","true") \
.csv("gs://sanjeev-bucket-name-issue/output/1MB/customers_final_new.csv")
# avoid using exact names in personal account for public repositories
#adding comment to test workflow re-run
