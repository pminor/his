from .. import db
from datetime import datetime 

class Title(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(16), nullable=False)