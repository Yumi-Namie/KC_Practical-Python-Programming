def encrypt_users():
    users = {'junior': 'lolailo123', 'adan':'senha123', 'ana':'anapass'}
    for u,c in users.items():
        users_encriptados = {}
        users_encriptados[u] = encriptar(c)
        print (users_encriptados)

def encriptar(senha):
    import bcrypt
    bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes,salt)
    return hash

encrypt_users()