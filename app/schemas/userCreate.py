from schemas.userValidate import UserValidate

class UserCreate():

    def __init__(self, name: str, email: str):       
        UserValidate.validate_name(name)
        UserValidate.validate_email(email)
        self.name = name
        self.email = email
        

    