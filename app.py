from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps, loads
app = Flask(__name__)
api = Api(app)
seq = []
times = []
def sorter(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

class Logging(Resource):
    def get(self):
        js = request.json
        print(js)
        print(js["message"])
        if js["log"] == "sequence":
            seq.append(loads(request.json["message"]))
        return {'hello': 'world'}
    def post(self):
        js = request.json
        print(js)
        if js["log"] == "sequence":
            di = loads(request.json["message"])
            seq.append((di["seq"], di["time"]))
        print("\n###########\n")
	
        for item in sorter(seq):
            print(item[0])
        print("\n###########\n")
        return {"hello": "world"}


api.add_resource(Logging, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=9004)
