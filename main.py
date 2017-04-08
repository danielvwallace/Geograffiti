from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource("dynamodb", region_name="us-west-2", endpoint_url="https://dynamodb.us-west-2.amazonaws.com")
table = dynamodb.Table("Pixel")


#Adds entries from input file "testinput.json"

with open("testinput.json") as json_file:
    locations = json.load(json_file)
    for loc in locations:
        place = loc

        print("Adding location:", place["location"])

        table.put_item(
           Item=place
        )

# Scan through table for all items when scan() is empty

response = table.scan()

for i in response['Items']:
    print(json.dumps(i))

