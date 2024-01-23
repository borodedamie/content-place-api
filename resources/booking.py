from pyairtable import Table
from flask import current_app, request, jsonify
from flask_restful import Resource


class Bookings(Resource):
    def __init__(self):
        self.base_id = current_app.config['BOOKING_AIRTABLE_BASE_ID']
        self.api_key = current_app.config['AIRTABLE_API_KEY']
        self.table_name = 'Bookings'
        self.table = Table(self.api_key, self.base_id, self.table_name)

    def post(self):
        data = request.get_json()
        record = {
            "First Name": data.get('first_name'),
            "Last Name": data.get('last_name'),
            "Email": data.get('email'),
            "Phone Number": data.get('phone_number'),
            "Session Time": data.get('session_time'),
            "How did you hear about us": data.get('how_did_you_hear_about_us'),
            "Services": data.get('services'),
            "Date": data.get('date')
        }

        response = self.table.create(record)

        if response:
            return {"message": "Booking created successfully!"}, 201
        else:
            return {"message": "Failed to create booking."}, 500
