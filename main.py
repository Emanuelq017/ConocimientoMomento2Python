class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = self.calcular_precio_venta(margen_de_venta)

    def calcular_precio_venta(self, margen_de_venta):
        return self.costo / (1 - margen_de_venta)

    def registrar_producto(self, productos):
        productos[self.id] = {
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'costo': self.costo,
            'cantidad': self.cantidad,
            'precio_de_venta': self.precio_de_venta
        }

    @staticmethod
    def imprimir_productos(productos):
        for id, producto in productos.items():
            print(f"ID: {id}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Costo: {producto['costo']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio de Venta: {producto['precio_de_venta']}")
            print("------")


# Función para obtener datos del usuario
def obtener_datos_producto():
    id = int(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    costo = float(input("Ingrese el costo del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    margen_de_venta = float(input("Ingrese el margen de venta (porcentaje): ")) / 100

    return id, nombre, descripcion, costo, cantidad, margen_de_venta


# Uso de la clase con interacción del usuario
productos = {}

options = 0

while options == 0:
    print("-------------Menú----------------")
    print("---------------------------------")
    print("----1-Registrar un producto------")
    print("-------2-Listar productos--------")
    print("-----------3-Salir---------------")
    print("---------------------------------")
    option = input("Opción =====> ")
    if option == "3":
        options = 3

    while option == "1":
        opcion = input("¿Desea registrar un nuevo producto? (s/n): ")

        if opcion.lower() != 's':
            break

        datos_producto = obtener_datos_producto()
        nuevo_producto = Producto(*datos_producto)
        nuevo_producto.registrar_producto(productos)

    if option == "2":
        Producto.imprimir_productos(productos)
