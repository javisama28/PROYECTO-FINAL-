# Constantes
PRECIO_BASE = 20.0
PRECIO_AZUCAR = 0.5
PRECIO_AGUA = -2.0
PRECIO_SOYA = 3.0
AUMENTO_TAMAÑO = 0.05

# Variables globales
nombre_cliente = ""
nit_cliente = ""
azucar = 0
tipo_leche = "deslactosada"
tamaño = "normal"
precio = PRECIO_BASE

# Funciones
def solicitar_datos_cliente():
    global nombre_cliente, nit_cliente
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    nit = input("¿Desea ingresar NIT? (s/n): ")
    if nit.lower() == "s":
        nit_cliente = input("Ingrese el NIT: ")

def ver_informacion_pedido():
    print("\nInformación del pedido:")
    print(f"Cliente: {nombre_cliente}")
    if nit_cliente:
        print(f"NIT: {nit_cliente}")
    print(f"Producto: Licuado de fresa con leche {tipo_leche}")
    if azucar > 0:
        print(f"Azúcar: {azucar} cucharada(s)")
    print(f"Tamaño: {tamaño}")
    print(f"Precio: Q{precio:.2f}")

def agregar_azucar():
    global azucar, precio
    if azucar < 2:
        azucar += 1
        precio += PRECIO_AZUCAR
        print(f"Se ha agregado {azucar} cucharada(s) de azúcar.")
        print(f"El precio por la azúcar es: Q{azucar * PRECIO_AZUCAR:.2f}")
    else:
        print("No se puede agregar más azúcar, se ha alcanzado el límite de 2 cucharadas.")

def modificar_leche():
    global tipo_leche, precio
    print("Seleccione el tipo de leche:")
    print("1. Sin leche (únicamente con agua)")
    print("2. Leche deslactosada")
    print("3. Leche entera")
    print("4. Leche de soya")
    opcion = input("Ingrese el número correspondiente: ")
    if opcion == "1":
        tipo_leche = "agua"
        precio += PRECIO_AGUA
    elif opcion == "2":
        tipo_leche = "deslactosada"
    elif opcion == "3":
        tipo_leche = "entera"
    elif opcion == "4":
        tipo_leche = "soya"
        precio += PRECIO_SOYA
    else:
        print("Opción inválida, se mantendrá la leche deslactosada.")

def agrandar_tamaño():
    global tamaño, precio
    if tamaño == "normal":
        tamaño = "grande"
        precio *= (1 + AUMENTO_TAMAÑO)
        print("El tamaño del licuado ha sido aumentado a grande.")
    else:
        print("El licuado ya está en tamaño grande, no se puede agrandar más.")

def confirmar_pedido():
    ver_informacion_pedido()
    print("\n¡Muchas gracias por su compra!")
    print("Su licuado está listo para ser servido.")

# Programa principal
solicitar_datos_cliente()

while True:
    print("\nMenú de opciones:")
    print("1. Ver información del pedido")
    print("2. Agregar azúcar")
    print("3. Modificar leche")
    print("4. Agrandar")
    print("5. Confirmar")
    opcion = input("Ingrese el número correspondiente a la opción deseada: ")

    if opcion == "1":
        ver_informacion_pedido()
    elif opcion == "2":
        agregar_azucar()
    elif opcion == "3":
        modificar_leche()
    elif opcion == "4":
        agrandar_tamaño()
    elif opcion == "5":
        confirmar_pedido()
        break
    else:
        print("Opción inválida, intente nuevamente.")