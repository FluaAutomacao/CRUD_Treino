from schemas.userValidate import UserValidate
from services.userService import UserServices

class UserCreate():

    def __init__(self, name: str, email: str, username: str):       
        # Executa validações
        self.name = UserValidate.validate_name(name)
        self.email = UserValidate.validate_email(email)
        self.username = username


        