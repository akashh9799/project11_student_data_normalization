import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define normalization function
def normalize_grade(grade):
    try:
        if grade == "A": return 90
        elif grade == "B": return 75
        elif grade == "C": return 60
        elif grade == "D": return 45
        elif grade == "F": return 30
        else: return int(grade)
    except:
        return None

normalize_udf = udf(normalize_grade, IntegerType())

# Read raw data
df1 = spark.read.csv("s3://student-exam-data-normalization/raw/school1.csv", header=True)
df2 = spark.read.json("s3://student-exam-data-normalization/raw/school2.json")

# Normalize grades
df1 = df1.withColumn("normalized_score", normalize_udf(df1["grade"]))
df2 = df2.withColumn("normalized_score", normalize_udf(df2["marks"]))

# Merge datasets
merged_df = df1.select("student_id", "normalized_score").unionByName(
            df2.select("student_id", "normalized_score"))

# Save to S3 as Parquet
merged_df.write.mode("overwrite").parquet("s3://student-exam-data-normalization/output/standardized/")

job.commit()