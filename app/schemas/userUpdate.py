from schemas.userValidate import UserValidate
from models.userRole import UserRole

class UserUpdate:
    def __init__(self, name: str = None, email: str = None, role: str = None):
        self.name = name
        self.email = email
        self.role = role

        #validação do nome a ser atualizado
        if self.name is not None:
            UserValidate.validate_name(name)
        
        #validação do e-mail a ser atualizado
        if self.email is not None:
            UserValidate.validate_email(email)
        
        #validação do role a ser atualizado
        if self.role is not None:
            UserRole(role)

