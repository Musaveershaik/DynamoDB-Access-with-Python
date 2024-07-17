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
