# AWS Lambda Functions

This repository contains two AWS Lambda function projects:
1. **Add Two Numbers**: A Lambda function that adds two numbers and returns the result.
2. **Store Document in S3**: A Lambda function that stores a document or PDF file in an S3 bucket.

---

## 1. Add Two Numbers Lambda Function

### Overview
This AWS Lambda function takes two numbers as input, adds them, and returns the result.

### Code Explanation
- It parses the input JSON containing two numbers (`num1` and `num2`).
- Performs addition and returns the result as JSON.

### Example Input
```json
{
  "num1": 5,
  "num2": 10
}

{
  "result": 15
}

Deployment Steps
Create the Lambda Function:

Go to the AWS Management Console.
Navigate to Lambda > Create Function > Author from Scratch.
Enter a function name (e.g., AddTwoNumbers), select Python 3.x runtime, and create the function.
Upload the Code:

Replace the default function code with the code from the file add_two_numbers.py in this repository.
Test the Function:

Create a test event in the Lambda console with the example input.
Run the test and check the result.
2. Store Document in S3 Lambda Function
Overview
This AWS Lambda function uploads a document or PDF file to a specified S3 bucket.

Code Explanation:

The Lambda function accepts a Base64-encoded file and its filename as input.
Decodes the file and uploads it to the specified S3 bucket using the AWS SDK (boto3).
Example Input
json
Copy code
{
  "file_name": "test_document.pdf",
  "file_content": "Base64-encoded-content-here"
}
Example Output
json
Copy code
{
  "message": "File uploaded successfully",
  "s3_key": "test_document.pdf"
}
Deployment Steps
Set Up an S3 Bucket:

Go to the AWS Management Console and create an S3 bucket (e.g., my-test-bucket).
Create the Lambda Function:

Navigate to Lambda > Create Function > Author from Scratch.
Enter a function name (e.g., StoreDocumentInS3), select Python 3.x runtime, and create the function.
Upload the Code:

Replace the default function code with the code from the file store_document_s3.py in this repository.
Add IAM Permissions:

Attach an IAM policy with S3 write permissions to the Lambda function's execution role. Example policy:
json
Copy code
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::my-test-bucket/*"
    }
  ]
}
Test the Function:

Create a test event with the example input.
Run the test and check the file in your S3 bucket.

Prerequisites
AWS Account with access to Lambda and S3.
Python 3.x environment for local testing (optional).
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Nagavinay Vasantham
GitHub
LinkedIn
