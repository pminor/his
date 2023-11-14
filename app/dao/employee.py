from ..model import Employee, db 

class DaoEmployee:

    @classmethod
    def add(cls,employee):
        errors = []

        if Employee.query.filter_by(code = employee.code, id_city=employee.id_city ).first():
            errors.append("The Employee already exists")

        if not employee.firstname:
            errors.append("The Employee firstname is required")
        if not employee.surname:
            errors.append("The Employee surname is required")
        if not employee.othername:
            errors.append("The Employee othername is required")

        if not employee.idnumber:
            errors.append("The Employee idnumber is required")
        if not employee.gender:
            errors.append("The Employee gender is required")
        if not employee.dob:
            errors.append("The Employee dob is required")

        if not employee.contact_telephone:
            errors.append("The Employee telephone contact is required")
        if not employee.contact_mobile:
            errors.append("The Employee mobile contact is required")
        if not employee.contact_email:
            errors.append("The Employee email contact is required")
        if not employee.contact_postal:
            errors.append("The Employee postal contact is required")

        if not employee.id_title:
            errors.append("The Employee title is required")
        if not employee.id_nation:
            errors.append("The Employee nation is required")
        if not employee.id_ethnic:
            errors.append("The Employee ethnicity is required")
        if not employee.id_county:
            errors.append("The Employee county is required")
        if not employee.id_postcode:
            errors.append("The Employee post code is required")

        if not errors:
            try:
                db.session.add(employee)
                db.session.commit()
            except:
                db.session.rollback()
                errors.append("Failed to create the Employee")

        return {"error": True if errors else False, "errors": errors}
    

    @classmethod
    def find(cls,id):
        errors = []
        employee = None 

        try:
            employee = Employee.query.get(id)
        except:
            errors.append("Failed to find the Employee")

        if not employee:
            errors.append("The Employee does not exist yet")

        return  {"error": True if errors else False, "errors": errors, "data": employee}
    

    @classmethod
    def get(cls):
        errors = []
        employees = None 

        try: 
            employees = Employee.query.all()
        except:
            errors.append("Failed to get employees")

        return  {"error": True if errors else False, "errors": errors, "data": employees}
    
    @classmethod
    def update(cls,id,update):
        errors = []

        try:
            Employee.query.filter_by(id=id).update(update)
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to update the Employee")

        return  {"error": True if errors else False, "errors": errors }

    
    @classmethod
    def delete(cls,id):
        errors = []

        try:
            Employee.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            db.session.rollback()
            errors.append("Failed to delete the Employee")

        return  {"error": True if errors else False, "errors": errors }

        