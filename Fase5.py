# Matriz del menú: [Nombre del Producto, Categoría, Precio Base]

menu = [
    ["Hamburguesa", "Comida Rápida", 25000],
    ["Pizza", "Comida Rápida", 32000],
    ["Ensalada César", "Saludable", 18000],
    ["Jugo Natural", "Bebida", 12000],
    ["Pasta Alfredo", "Italiana", 28000],
    ["Helado", "Postre", 10000]
]

# Función para calcular el precio final
def calcular_precio_final(producto, categoria_objetivo, umbral):
    nombre, categoria, precio_base = producto

    # Aplicar descuento del 15%
    if categoria == categoria_objetivo and precio_base > umbral:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base

    return precio_final

# Parámetros de la promoción
categoria_objetivo = "Comida Rápida"
umbral = 20000

# Mostrar resultados
print("PROMOCIÓN DEL MENÚ\n")

for producto in menu:
    nombre, categoria, precio_base = producto
    precio_final = calcular_precio_final(
        producto,
        categoria_objetivo,
        umbral
    )

    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base: $", precio_base)
    print("Precio Final: $", precio_final)
    print("-----------------------------")