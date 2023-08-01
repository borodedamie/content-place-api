import requests
from flask import current_app, request
from flask_restful import Resource
from pyairtable import Table


class Articles(Resource):
    def get(self):
        base_id = current_app.config['AIRTABLE_BASE_ID']
        api_key = current_app.config['AIRTABLE_API_KEY']
        table_name = 'Articles'

        # Get the page size and offset from the request arguments
        page_size = request.args.get('page_size', 6)
        offset = request.args.get('offset')

        url = f'https://api.airtable.com/v0/{base_id}/{table_name}'
        headers = {'Authorization': f'Bearer {api_key}'}
        params = {'maxRecords': page_size, 'pageSize': page_size}

        if offset:
            params['offset'] = offset

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        records = data['records']
        next_offset = data.get('offset')

        result = {
            'records': records,
            'offset': next_offset
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
