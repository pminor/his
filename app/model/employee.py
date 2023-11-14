from .. import db 
from datetime import datetime

class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)

    firstname = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    othername = db.Column(db.String(64), nullable=False, default='Other')

    idnumber = db.Column(db.String(16), nullable=False)
    gender = db.Column(db.String(2), nullable=False)

    dob = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    contact_telephone = db.Column(db.String(16), nullable=False)
    contact_mobile = db.Column(db.String(16), nullable=False)
    contact_email = db.Column(db.String(32), nullable=False)
    contact_postal = db.Column(db.String(16), nullable=False)

    disability = db.Column(db.String(2), nullable=True)
    disability_detail = db.Column(db.String(128), nullable=True)
    disability_regnumber = db.Column(db.String(128), nullable=True)

    id_title = db.Column(db.Integer,db.ForeignKey('title.id'),nullable=False)
    id_nation = db.Column(db.Integer,db.ForeignKey('nation.id'),nullable=False)
    id_ethnic = db.Column(db.Integer,db.ForeignKey('ethnic.id'),nullable=False)
    id_county = db.Column(db.Integer,db.ForeignKey('county.id'),nullable=False)
    id_postcode = db.Column(db.Integer,db.ForeignKey('postcode.id'),nullable=False)