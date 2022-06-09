import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table_name = 'Purchased-Shares'
params = {
    'TableName': table_name,
    'KeySchema': [
        {'AttributeName': 'partition_key', 'KeyType': 'HASH'}
    ],
    'AttributeDefinitions': [
        {'AttributeName': 'partition_key', 'AttributeType': 'S'}
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 2,
        'WriteCapacityUnits': 2
    }
}
table = dynamodb.create_table(**params)
print(f"Creating {table_name}...")
table.wait_until_exists()
