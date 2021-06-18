from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask("website")
app.config.from_object("website.config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from .models import tables
from .controllers import routes
