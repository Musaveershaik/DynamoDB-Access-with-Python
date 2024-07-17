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

1. Install the required Python libraries:
   ```bash
   pip install boto3
   
## Get Your Credentials 

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

## Code
```python
   import boto3
   
   # Initialize a session using Amazon DynamoDB with your credentials
   session = boto3.Session(
       aws_access_key_id='your_access_key',
       aws_secret_access_key='your_secret_key',
       region_name='your_region'
   )
   
   # Initialize DynamoDB resource
   dynamodb = session.resource('dynamodb')
   
   # Specify the table name
   table_name = 'FIRST-TABLE'
   table = dynamodb.Table(table_name)
   
   # Function to get an item from the table
   def get_item_from_table(table, key):
       try:
           response = table.get_item(Key=key)
           item = response.get('Item')
           if item:
               print(f"Item retrieved: {item}")
           else:
               print("Item not found")
       except Exception as e:
           print(f"Error getting item: {e}")
   
   # Example key to get item
   key = {
       'test-key': 'your_key'
   }
   
   # Call the function to get item
   get_item_from_table(table, key)
