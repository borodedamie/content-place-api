from pyairtable import Table
from flask import current_app, request, jsonify
from flask_restful import Resource


class Contacts(Resource):
    def __init__(self):
        self.base_id = current_app.config['BOOKING_AIRTABLE_BASE_ID']
        self.api_key = current_app.config['AIRTABLE_API_KEY']
        self.table_name = 'Contacts'
        self.table = Table(self.api_key, self.base_id, self.table_name)

    def post(self):
        data = request.get_json()
        record = {
            "Name": data.get('name'),
            "Email": data.get('email'),
            "Phone": data.get('phone'),
            "For": data.get('service'),
            "Message": data.get('message'),
        }

        response = self.table.create(record)

        if response:
            return {"message": "Contact created successfully!"}, 201
        else:
            return {"message": "Failed to create booking."}, 500