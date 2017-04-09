import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from flask import Flask, request, jsonify, redirect, url_for, send_from_directory
import flask.json


application = Flask(__name__)





dynamodb = boto3.resource(
	"dynamodb", 
	region_name="us-west-2", 
	endpoint_url="https://dynamodb.us-west-2.amazonaws.com"
	)

table = dynamodb.Table("Pixels")




class DecimalEncoder(flask.json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, decimal.Decimal):
			return str(obj)
		return super(DecimalEncoder, self).default(obj)


application.json_encoder = DecimalEncoder

@application.route('/')
def index():
	return "Welcome to the Geograffiti Flask API"

@application.route('/api/update_pixel', methods=['POST'])
def api_start_session():
	data = request.get_json()
	response = table.scan()['Items']
	print(response)
	for i in response:
		if i['x'] == data['x'] and i['y'] == data['y']:
			table.delete_item(Key={'ID':i['ID']})
	table.put_item(Item=data)
	return jsonify({'message':'success'})

@application.route('/api/get_pixels', methods=['GET'])
def api_get_questionnaire():
	try:
		response = table.scan()['Items']
		return jsonify(response)
	except: 
		return jsonify({"message":"errorrrrrrrrr"})

if __name__ == "__main__":
	application.run(debug=True)
