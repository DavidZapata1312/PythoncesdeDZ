class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Supermercado:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                print("Producto eliminado exitosamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, nombre, nuevo_nombre, nuevo_precio):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.nombre = nuevo_nombre
                producto.precio = nuevo_precio
                print("Producto actualizado exitosamente.")
                return
        print("Producto no encontrado.")

    def listar_productos(self):
        if self.productos:
            print("Lista de productos:")
            for producto in self.productos:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}")
        else:
            print("No hay productos en el supermercado.")

def menu():
    print("\n--- Menú ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Listar productos")
    print("5. Salir")

supermercado = Supermercado()

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        producto = Producto(nombre, precio)
        supermercado.agregar_producto(producto)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        supermercado.eliminar_producto(nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
        supermercado.actualizar_producto(nombre, nuevo_nombre, nuevo_precio)
    elif opcion == "4":
        supermercado.listar_productos()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
