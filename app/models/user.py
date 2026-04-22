from models.userRole import UserRole

class User:
    # ATRIBUTOS / CONSTANTES
    DEFAULT_ROLE = UserRole.USER

    # CONSTRUTORES

    def __init__(self, name: str, email: str):
        self.name = name   
        self.email = email
        self.id = -1
        self.role = self.DEFAULT_ROLE
