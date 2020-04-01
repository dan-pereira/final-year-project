import boto3 
client = boto3.resource('dynamodb')
table = client.Table('FYP')
response = table.put_item(
	Item = { 
		'moisture_level': 20,
		}
	)