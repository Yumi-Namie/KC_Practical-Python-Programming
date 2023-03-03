user = input("Usuario: ")
password = input ("Contraseña: ")

user2 = input("Confirme el usuario: ")
pass2 = input("Confirme la contraseña: ")

if user != user2 or password != pass2:
    print("No te conozco, no pasas.")
else: 
    print("Entró en el sistema")

