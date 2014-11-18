#!/usr/bin/python
import json
import settings
from hardware.hardware import PortalHW
from flask import Flask
from flask import jsonify
from flask import Response
app = Flask(__name__)

version = settings.constants['API_VERSION']
door_ids = settings.constants['DOOR_IDS']
api_endpoint = "/api/" + version + "/"

@app.route(api_endpoint + "doors", methods = ['GET'])
def getIds():
	return json.dumps(door_ids)

@app.route(api_endpoint + "doors/<door_id>/toggle", methods = ['POST'])
def toggle(door_id):
	if (door_id not in door_ids):
		return jsonify("invalid door id")
	print door_id
	portal = PortalHW()
	portal.toggle_door(door_id)
	return jsonify("toggling door state on:  " + str(door_id))

@app.route(api_endpoint + "doors/<door_id>/toggle", methods = ['GET'])
def getDoorState(door_id):
	return notYetImplemented()

@app.route(api_endpoint + "temperature", methods = ['GET'])
def getTemperature():
	return notYetImplemented()

@app.route(api_endpoint + "lights", methods = ['POST'])
def getLights():
	return notYetImplemented()

@app.route("/")
def hello():
	return "Hai."

def notYetImplemented():
	errorCode = 404
	message = {
		'status': errorCode,
		'message': 'Endpoint found but not yet implemented:  ' + request.url
	}
	response = jsonify(message)
	response.status_code = errorCode
	return response

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
