from flask import Flask
import json
app = Flask(__name__)

version = "v1"
apiEndpoint = "/api/" + version + "/"
door_ids = [1, 2]

@app.route(apiEndpoint + "doors")
def getIds():
	return json.dumps(door_ids)

@app.route(apiEndpoint + "doors/<int:door_id>/open")
def open(door_id):
	if (door_id not in door_ids):
		return json.dumps("invalid door id")

	return "opening:  " + str(door_id)

@app.route(apiEndpoint + "doors/<int:door_id>/close")
def close(door_id):
	if (door_id not in door_ids):
		return json.dumps("invalid door id")

	return "closing:  " + str(door_id)

@app.route("/")
def hello():
	return "Hai."

if __name__ == "__main__":
	app.run()
