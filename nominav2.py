# Definición de la clase CalculadoraNomina
class CalculadoraNomina:
    def __init__(self, salario):
        self.salario = salario

    def calcular_vacaciones(self):
        return self.salario * 0.1  # Suponiendo que las vacaciones son el 10% del salario

    def calcular_cesantias(self):
        return self.salario * 0.0833  # Suponiendo que las cesantías son el 8.33% del salario

    def calcular_primas(self):
        return self.salario * 0.0833  # Suponiendo que las primas son el 8.33% del salario


# Base de datos de empleados (nombre de usuario y contraseña)
empleados = {
    'empleado1': 'contrasena1',
    'empleado2': 'contrasena2',
    'empleado3': 'contrasena3'
}


def login():
    # Pedir al usuario que ingrese su nombre de usuario y contraseña
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")

    # Verificar si el nombre de usuario existe y si la contraseña es correcta
    if usuario in empleados and empleados[usuario] == contrasena:
        print("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(usuario))
        # Obtener el salario del empleado
        salario = float(input("Ingrese el salario del empleado: "))
        if salario < 0:
            raise ValueError("El salario no puede ser negativo.")

        # Crear una instancia de la CalculadoraNomina con el salario proporcionado
        calculadora = CalculadoraNomina(salario)

        # Calcular vacaciones, cesantías y primas
        vacaciones = calculadora.calcular_vacaciones()
        cesantias = calculadora.calcular_cesantias()
        primas = calculadora.calcular_primas()

        # Imprimir resumen de nómina
        print("\n--- Resumen de Nómina ---")
        print("Salario:", salario)
        print("Vacaciones:", vacaciones)
        print("Cesantías:", cesantias)
        print("Primas:", primas)
    else:
        print("Nombre de usuario o contraseña incorrectos.")


# Ejecutar la función de inicio de sesión
login()
