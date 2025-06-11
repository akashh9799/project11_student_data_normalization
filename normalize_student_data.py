import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

# Initialize context
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Step 1: Read data from AWS Glue Catalog tables
school1_df = spark.read.table("student_exam_db.school1_csv")
school2_df = spark.read.table("student_exam_db.school2_json")

# Step 2: Standardize grades
def grade_to_score(grade):
    mapping = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 50}
    return mapping.get(grade.upper(), None)

grade_udf = udf(grade_to_score, IntegerType())

school1_df = school1_df.withColumn("standard_score", grade_udf(school1_df["grade"]))
school2_df = school2_df.withColumn("standard_score", grade_udf(school2_df["grade"]))

# Step 3: Merge the data
merged_df = school1_df.unionByName(school2_df)

# Step 4: Write output to S3 in Parquet format
output_path = "s3://your-output-bucket/standardized_student_data/"
merged_df.write.mode("overwrite").format("parquet").save(output_path)

# Finish Job
job.commit()
