import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table_name = 'Purchased-Shares'
table = dynamodb.Table(table_name)

import csv
file = 'c:/sharesInfo/PurchasedShares.csv'
with open(file, 'rt')as f:
  data = csv.reader(f)
  for row in data:
      table.put_item(Item={
          'partition_key': row[0],
          'Quantity': row[2],
          'Purchase Rate': row[1],
          'date': row[3]
      })
