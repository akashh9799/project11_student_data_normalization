 Introduction:
 
  This project details an ETL (Extract, Transform, Load) pipeline implemented on AWS for standardizing student exam data. The primary goal is to collect raw exam      data from various sources (e.g., CSVs, JSONs from different schools), normalize it to a consistent format (specifically, converting grades to a 0-100 scale), and    then store the processed, unified data for further analysis.
  

S3 Bucket Structure

  The S3 bucket student-exam-data-normalization is designed with the following structure to manage raw input and normalized output data:
     s3://student-exam-data-normalization/raw/: This prefix is used to store the original, unprocessed data files from different schools (e.g., school1.csv,               school2.json).
     s3://student-exam-data-normalization/output/standardized/: This prefix will house the normalized and merged data, saved in Parquet format.

     
Workflow Overview:

  The data normalization workflow involves the following key steps on AWS:

3.1. AWS Environment Preparation: An S3 bucket (student-exam-data-normalization) is created to hold raw and processed data. Raw data files (CSVs, JSONs) are uploaded to the raw/prefix within this bucket.

3.2. IAM Role Setup: An IAM role named AWSGlueServiceRoleForStudentProject is created with necessary permissions for S3 access, Glue service operations, and optional Redshift commands.

3.3. Glue Crawler Execution: An AWS Glue Crawler scans the raw/ S3 path to infer schemas of the input data and populate the AWS Glue Data Catalog with tables (e.g., in student_exam_db).

3.4. Glue Job Creation and Execution:

3.5. Optional Redshift Storage: The normalized data can optionally be loaded into an Amazon Redshift cluster for data warehousing and further analytical querying.

Technologies Used:

The core technologies leveraged in this project are:

AWS S3: Used for scalable and secure object storage of both raw and normalized data.

AWS Glue: A fully managed ETL service that includes capabilities for data cataloging (crawlers) and running Apache Spark jobs (Glue jobs).

PySpark: The Python API for Apache Spark, utilized within AWS Glue for data transformation and normalization logic.

AWS IAM: For managing access and permissions to AWS resources.


How to Use:
   
To set up and run this data normalization pipeline:

5.1. Prepare AWS Environment

5.2. Set Up IAM Role

5.3. Create and Run Glue Crawler

5.4. Create and Run Glue Job



Repository Structure
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

AKASH SURESH

Bachelor of Computer Applications (BCA), Sri Balaji University, Pune

Specialization: Cloud & Cybersecurity

GitHub: @akash9799

