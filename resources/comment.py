from pyairtable import Table
from flask import current_app, request
from flask_restful import Resource


class Comments(Resource):
    def __init__(self):
        self.base_id = current_app.config['AIRTABLE_BASE_ID']
        self.api_key = current_app.config['AIRTABLE_API_KEY']
        self.table_name = 'Comments'
        self.table = Table(self.api_key, self.base_id, self.table_name)

    def get(self, article_id):
        records = self.table.all()

        comments = [record for record in records if article_id in record['fields'].get('Articles', [])]

        return comments

    def post(self, article_id):
        data = request.get_json()
        name = data['name']
        notes = data['notes']

        record = {
            'Name': name,
            'Notes': notes,
            'Articles': [article_id]
        }
        self.table.create(record)

        return {'message': 'Comment created'}, 201
