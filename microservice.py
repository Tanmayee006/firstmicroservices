# from flask import Flask, jsonify
from flask import Flask, jsonify, abort, make_response, request, url_for
import random
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_microservice():
	message = {"message": "Hello from the microservice! This is Tanmayee"}
	return jsonify(message)

if __name__ == "__main__":
	app.run(port=8000)
