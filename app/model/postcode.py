from .. import db
from datetime import datetime 

class PostCode(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    code = db.Column(db.String(16), nullable=False)

    id_city = db.Column(db.Integer,db.ForeignKey('city.id'),nullable=False)