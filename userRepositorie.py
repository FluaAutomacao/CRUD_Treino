from models.user import User

class UserRepositorie:
    def __init__(self):
        self.dataBase = {}

    def save_user(self, user: User):
        user.id = len(self.dataBase)
        self.dataBase[user.id] = user
    
    def user_delete(self,user: User):
        self.dataBase.pop(user.id)

    # def user_update_name(self, user: User, dados: dict):
        
    #     self.dataBase[user.id]
