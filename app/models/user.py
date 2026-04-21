class User:
    # ATRIBUTOS / CONSTANTES
    DEFAULT_ROLE = "user"

    # CONSTRUTORES

    def __init__(self, name: str, email: str):
        self.name = name   
        self.email = email
        self.id = -1
        self.role = self.DEFAULT_ROLE
        #self.user = [self.name, self.email]
        #return self.user
        # return [self.name, self.email, self.id]
