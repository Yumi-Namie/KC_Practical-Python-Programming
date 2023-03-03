
def ask_user():
    str_user = input ("User name: ")
    str_pwd = input ("Password: ")
    return str_user, str_pwd

def validate_user(usuario, senha):
    users = {'junior': 'lolailo123', 'adan':'senha123', 'ana':'anapass'}
    if users.get(usuario) == senha:
        print("Entró en el sistema")
    else:
        print("No te conozco, no pasas")

if __name__ == '__main__':
    usuario, senha_encriptada = ask_user()
    validate_user(usuario, senha_encriptada)






