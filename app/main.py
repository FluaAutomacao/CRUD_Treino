from services.userService import UserServices
from schemas.userCreate import UserCreate
from schemas.userUpdate import UserUpdate
from repositories.userRepositorie import UserRepositorie

#Atributos---------*----------*---------*---------*----------*---------*
#Espaçamento usado entre múltiplos prints
espacamento = 1


#Instanciamento do banco de dados
repositorie = UserRepositorie()

#Instanciamento dos serviços
services = UserServices(repositorie)


#---------*----------*---------*---------*----------*---------*
#Banco de dados para cadstro de usuários, por hora apenas nome e e-mail
dados = [
    ("Flavio Gomes", "eng_fgomes@outlook.com", "flavio.gomes"),
    ("Ana Silva", "ana.silva@gmail.com", "ana.silva"),
    ("Bruno Costa", "bruno_costa123@hotmail.com", "bruno.costa"),
    ("Carlos Souza", "carlos.souza+dev@yahoo.com", "carlos.souza"),
    ("Daniel Oliveira", "daniel-oliveira@outlook.com", "daniel.oliveira"),
    ("Eduardo Pereira", "eduardo.pereira@empresa.com", "eduardo.pereira"),
    ("Eduardo Pereira", "eduardo.reizinho@brabonet.com", "eduardo.reizinho"),
    ("Fernanda Lima", "fernanda_lima+tech@gmail.com", "fernanda.lima"),
    ("Gabriel Rocha", "gabriel.rocha123@outlook.com", "gabriel.rocha"),
    ("Helena Martins", "helena.martins@yahoo.com", "helena.martins"),
    ("Heleninha Braba", "helena.martins@yahoo.com", "heleninha.braba"),
    ("Igor Fernandes", "igor_fernandes@empresa.com", "igor.fernandes"),
    ("Juliana Alves", "juliana.alves+dev@gmail.com", "juliana.alves"),
]

#Criação de usuários em loop usando metodo da classe serviços - simula várias requisições de novos usuários
#Retorna erro caso nome e/ou e-mail não seja(m) válido(s)
for name, email, username in dados:
    try:
        validateUser = UserCreate(name, email, username)
        services.create_user(validateUser.name, validateUser.email, validateUser.username)

    except ValueError as messenge:
        print(messenge)

#Iteração para gerar print do banco de dados completo
for key, value in services.get_users().items():
    print(f"ID: {key}\nNome:{value.name}\nE-mail: {value.email}\nUsername: '{value.username}\nCriado em: {value.created_at}'"+"\n" * espacamento)

#Separador dos itens no terminal---------*----------*---------*---------*----------*---------*
print("-"*20 + "\n" * espacamento)
#Testa a procura de usuário por ID - ID a ser procurada
searchID = 7

#Procura usuário por ID - Retorna erro caso ID não seja válida
searchedUserByID = services.get_user_by_id(searchID)
if searchedUserByID:
    print(f"Procurado por ID:\nID: {searchID}\nNome: {searchedUserByID.name}\nE-mail: {searchedUserByID.email}")
else:
    print(f"Não há cadastro ID '{searchID}' no banco de dados.")


#Separador dos itens no terminal---------*----------*---------*---------*----------*---------*
print("-"*20 + "\n" * espacamento)
#Procura usuário por nome - nome a ser procurado
searchName = "Eduardo Pereira"

#Se encontra usuário, printa seus dados. Se não encontra, informa usúaro não encontrado.

userFound = services.get_user_by_name(searchName)
if userFound:
    for user in userFound:
        print(f"Procurado por nome:\nID: {user.id}\nNome: {user.name}\nE-mail: {user.email}")
else:
    print(f"Não há cadastro '{searchName}' no banco de dados.")

#Separador dos itens no terminal---------*----------*---------*---------*----------*---------*
print("-"*20 + "\n" * espacamento)
#Procura usuário por e-mail - e-mail a ser procurado
searchEmail = "eng_fgomes@outlook.com"

#Se encontra usuário, printa seus dados. Se não encontra, informa usúaro não encontrado.

userFound = services.get_user_by_email(searchEmail)
if userFound:
    print(f"Procurado por e-mail:\nID: {userFound.id}\nNome: {userFound.name}\nE-mail: {userFound.email}")
else:
    print(f"E-mail '{searchEmail}' não cadastrado no banco de dados")

#Separador dos itens no terminal---------*----------*---------*---------*----------*---------*
print("-"*20 + "\n" * espacamento)

#Exemplo de tentativa de criaçaõ de usuário com e-mail repetido
try:
    services.create_user("Heleninha Braba", "helena.martins@yahoo.com", "Yoyo-jojo")
except ValueError as messenge:
    print(messenge)

#Separador dos itens no terminal---------*----------*---------*---------*----------*---------*
print("-"*20 + "\n" * espacamento)

#Remoção de usuário do banco de dados

# searchID = 0

#Remoção de usuário do banco de dados - baseado no ID do usuário
userID = 9
services.user_delete_by_id(userID)

#Remoção de usuário do banco de dados - baseado no e-mail
userEmail = "eng_fgomes@outlook.com"
services.user_delete_by_email(userEmail)

#Separador dos itens no terminal---------*----------*---------*---------*----------*---------*
print("-"*20 + "\n" * espacamento)

for key, value in services.get_users().items():
    print(f"ID: {key}\nNome:{value.name}\nE-mail: {value.email}"+"\n" * espacamento)


#Separador dos itens no terminal---------*----------*---------*---------*----------*---------*
print("-"*20 + "\n" * espacamento)

#Atualização de usuário

idUpdate = 1

userToUpdate = UserUpdate(name = "Joanazes Bebaz", username = "Jojoyoyo")
services.user_update(id = idUpdate, user = userToUpdate)




userUpdated = services.get_users()[idUpdate]
print(
    f"Usuário Atualizado\n"
    f"ID: {idUpdate}\n"
    f"Nome:{userUpdated.name}\n"
    f"E-mail: {userUpdated.email}\n"
    f"Role: {userUpdated.role}\n"
    f"Username: {userUpdated.username}\n"
    f"Criado em: {userUpdated.created_at}\n"
    f"Atualizado em: {userUpdated.updated_at}"
    + "\n" * espacamento)
