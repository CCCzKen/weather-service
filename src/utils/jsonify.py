from flask import jsonify


class JsonpResp(object):

    @staticmethod
    def success(data):
        return jsonify(dict(code=0, data=data))
