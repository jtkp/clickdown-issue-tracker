import json

from flask import Flask, request, jsonify, Blueprint
from flask_restx import Resource, Api, fields, inputs, reqparse, Namespace
import sqlite3

from db import *

bp = Blueprint('labels', __name__, url_prefix='/labels')
api = Namespace("labels", "Operations for labels")


# get labels for a user
@api.route('/<int:user>', methods=['GET'])
class Users(Resource):
    @api.response(200, 'Successfully retrieved label info')
    @api.response(404, 'Not Found')
    @api.doc(description="Gets all labels for a user given their id")
    def get(self, user):
        conn = sqlite3.connect('clickdown.db')
        c = conn.cursor()
        query = f"""
                SELECT  labels
                FROM    users
                WHERE   id = '{user}';
                """

        c.execute(query)

        data = []

        try:
            data = c.fetchone()[0]
        except:
            return []

        c.close()
        conn.close()

        return json.dumps(data)


# add new labels
label_payload = api.model('task', {
    "labels": fields.String
})
# post labels for a user
@api.route('/<int:user>', methods=['POST'])
class Users(Resource):
    @api.response(200, 'Successfully created label info')
    @api.response(404, 'Not Found')
    @api.doc(description="Stores label data")
    @api.expect(label_payload)
    def post(self, user):
        parser = reqparse.RequestParser()
        parser.add_argument('labels', required=True)
        args = parser.parse_args()
        conn = sqlite3.connect('clickdown.db')
        c = conn.cursor()
        query = f"""
                SELECT  labels
                FROM    users
                WHERE   id = '{user}';
                """
        existing = ''
        query = ''
        try:
            existing = c.fetchall()
            query = f"""
                    UPDATE  users
                    SET     labels = '{existing + ',' + args.labels}'
                    WHERE   id = '{user}';
                    """
            print('try')
        except:
            existing = ''
            query = f"""
                    UPDATE  users
                    SET     labels = '{existing + ', ' + args.labels}'
                    WHERE   id = '{user}';
                    """
            print('except')
        c.execute(query)

        conn.commit()
        c.close()
        conn.close()

        return {'value': True}

