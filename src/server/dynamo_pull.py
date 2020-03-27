import boto3 
import json 
import decimal
# from boto3.dynamodb.conditions import Key,Attr
client = boto3.resource('dynamodb')
table = client.Table('FYP')


def dynamo_scan():
	response = table.scan()
		# FilterExpression = Attr('moisture_level'))
	listy = []

	for item in response['Items']: 
		# print(item)
		for x in item: 
			val = item[x]
			val = int(val)
			# print(type(val))
			listy.append(val)
	print(listy)


	return listy
