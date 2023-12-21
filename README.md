# ETF-with-Apache-Airflow

This code defines an Apache Airflow DAG (Directed Acyclic Graph) named "ETL_Server_Access_Log_Processing" with a series of tasks for downloading, extracting, transforming, and loading data. The DAG is scheduled to run daily. Here's a brief description:

1. **Importing Modules:**
   The code begins by importing necessary modules from the Apache Airflow library.

2. **DAG Arguments Block:**
   The `default_args` dictionary sets up default parameters for the DAG, including owner, start date, email settings, retries, and retry delay.

3. **DAG Definition Block:**
   The DAG itself is defined with the ID "ETL_Server_Access_Log_Processing." It has a description indicating that it's the author's first DAG and is scheduled to run daily.

4. **Download Task:**
   The `Download` task uses the `BashOperator` to execute a shell command that downloads a web server access log file from a specified URL.

5. **Extract Task:**
   The `Extract` task uses the `BashOperator` to execute a shell command (`cut`) that extracts specific fields (`timestamp` and `visitorid`) from the downloaded log file and saves the result in a new file named "extracted.txt."

6. **Transform Task:**
   The `Transform` task uses the `BashOperator` to execute a shell command (`tr`) that capitalizes all characters in the `visitorId` field in the "extracted.txt" file, producing a new file named "capitalized.txt."

7. **Load Task:**
   The `Load` task uses the `BashOperator` to execute a shell command (`zip`) that compresses the "capitalized.txt" file into a ZIP archive named "log.zip."

8. **Task Dependencies:**
   The `Download` task is set as a dependency for the `Extract` task, the `Extract` task is a dependency for the `Transform` task, and the `Transform` task is a dependency for the `Load` task. This creates a sequence of tasks where each task depends on the successful completion of the previous one.

The DAG is essentially an ETL (Extract, Transform, Load) workflow that processes a web server access log file on a daily basis.
