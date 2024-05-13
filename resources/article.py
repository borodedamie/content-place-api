import requests
from flask import current_app, request
from flask_restful import Resource
from pyairtable import Table

class Articles(Resource):
    def get(self):
        base_id = current_app.config['AIRTABLE_BASE_ID']
        api_key = current_app.config['AIRTABLE_API_KEY']
        table_name = 'Articles'

        url = f'https://api.airtable.com/v0/{base_id}/{table_name}'
        headers = {'Authorization': f'Bearer {api_key}'}

        # Initialize an empty list to store all the records
        all_records = []
        # Initialize the offset variable
        offset = None

        # Keep fetching records until there are no more records
        while True:
            params = {}
            if offset:
                params['offset'] = offset

            response = requests.get(url, headers=headers, params=params)
            data = response.json()

            records = data['records']
            all_records.extend(records)

            # Check if there is an offset in the response
            if 'offset' in data:
                offset = data['offset']
            else:
                break

        result = {
            'records': all_records
        }

        return result


class Article(Resource):
    def __init__(self):
        self.base_id = current_app.config['AIRTABLE_BASE_ID']
        self.api_key = current_app.config['AIRTABLE_API_KEY']
        self.table_name = 'Articles'
        self.table = Table(self.api_key, self.base_id, self.table_name)

    def get(self, article_id):
        record = self.table.get(article_id)
        return record
