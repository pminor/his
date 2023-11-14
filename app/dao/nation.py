from ..model import Nation, db 

class DaoNation:

    @classmethod
    def add(cls,nation):
        errors = []

        if Nation.query.filter_by(nation = nation.nation).first():
            errors.append("The Nation already exists")

        if not nation.nation:
            errors.append("The Nation name is required")

        if not errors:
            try:
                db.session.add(nation)
                db.session.commit()
            except:
                db.session.rollback()
                errors.append("Failed to create the Nation")

        return {"error": True if errors else False, "errors": errors}
    

    @classmethod
    def find(cls,id):
        errors = []
        nation = None 

        try:
            nation = Nation.query.get(id)
        except:
            errors.append("Failed to find the Nation")

        if not nation:
            errors.append("The Nation does not exist yet")

        return  {"error": True if errors else False, "errors": errors, "data": nation}
    

    @classmethod
    def get(cls):
        errors = []
        nations = None 

        try: 
            nations = Nation.query.all()
        except:
            errors.append("Failed to get Nations")

        return  {"error": True if errors else False, "errors": errors, "data": nations}
    
    @classmethod
    def update(cls,id,update):
        errors = []

        try:
            Nation.query.filter_by(id=id).update(update)
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to update the Nation")

        return  {"error": True if errors else False, "errors": errors }

    
    @classmethod
    def delete(cls,id):
        errors = []

        try:
            Nation.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to delete the Nation")

        return  {"error": True if errors else False, "errors": errors }

        