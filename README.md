1. Introduction
This project details an ETL (Extract, Transform, Load) pipeline implemented on AWS for standardizing student exam data. The primary goal is to collect raw exam data from various sources (e.g., CSVs, JSONs from different schools), normalize it to a consistent format (specifically, converting grades to a 0-100 scale), and then store the processed, unified data for further analysis.

2. S3 Bucket Structure
The S3 bucket student-exam-data-normalization is designed with the following structure to manage raw input and normalized output data:

s3://student-exam-data-normalization/raw/: This prefix is used to store the original, unprocessed data files from different schools (e.g., school1.csv, school2.json).
s3://student-exam-data-normalization/output/standardized/: This prefix will house the normalized and merged data, saved in Parquet format.
3. Workflow Overview
The data normalization workflow involves the following key steps on AWS:

3.1. AWS Environment Preparation: An S3 bucket (student-exam-data-normalization) is created to hold raw and processed data. Raw data files (CSVs, JSONs) are uploaded to the raw/prefix within this bucket.

3.2. IAM Role Setup: An IAM role named AWSGlueServiceRoleForStudentProject is created with necessary permissions for S3 access, Glue service operations, and optional Redshift commands.

3.3. Glue Crawler Execution: An AWS Glue Crawler scans the raw/ S3 path to infer schemas of the input data and populate the AWS Glue Data Catalog with tables (e.g., in student_exam_db).

3.4. Glue Job Creation and Execution:
* 3.4.1. An AWS Glue job named normalize_student_data is configured to use PySpark.
* 3.4.2. This job loads data from the tables created by the crawler.
* 3.4.3. A PySpark script within the job normalizes grades (e.g., converts letter grades to numerical scores on a 0-100 scale) and merges the disparate datasets into a unified DataFrame.
* 3.4.4. The processed data is then saved in Parquet format to the s3://student-exam-data-normalization/output/standardized/ path.

3.5. Optional Redshift Storage: The normalized data can optionally be loaded into an Amazon Redshift cluster for data warehousing and further analytical querying.

4. Technologies Used
The core technologies leveraged in this project are:

AWS S3: Used for scalable and secure object storage of both raw and normalized data.
AWS Glue: A fully managed ETL service that includes capabilities for data cataloging (crawlers) and running Apache Spark jobs (Glue jobs).
PySpark: The Python API for Apache Spark, utilized within AWS Glue for data transformation and normalization logic.
AWS IAM: For managing access and permissions to AWS resources.
Amazon Redshift (Optional): A data warehousing service for storing and querying large datasets.
5. How to Use
To set up and run this data normalization pipeline:

5.1. Prepare AWS Environment:
* 5.1.1. Log into an AWS account.
* 5.1.2. Create an S3 bucket named student-exam-data-normalization in your preferred region.
* 5.1.3. Upload your raw data files (e.g., school1.csv, school2.json) into the raw/ folder within this S3 bucket.

5.2. Set Up IAM Role:
* 5.2.1. Navigate to IAM and create a new role.
* 5.2.2. Select "Glue" as the service that will use this role.
* 5.2.3. Attach the AmazonS3FullAccess, AWSGlueServiceRole, and optionally AmazonRedshiftAllCommandsFullAccess policies.
* 5.2.4. Name the role AWSGlueServiceRoleForStudentProject.

5.3. Create and Run Glue Crawler:
* 5.3.1. Go to AWS Glue -> Crawlers.
* 5.3.2. Add a new crawler, pointing its data source to s3://student-exam-data-normalization/raw/.
* 5.3.3. Assign the AWSGlueServiceRoleForStudentProject IAM role.
* 5.3.4. Configure the output to create a new database, for instance, student_exam_db.
* 5.3.5. Run the crawler to populate the Glue Data Catalog.

5.4. Create and Run Glue Job:
* 5.4.1. Go to AWS Glue -> Jobs.
* 5.4.2. Add a new job with the name normalize_student_data.
* 5.4.3. Select Spark type and Python language.
* 5.4.4. Choose the AWSGlueServiceRoleForStudentProject IAM role.
* 5.4.5. Upload the normalize_student_data.py script (found in glue_script/) as the job's script. Ensure the S3 output path in the script matches your bucket s3://student-exam-data-normalization/output/standardized/.
* 5.4.6. Run the Glue job to execute the data normalization process.

5.5. Optional: Load to Redshift:
* 5.5.1. If Redshift integration is desired, set up a Redshift cluster and create a target table with the appropriate schema.
* 5.5.2. Use a Glue job or Redshift's COPY command to load the Parquet data from s3://student-exam-data-normalization/output/standardized/ into your Redshift table.

6. Repository Structure
The project repository (project11/) is organized as follows:

project11/
├── README.md
├── glue_script/
│   └── normalize_student_data.py
├── data_sample/
│   ├── school1.csv
│   └── school2.json
├── screenshots/
│   ├── crawler_setup.png
│   └── s3_bucket.png
└── architecture_diagram.png
