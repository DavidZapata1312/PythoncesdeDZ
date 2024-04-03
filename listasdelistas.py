class Usuario:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

# Función para agregar un nuevo usuario a la lista
def agregar_usuario(lista_usuarios, nombre, edad, correo):
    nuevo_usuario = Usuario(nombre, edad, correo)
    lista_usuarios.append(nuevo_usuario)
    print("Usuario agregado exitosamente.")

# Función para mostrar todos los usuarios almacenados
def mostrar_usuarios(lista_usuarios):
    if len(lista_usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        print("Lista de usuarios:")
        for i, usuario in enumerate(lista_usuarios, start=1):
            print(f"Usuario {i}:")
            print(f"Nombre: {usuario.nombre}")
            print(f"Edad: {usuario.edad}")
            print(f"Correo: {usuario.correo}")
            print()

# Lista para almacenar los usuarios
usuarios = []

# Ejemplo de uso
agregar_usuario(usuarios, "Juan", 25, "juan@example.com")
agregar_usuario(usuarios, "María", 30, "maria@example.com")

# Mostrar usuarios almacenados
mostrar_usuarios(usuarios)
