from ..model import Title, db 

class DaoTitle:

    @classmethod
    def add(cls,title):
        errors = []

        if Title.query.filter_by(title = title.title).first():
            errors.append("The Title already exists")

        if not title.title:
            errors.append("The Title name is required")

        if not errors:
            try:
                db.session.add(title)
                db.session.commit()
            except:
                db.session.rollback()
                errors.append("Failed to create the Title")

        return {"error": True if errors else False, "errors": errors}
    

    @classmethod
    def find(cls,id):
        errors = []
        title = None 

        try:
            title = Title.query.get(id)
        except:
            errors.append("Failed to find the Title")

        if not title:
            errors.append("The Title does not exist yet")

        return  {"error": True if errors else False, "errors": errors, "data": title}
    

    @classmethod
    def get(cls):
        errors = []
        titles = None 

        try: 
            titles = Title.query.all()
        except:
            errors.append("Failed to get titles")

        return  {"error": True if errors else False, "errors": errors, "data": titles}
    
    @classmethod
    def update(cls,id,update):
        errors = []

        try:
            Title.query.filter_by(id=id).update(update)
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to update the Title")

        return  {"error": True if errors else False, "errors": errors }

    
    @classmethod
    def delete(cls,id):
        errors = []

        try:
            Title.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to delete the Title")

        return  {"error": True if errors else False, "errors": errors }

        