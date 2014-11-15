from flask import Flask
app = Flask(__name__)
version = "v1"
apiEndpoint = "/api/" + version + "/"

@app.route(apiEndpoint + "doors")
def getIds():
 	# TODO return json of id's
	return "I am doors. Here me roars."

@app.route(apiEndpoint + "doors/<int:door_id>/open")
def open(door_id):
	return "opening:  " + str(door_id)

@app.route(apiEndpoint + "doors/<int:door_id>/close")
def close(door_id):
	return "closing:  " + str(door_id)

@app.route("/")
def hello():
	return "Hai."


if __name__ == "__main__":
	app.run()