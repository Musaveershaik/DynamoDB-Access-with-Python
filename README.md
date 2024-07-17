# DynamoDB Access with Python

## Overview

This repository provides a Python script to access DynamoDB using AWS credentials. The script demonstrates how to retrieve an item from a DynamoDB table.

## Features

- Connect to DynamoDB using AWS credentials
- Retrieve items from a DynamoDB table
- Error handling for DynamoDB operations

## Requirements

- Python 3.x
- `boto3` library

## Installation

1. Clone the repository:
   ```bash
   https://github.com/Musaveershaik/DynamoDB-Access-with-Python.git
   cd dynamodb-access-python
2. Install the required Python libraries:
   ```bash
   pip install boto3

##Usage

1. Set your AWS credentials as environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID='your_access_key'
   export AWS_SECRET_ACCESS_KEY='your_secret_key'
   export AWS_REGION='your_region'
2. Update the dynamodb_access.py script with your table details:
   ```bash
   # Example key to get item
   key = {
    'test-key': 'your_key'
   }
3. Run the Script:
   ```bash
   python dynamodb_access.py
