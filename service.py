#!/usr/bin/python
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
	return jsonify(door_ids)

@app.route(api_endpoint + "doors/<door_id>/toggle", methods = ['POST'])
def toggle(door_id):
	if (door_id not in door_ids):
		return jsonify("invalid door id")
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


@app.route(api_endpoint + "brewer", methods = ['POST'])
def startBrewingCoffee():
	return buildErrorFeedback(418, "Error code 418. For help, visit:  http://tools.ietf.org/html/rfc2324")

@app.route("/")
def hello():
	return "Hai."

@app.errorhandler(404)
def pageNotFound(error=None):
	return buildErrorFeedback(404, "Page not found:  " + request.url)

def notYetImplemented():
	errorCode = 404
	message = 'Endpoint has not yet been implemented:  ' + request.url
	return buildErrorFeedback(errorCode, message)

def buildErrorFeedback(errorCode, errorMessage):
	message = {
		'status': errorCode,
		'message': errorMessage
	}
	response = jsonify(message)
	response.status_code = errorCode
	return response


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
