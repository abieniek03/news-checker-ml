from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import lit

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

true_df = glueContext.create_dynamic_frame.from_catalog(
    database="news-db",
    table_name="true"
).toDF()

fake_df = glueContext.create_dynamic_frame.from_catalog(
    database="news-db",
    table_name="fake"
).toDF()

true_df = true_df.withColumn("label", lit(1))
fake_df = fake_df.withColumn("label", lit(0))

combined_df = true_df.unionByName(fake_df)

combined_df = combined_df.select("title", "text", "label")

combined_df.write.mode("overwrite").parquet("s3://api-cdv-project/data/processed")