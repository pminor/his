from .. import db
from datetime import datetime 

class City(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    city = db.Column(db.String(16), nullable=False)