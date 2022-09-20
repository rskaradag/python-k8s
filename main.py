from flask import Flask, jsonify, request
from kubernetes import client, config
import json, copy
from node import node
from connector import connector

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

		#_temp2=copy.deepcopy(HOSTS)

		jsonData=json.loads(request.data)
		groupId = jsonData["groupId"]

		for i in HOSTS:
			i.record_group(groupId)
		
		return jsonify(groupId= groupId), 201

	except Exception as e:
		return jsonify("400 - an error. Perhaps the object exists"), 400
	#finally:
		#HOSTS=copy.deepcopy(_temp2)

@app.route("/v1/group/",methods=['DELETE'])
def delete_group():
	try:
		jsonData=json.loads(request.data)
		groupId = jsonData["groupId"]

		for i in HOSTS:
			i.delete_group(groupId)

		return jsonify(groupId=groupId), 200
	except:
		return jsonify(isError= True,
                    message= str(e),
                    statusCode= 400), 400

@app.route("/v1/group/<string:groupId>",methods=['GET'])
def get_group(groupId):
	return jsonify(groupId=groupId), 200

@app.route("/v1/group/",methods=['GET'])
def get_group_all():
	return jsonify(groupId=HOSTS[0].get_all_groups()), 200

if __name__ == "__main__":
	config.load_kube_config()  # for local environment

	v1 = client.CoreV1Api()
	v1_coordination=client.CoordinationApi()

	HOSTS = [
	 node('node01.app.internal.com'),
	 node('node02.app.internal.com'),
	 node('node03.app.internal.com')
	]

	app.run(host='0.0.0.0',debug=True)