from flask import Flask, request
from flask.json import jsonify
from flask_restful import Resource


class Version(Resource):
    def get(self):
        version_number = request.args.get("version_number")
        app_name = request.args.get("app_name")
        return jsonify({"version_number":version_number, "app_name":app_name})
        