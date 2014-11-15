#!/usr/bin/python
import json
import settings
from hardware.hardware import PortalHW
from flask import Flask
app = Flask(__name__)

version = settings.constants['API_VERSION']
door_ids = settings.constants['DOOR_IDS']
api_endpoint = "/api/" + version + "/"

@app.route(api_endpoint + "doors")
def getIds():
	return json.dumps(door_ids)

@app.route(api_endpoint + "doors/<door_id>/toggle")
def toggle(door_id):
	if (door_id not in door_ids):
		return json.dumps("invalid door id")
	print door_id
	portal = PortalHW()
	portal.toggle_door(door_id)
	return "toggling door state on:  " + str(door_id)

@app.route(api_endpoint + "temperature")
def getTemperature():
	return "Not Yet Implemented"

@app.route(api_endpoint + "lights")
def getLights():
	return "Not Yet Implemented"

@app.route("/")
def hello():
	return "Hai."

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)