from .. import db
from datetime import datetime 

class Ethnic(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    ethnic = db.Column(db.String(16), nullable=False)