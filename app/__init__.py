from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = app.config.get('CONFIG_KEY')
db = SQLAlchemy(app)
migrate = Migrate(app, db)



from app import routes, models

