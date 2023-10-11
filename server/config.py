# Standard library imports

# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData

# Local imports
from models import db, User

# Instantiate app, set attributes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False



migrate = Migrate(app, db)
db.init_app(app)

# Instantiate REST API
api = Api(app)

# Instantiate CORS
CORS(app)

# Set up:
    # cd into server and run the following in the Terminal:
        # flask db init
        # flask db revision --autogenerate -m 'Create tables' 
        # flask db upgrade 
        # python seed.py
        # cd into client and run `npm i`

# Status codes
    # Most common response codes
        # 200 = ok ( GET, PATCH )
        # 201 = created ( POST )
        # 204 = no content ( DELETE )
        # 404 = not found
        # 401 = unauthorized ( Login )
        # 422 = unprocessable entity ( Validation Errors )
        # 418 = I'm a teapot! 🫖