from .. import db
from datetime import datetime 

class Nation(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nation = db.Column(db.String(16), nullable=False)