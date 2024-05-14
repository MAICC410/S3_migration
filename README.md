# AWS Lambda S3 File Processor

This repository contains a Python AWS Lambda function that processes PDF and TIFF files stored in an Amazon S3 bucket. When files are uploaded to a specified source bucket, the Lambda function is triggered, processes the files by renaming them, and then moves them to a target bucket.

## Features

- **Automated File Processing**: Automatically process files as they are uploaded to the S3 bucket.
- **Support for PDF and TIFF Files**: Specifically handles PDF and TIFF files, ensuring they are processed correctly.
- **Environment Variable Configuration**: Uses environment variables to manage configuration settings, making the function flexible and easy to adapt to different environments.

## Prerequisites

To use this function, you will need:
- An AWS account.
- Two S3 buckets: one for the source and one for the destination of processed files.
- AWS CLI configured on your machine.

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/MAICC410/S3_migration.git
   cd s3_migration

2. Set up AWS Lambda
Navigate to AWS Lambda in the AWS Management Console.
Create a new Lambda function and upload the function code.
Set the runtime to Python.

3. Configure Environment Variables
SOURCE_BUCKET_NAME: The name of your source S3 bucket.
TARGET_BUCKET_NAME: The name of your destination S3 bucket.
These can be configured in the Lambda function's settings in the AWS Management Console.

4. Set up S3 Trigger
In the Lambda function configuration, add an S3 trigger.
Select the source bucket and the event type (e.g., PUT).
Configure the prefix or suffix if necessary to target specific file types or directories.

## Usage
Once the function is set up and the trigger is configured, any PDF or TIFF files uploaded to the source bucket will automatically be processed and moved to the destination bucket based on the configurations.

## Monitoring and Logs
You can monitor the function execution and view logs through AWS CloudWatch.
Logs will provide detailed information about the processing of each file and any errors that might occur.
