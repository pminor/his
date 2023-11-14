from ..model import City, db 

class DaoCity:

    @classmethod
    def add(cls,city):
        errors = []

        if City.query.filter_by(city = city.city).first():
            errors.append("The city already exists")

        if not city.city:
            errors.append("The city name is required")

        if not errors:
            try:
                db.session.add(city)
                db.session.commit()
            except:
                db.session.rollback()
                errors.append("Failed to create the city")

        return {"error": True if errors else False, "errors": errors}
    

    @classmethod
    def find(cls,id):
        errors = []
        city = None 

        try:
            city = City.query.get(id)
        except:
            errors.append("Failed to find the city")

        if not city:
            errors.append("The city does not exist yet")

        return  {"error": True if errors else False, "errors": errors, "data": city}
    

    @classmethod
    def get(cls):
        errors = []
        cities = None 

        try: 
            cities = City.query.all()
        except:
            errors.append("Failed to get cities")

        return  {"error": True if errors else False, "errors": errors, "data": cities}
    
    @classmethod
    def update(cls,id,update):
        errors = []

        try:
            City.query.filter_by(id=id).update(update)
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to update the city")

        return  {"error": True if errors else False, "errors": errors }

    
    @classmethod
    def delete(cls,id):
        errors = []

        try:
            City.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to delete the city")

        return  {"error": True if errors else False, "errors": errors }

        