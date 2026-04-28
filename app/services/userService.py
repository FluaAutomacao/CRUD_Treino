from models.user import User
# from schemas.userCreate import UserCreate
from schemas.userUpdate import UserUpdate
from repositories.userRepositorie import UserRepositorie
from models.userRole import UserRole
from datetime import datetime, timezone

class UserServices():
    def __init__(self, repositorie: UserRepositorie):
        self.repositorie = repositorie

    def create_user(self, name: str, email: str, username: str)-> User:
        #Verifica se já tem o username no banco de dados
        self.user_username_validate(username)
        
        #Verifica se já tem o e-mail no banco de dados
        self.user_email_validate(email)
        
        #Cria usuário
        userData = User(name, email, username)
        #Salva usuário no banco de dados
        self.repositorie.save_user(userData)
        return userData
    
    def user_username_validate(self, username: str) -> None:
        if self.get_user_by_name(username) is []:
            raise ValueError(f"Username '{username}' já cadastrado no banco de dados.")
        
    def user_email_validate(self, email: str) -> None:
        if self.get_user_by_email(email) is not None:
            raise ValueError(f"E-mail {email} já cadastrado no banco de dados.")
       
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
            
    def get_user_by_username(self, username: str) -> User:
        dataBase = self.get_users()
        for value in dataBase.values():
            if value.username == username:
                return value
            
    def user_delete_by_id(self, id: int):
        if id in self.get_users():
            self.user_delete_service(self.get_user_by_id(id))

    def user_delete_by_email(self, email: str):
        user = self.get_user_by_email(email)
        if user is not None:
            if user.id in self.get_users():
                self.user_delete_service(user)      
    
    def user_delete_service(self, user: User):
        if user.role != "admin":
            self.repositorie.user_delete(user)
            print(f"Usuário removido\nNome: {user.name}\ne-mail: {user.email}")
        else:
            print("Contas com Role admin não podem ser removidas.")
    
    
    
    def user_update(self,id: int, user: UserUpdate) -> None:
        currentUser = self.get_user_by_id(id)
        updated = False

        if currentUser is None:
            print(f"ID '{id}' não cadastrado no banco de dados.")
            return None
        
        
        
        currentUser.apply_update(user)

        

    
    # def user_update(self,id: int, user: UserUpdate):
    #     currentUser = self.get_user_by_id(id)
    #     updated = False

    #     if currentUser is None:
    #         print(f"ID '{id}' não cadastrado no banco de dados.")
    #         return None
        
    #     if user.name is not None:
    #         self.repositorie.dataBase[currentUser.id].name = user.name
    #         updated = True
        
    #     if user.email is not None:
    #         self.repositorie.dataBase[currentUser.id].email = user.email
    #         updated = True

    #     if user.username is not None:
    #         self.repositorie.dataBase[currentUser.id].username = user.username
    #         updated = True
            
    #     if user.role is not None:
    #         self.repositorie.dataBase[currentUser.id].role = UserRole(user.role)
    #         updated = True
        
    #     if updated:
    #         user.updated_at = datetime.now(timezone.utc)