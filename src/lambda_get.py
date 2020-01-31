from botocore.vendored import requests

def lambda_handler(event, context):
   response = requests.get("https://example.com/")
   print response.json()