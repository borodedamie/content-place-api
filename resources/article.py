import requests
from flask import current_app, request
from flask_restful import Resource

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
