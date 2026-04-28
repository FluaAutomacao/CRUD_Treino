from models.userRole import UserRole
from datetime import datetime, timezone

class User:
    # ATRIBUTOS / CONSTANTES
    default_role = UserRole.USER
    default_status = 1
    default_birth_date = None
    default_phone_number = None
    default_phone_address = None
    default_time = datetime.now(timezone.utc)

    # CONSTRUTORES

    def __init__(self, name: str, email: str, username: str):
        # Atributos obrigatórios do Usuário
        self.name = name
        self.email = email
        self.username = username
        self.id = -1
        self.role = self.default_role

        # Atributos opcionais  de cadastro do Usuário
        self.birth_date = self.default_birth_date
        self.phone_number = self.default_phone_number
        self.address = self.default_phone_address

        # Atributos de status do Usuário
        self.is_active = self.default_status
        self.created_at = self.default_time
        self.updated_at = self.default_time
        # self.last_login =
        # self.failed_attempts =
        # self.is_locked =

    
    def apply_update(self, userUpdate):
        for atribute, value in vars(userUpdate).items():
            if value is not None and value != self.atribute:
                setattr(self, atribute, value)
                updated = True
        
        if updated:
            self.updated_at = datetime.now(timezone.utc)

        
        
        
