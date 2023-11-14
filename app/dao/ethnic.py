from ..model import Ethnic, db 

class DaoEthnic:

    @classmethod
    def add(cls,ethnic):
        errors = []

        if Ethnic.query.filter_by(ethnic = ethnic.ethnic).first():
            errors.append("The Ethnic already exists")

        if not ethnic.ethnic:
            errors.append("The Ethnic name is required")

        if not errors:
            try:
                db.session.add(ethnic)
                db.session.commit()
            except:
                db.session.rollback()
                errors.append("Failed to create the Ethnic")

        return {"error": True if errors else False, "errors": errors}
    

    @classmethod
    def find(cls,id):
        errors = []
        ethnic = None 

        try:
            ethnic = Ethnic.query.get(id)
        except:
            errors.append("Failed to find the Ethnic")

        if not ethnic:
            errors.append("The Ethnic does not exist yet")

        return  {"error": True if errors else False, "errors": errors, "data": ethnic}
    

    @classmethod
    def get(cls):
        errors = []
        ethnics = None 

        try: 
            ethnics = Ethnic.query.all()
        except:
            errors.append("Failed to get ethnics")

        return  {"error": True if errors else False, "errors": errors, "data": ethnics}
    
    @classmethod
    def update(cls,id,update):
        errors = []

        try:
            Ethnic.query.filter_by(id=id).update(update)
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to update the Ethnic")

        return  {"error": True if errors else False, "errors": errors }

    
    @classmethod
    def delete(cls,id):
        errors = []

        try:
            Ethnic.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to delete the Ethnic")

        return  {"error": True if errors else False, "errors": errors }

        