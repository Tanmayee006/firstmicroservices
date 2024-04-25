# from flask import Flask, jsonify
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_microservice():
	# message = {"message": "Hello from the microservice! This is Tanmayee"}
	return "<p>Hello World</p>"
