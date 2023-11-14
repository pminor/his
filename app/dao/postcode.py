from ..model import PostCode, db 

class DaoPostCode:

    @classmethod
    def add(cls,postcode):
        errors = []

        if PostCode.query.filter_by(code = postcode.code, id_city=postcode.id_city ).first():
            errors.append("The PostCode already exists")

        if not postcode.code:
            errors.append("The PostCode code is required")

        if not postcode.id_city:
            errors.append("The PostCode city is required")

        if not errors:
            try:
                db.session.add(postcode)
                db.session.commit()
            except:
                db.session.rollback()
                errors.append("Failed to create the PostCode")

        return {"error": True if errors else False, "errors": errors}
    

    @classmethod
    def find(cls,id):
        errors = []
        postcode = None 

        try:
            postcode = PostCode.query.get(id)
        except:
            errors.append("Failed to find the PostCode")

        if not postcode:
            errors.append("The PostCode does not exist yet")

        return  {"error": True if errors else False, "errors": errors, "data": postcode}
    

    @classmethod
    def get(cls):
        errors = []
        postcodes = None 

        try: 
            postcodes = PostCode.query.all()
        except:
            errors.append("Failed to get postcodes")

        return  {"error": True if errors else False, "errors": errors, "data": postcodes}
    
    @classmethod
    def update(cls,id,update):
        errors = []

        try:
            PostCode.query.filter_by(id=id).update(update)
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to update the PostCode")

        return  {"error": True if errors else False, "errors": errors }

    
    @classmethod
    def delete(cls,id):
        errors = []

        try:
            PostCode.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to delete the PostCode")

        return  {"error": True if errors else False, "errors": errors }

        