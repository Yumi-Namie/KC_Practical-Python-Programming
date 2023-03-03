def encriptar(senha):
    import bcrypt
    bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt(8)
    hash = bcrypt.hashpw(bytes,salt)
    return hash

def encrypt_users():
    users = {'junior': 'lolailo123', 'adan':'senha123', 'ana':'anapass'}
    users_encriptados = {}
    for u,c in users.items():
        users_encriptados[u] = encriptar(c)
        #users_encriptados.update({u:c})
    return users_encriptados

def ask_user():
    str_user = input ("User name: ")
    str_pwd = input ("Password: ")
    senha = encriptar(str_pwd)
    return str_user, senha


def validate_user(usuario, senha):
    if users_encriptados.get(usuario) == senha:
        print("Entró en el sistema")
    else:
        print("No te conozco, no pasas")
   

if __name__ == '__main__':
    users_encriptados = encrypt_users()
    usuario, senha = ask_user()
    validate_user(usuario, senha)




