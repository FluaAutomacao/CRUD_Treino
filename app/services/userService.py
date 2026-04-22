from models.user import User
from schemas.userCreate import UserCreate
from schemas.userUpdate import UserUpdate
from repositories.userRepositorie import UserRepositorie
from models.userRole import UserRole

class UserServices():
    def __init__(self):
        self.repositorie = UserRepositorie()

    def create_user(self, name: str, email: str)-> User:
        #Válida nome e e-mail
        validatedData = UserCreate(name, email)

        #Verifica se já tem o e-mail no banco de dados
        if self.get_user_by_email(email) is not None:
            raise ValueError(f"E-mail {email} já cadastrado no banco de dados.")

        #Cria usuário
        userData = User(validatedData.name, validatedData.email)
        #Salva usuário no banco de dados
        self.repositorie.save_user(userData)
        return userData
       
    def get_users(self) -> dict:
        return self.repositorie.dataBase
    
    def get_user_by_id(self, id:int) -> User:
        return self.get_users().get(id)
    
    def get_user_by_name(self, name: str) -> list:
        usersList = []
        dataBase = self.get_users()
        for value in dataBase.values():
            if value.name == name:
                usersList.append(value)
        return usersList
            
    def get_user_by_email(self, email: str) -> User:
        dataBase = self.get_users()
        for value in dataBase.values():
            if value.email == email:
                return value
    
    def user_delete_by_id(self, id: int):
        if id in self.get_users():
            self.user_delete_service(self.get_user_by_id(id))

    def user_delete_by_email(self, email: str):
        user = self.get_user_by_email(email)
        if user.id in self.get_users():
            self.user_delete_service(user)      
    
    def user_delete_service(self, user: User):
        if user.role != "admin":
            self.repositorie.user_delete(user)
            print(f"Usuário removido\nNome: {user.name}\ne-mail: {user.email}")
        else:
            print("Contas com Role admin não podem ser removidas.")
    
    def user_update(self,id: int, name: str = None, email: str = None, role: str = None):
        user = self.get_user_by_id(id)
        UserUpdate(name, email, role)
        
        if user is None:
            print(f"ID '{id}' não cadastrado no banco de dados.")
            return None
        
        if name is not None:
            self.repositorie.dataBase[user.id].name = name 
        
        if email is not None:
            self.repositorie.dataBase[user.id].email = email
            
        if role is not None:
            self.repositorie.dataBase[user.id].role = UserRole(role)