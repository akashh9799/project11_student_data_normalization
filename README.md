<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
      
</head>
<body>
    <header>
        <h1>Student Exam Data Normalization on AWS</h1>
    </header>
    <main>
        <h2>Introduction</h2>
        <p>This project details an ETL (Extract, Transform, Load) pipeline implemented on AWS for standardizing student exam data. The primary goal is to collect raw exam data from various sources (e.g., CSVs, JSONs from different schools), normalize it to a consistent format (specifically, converting grades to a 0-100 scale), and then store the processed, unified data for further analysis.</p>

  <h2>S3 Bucket Structure</h2>
        <p>The S3 bucket <code>student-exam-data-normalization</code> is designed with the following structure:</p>
        <ul>
            <li><code>s3://student-exam-data-normalization/raw/</code>: Original data</li>
            <li><code>s3://student-exam-data-normalization/output/standardized/</code>: Normalized data (Parquet format)</li>
        </ul>

   <h2>Workflow Overview</h2>
        <ol>
            <li>AWS Environment Preparation</li>
            <li>IAM Role Setup</li>
            <li>Glue Crawler Execution</li>
            <li>Glue Job Creation and Execution</li>
            <li>Optional Redshift Storage</li>
        </ol>

   <h2>Technologies Used</h2>
        <ul>
            <li>AWS S3</li>
            <li>AWS Glue (Crawlers, Jobs)</li>
            <li>PySpark</li>
            <li>AWS IAM</li>
        </ul>

   <h2>How to Use</h2>
        <ol>
            <li>Prepare AWS Environment</li>
            <li>Set Up IAM Role</li>
            <li>Create and Run Glue Crawler</li>
            <li>Create and Run Glue Job</li>
        </ol>

   <h2>Repository Structure</h2>
<pre><code>
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
</code></pre>


   <p><strong>AKASH SURESH</strong><br>
        Bachelor of Computer Applications (BCA), Sri Balaji University, Pune<br>
        Specialization: Cloud & Cybersecurity<br>
        GitHub: <a href="https://github.com/akash9799" target="_blank">@akash9799</a></p>
    </main>
</body>
</html>
