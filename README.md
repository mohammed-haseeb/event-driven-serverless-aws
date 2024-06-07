# Event-Driven Serverless Processing with AWS

This project demonstrates an event-driven serverless architecture using AWS services. It automates the processing of files uploaded to an S3 bucket by triggering Lambda functions that perform specified tasks, such as making API calls and deleting the uploaded files.

## Project Overview

This project includes the following components:

- **AWS S3**: Stores the files and triggers events upon object creation.
- **AWS Lambda**: Processes the S3 events, calls external APIs, waits for a defined period, and deletes the processed files.
- **AWS CloudWatch**: Captures logs from the Lambda function for monitoring and debugging.
- **IAM Roles and Policies**: Securely manage access permissions for Lambda and S3.
- **Terraform**: Provisions and manages AWS resources as Infrastructure as Code (IaC).

## Architecture Diagram

![Architecture Diagram](diagrams/architecture.png)

## Features

- **Event-Driven Architecture**: Automatically triggers Lambda functions when files are uploaded to S3.
- **Serverless Processing**: Uses AWS Lambda for serverless function execution, ensuring scalability and cost-efficiency.
- **Automated Workflows**: Performs API calls and cleans up S3 objects after processing.
- **Secure IAM Policies**: Ensures secure access to AWS resources.
- **Infrastructure as Code**: Utilizes Terraform for consistent and repeatable infrastructure setup.

## Prerequisites

- AWS Account
- Terraform installed
- AWS CLI configured

## Pre-packaged Lambda Function

The `lambda_function.zip` file is included for convenience. You can use this pre-packaged Lambda function directly or install necessary libraries to create your own package.

## Suggestions and Feedback

Please feel free to give me suggestions as I am in my learning phase. Thank you.
