import os 
os.system("cls")


#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}


#stock = {modelo: [precio, stock], ...] 

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],
}



def stock_marca(marca):
    marca_lower = marca.lower()
    total_stock = 0
    for modelo, info in productos.items():
        if info[0].lower() == marca_lower:
            total_stock += stock.get(modelo, [0,0])[1]
    print(f"El stock de la marca {marca} es: {total_stock}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, (precio, stk) in stock.items():
        if stk > 0 and p_min <= precio <= p_max:
            marca = productos[modelo][0]
            resultados.append(f"{marca} {modelo} - Precio: {precio}")
    resultados.sort()
    if resultados:
        print(f"Los notebooks entre los precios consulta son:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p 
        return True
    else:
        return False

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Debe ingresar valores enteros!!")


while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    opcion = input("Ingrese opción: ").strip()

    if opcion == '1':
        marca = input("Ingrese marca a consultar: ").strip()
        stock_marca(marca)

    elif opcion == '2':
        p_min = pedir_entero("Ingrese precio mínimo: ")
        p_max = pedir_entero("Ingrese precio máximo: ")
        busqueda_precio(p_min, p_max)

    elif opcion == '3':
        while True:
            modelo = input("Ingrese modelo a actualizar: ").strip()
            try:
                p = int(input("Ingrese precio nuevo: "))
            except ValueError:
                print("Debe ingresar valores enteros!!")
                continue
            exito = actualizar_precio(modelo, p)
            if exito:
                print("Precio actualizado!!")
            else:
                print("El modelo no existe!!")

            otro = input("Desea actualizar otro precio (s/n)?: ").strip().lower()
            if otro != 'si' and otro != 's':
                break

    elif opcion == '4':
        print("Programa finalizado.")
        break

    else:
        print("Debe seleccionar una opción válida!!")

    