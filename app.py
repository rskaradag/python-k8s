from flask import Flask, jsonify, request
from kubernetes import client, config
import json
from connector import node

app = Flask(__name__)

@app.route("/test")
def hello():

	body = {
        "metadata": {
            "labels": {
                "foo": "bar",
                "baz": None}
        }
    }

	v1 = client.CoreV1Api()
	node_list = v1.list_node()
	print("%s\t\t%s" % ("NAME", "LABELS"))
	for node in node_list.items:
		api_response = v1.patch_node(node.metadata.name, body)
		print("%s\t%s" % (node.metadata.name, node.metadata.labels))

	return "test"

@app.route("/v1/group/",methods=['POST'])
def add_group():
	try:
		jsonData=json.loads(request.data)
		groupId = jsonData["groupId"]
		try:

		except:
		for n in HOSTS:
			if n.record_group:
				return jsonify(message= "Success",
                    statusCode= 201,
                    data= GROUPS), 201
			else:
				return jsonify("400 - an error. Perhaps the object exists"), 400

	except Exception as e:
		return jsonify(isError= True,
                    message= str(e),
                    statusCode= 400), 400

@app.route("/v1/group/",methods=['DELETE'])
def delete_group():
	try:
		jsonData=json.loads(request.data)
		groupId = jsonData["groupId"]

		GROUPS.remove(groupId)

		return jsonify(groupId=groupId), 200
	except:
		return jsonify(isError= True,
                    message= str(e),
                    statusCode= 400), 400

@app.route("/v1/group/<string:groupId>",methods=['GET'])
def get_group(groupId):

	return jsonify(groupId=groupId), 200

if __name__ == "__main__":
	config.load_kube_config()  # for local environment

	v1 = client.CoreV1Api()
	v1_coordination=client.CoordinationApi()

	HOSTS = [
	 node('node01.app.internal.com'),
	 node('node02.app.internal.com'),
	 node('node03.app.internal.com')
	]

	GROUPS =[]

	app.run(host='0.0.0.0')