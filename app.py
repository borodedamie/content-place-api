from flask import Flask
from flask_restful import Api
import os
from resources.article import Articles
from resources.comment import Comments

app = Flask(__name__)
api = Api(app)

app.config['AIRTABLE_BASE_ID'] = os.environ.get('AIRTABLE_BASE_ID')
app.config['AIRTABLE_API_KEY'] = os.environ.get('AIRTABLE_API_KEY')

api.add_resource(Articles, '/articles')
api.add_resource(Comments, '/comments/<string:article_id>')

if __name__ == '__main__':
    app.run(debug=True)