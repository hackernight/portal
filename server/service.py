from flask import Flask
import json
import settings
app = Flask(__name__)

version = settings.constants['API_VERSION']
door_ids = settings.constants['DOOR_IDS']
apiEndpoint = "/api/" + version + "/"

@app.route(apiEndpoint + "doors")
def getIds():
	return json.dumps(door_ids)

@app.route(apiEndpoint + "doors/<int:door_id>/toggle")
def open(door_id):
	if (door_id not in door_ids):
		return json.dumps("invalid door id")

	# TODO actually toggle the door w/ sam's thing
	return "toggling door state on:  " + str(door_id)

@app.route("/")
def hello():
	return "Hai."

if __name__ == "__main__":
	app.run()
