class UserRequest():

    def __init__(self, name: str, email: str):
        self.validate_name(name)
        self.validate_email(email)
        self.name = name
        self.email = email
        

    def validate_name (self, name: str):
        if name == "":
            raise ValueError("Nome está vazio.")
        for char in name:
            if not(char.isalpha()):
                if char != " ":
                    raise ValueError("Apenas letras são aceitas no nome.")
                
    def validate_email (self, email: str):
        count = 0
        index = -1

        if not("@" in email):
            raise ValueError("e-mail não é válido")
        for idx, char in enumerate(email):
            if not char.isalnum():
                if char == "@":
                    if count == 0:
                        count = 1
                        index = idx
                    else:
                        raise ValueError("e-mail não é válido. Tem mais de um @ declarado")
                elif not char in "._-+" and not count:
                    raise ValueError("e-mail não é válido. e-mail pode ter letras, números e caractéres . _ - + antes do @.")
                elif not char in "._-" and count:
                    raise ValueError("e-mail não é válido. e-mail pode ter letras, números e caractéres . _ - após @.")
        
        if not ".com" in email:
            raise ValueError("e-mail não possui .com")