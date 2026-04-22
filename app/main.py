from services.userService import UserServices

#Atributos---------*----------*---------*---------*----------*---------*
#Espaçamento usado entre múltiplos prints
espacamento = 1


#---------*----------*---------*---------*----------*---------*
#Banco de dados para cadstro de usuários, por hora apenas nome e e-mail
dados = [
    ("Flavio Gomes","eng_fgomes@outlook.com"),
    ("Ana Silva", "ana.silva@gmail.com"),
    ("Bruno Costa", "bruno_costa123@hotmail.com"),
    ("Carlos Souza", "carlos.souza+dev@yahoo.com"),
    ("Daniel Oliveira", "daniel-oliveira@outlook.com"),
    ("Eduardo Pereira", "eduardo.pereira@empresa.com"),
    ("Eduardo Pereira", "eduardo.reizinho@brabonet.com"),
    ("Fernanda Lima", "fernanda_lima+tech@gmail.com"),
    ("Gabriel Rocha", "gabriel.rocha123@outlook.com"),
    ("Helena Martins", "helena.martins@yahoo.com"),
    ("Heleninha Braba", "helena.martins@yahoo.com"),
    ("Igor Fernandes", "igor_fernandes@empresa.com"),
    ("Juliana Alves", "juliana.alves+dev@gmail.com"),]

#Criação da classe de serviços - gerencia as regras internas
services = UserServices()


#Criação de usuários em loop usando metodo da classe serviços - simula várias requisições de novos usuários
#Retorna erro caso nome e/ou e-mail não seja(m) válido(s)
for name, email in dados:
    try:
        services.create_user(name, email)
    except ValueError as messenge:
        print(messenge)

#Iteração para gerar print do banco de dados completo
for key, value in services.get_users().items():
    print(f"ID: {key}\nNome:{value.name}\nE-mail: {value.email}"+"\n" * espacamento)

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
    services.create_user("Heleninha Braba", "helena.martins@yahoo.com")
except ValueError as messenge:
    print(messenge)

#Separador dos itens no terminal---------*----------*---------*---------*----------*---------*
print("-"*20 + "\n" * espacamento)

#Remoção de usuário do banco de dados

searchID = 0

#Remoção de usuário do banco de dados - baseado no ID do usuário
userID = 9
services.user_delete_by_id(userID)

#Remoção de usuário do banco de dados - baseado no nome
userEmail = "eng_fgomes@outlook.com"
# print(services.get_user_by_name(userName))
services.user_delete_by_email(userEmail)

#Separador dos itens no terminal---------*----------*---------*---------*----------*---------*
print("-"*20 + "\n" * espacamento)

for key, value in services.get_users().items():
    print(f"ID: {key}\nNome:{value.name}\nE-mail: {value.email}"+"\n" * espacamento)


#Separador dos itens no terminal---------*----------*---------*---------*----------*---------*
print("-"*20 + "\n" * espacamento)

#Atualização de usuário

idUpdate = 1

services.user_update(id = idUpdate, name = "Joanazes Bebaz", email = "joninhas@bol.com.br")


userUpdated = services.get_users()[idUpdate]
print(f"Usuário Atualizado\nID: {idUpdate}\nNome:{userUpdated.name}\nE-mail: {userUpdated.email}\nRole: {userUpdated.role}"+"\n" * espacamento)