from flask import Flask
from flask_restful import Api
import os
from flask_cors import CORS
from resources.article import Articles, Article
from resources.comment import Comments

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

app.config['AIRTABLE_BASE_ID'] = os.environ.get('AIRTABLE_BASE_ID')
app.config['AIRTABLE_API_KEY'] = os.environ.get('AIRTABLE_API_KEY')

api.add_resource(Articles, '/articles')
api.add_resource(Comments, '/comments/<string:article_id>')
api.add_resource(Article, '/articles/<string:article_id>')

if __name__ == '__main__':
    app.run(debug=True)