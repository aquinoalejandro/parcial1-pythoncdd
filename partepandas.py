import pandas as pd

productos = [
{"nombre": "Camiseta", "precio": 20, "cantidad_disponible":
100},
{"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
{"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
{"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
{"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
{"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
{"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
{"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
{"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
{"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible":
25},
{"nombre": "Calcetines", "precio": 10, "cantidad_disponible":
150},
{"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
{"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
{"nombre": "Pendientes", "precio": 15, "cantidad_disponible":
180},
{"nombre": "Cinturón", "precio": 20, "cantidad_disponible":
100},
{"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
{"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
{"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
{"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
{"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]

def operaciones(productos):
    #creo un dataframe con la lista
    df = pd.DataFrame(productos, columns=["nombre", "precio", "cantidad_disponible"])
    #total de inventario
    df["total_inventario"] = df["precio"] * df["cantidad_disponible"]
    #valor total de inventario(suma de todos los valores)
    df["valor_total_inventario"] = df["total_inventario"].cumsum()
    #ventas
    df["update_cantidad"] = df["cantidad_disponible"].replace(80,79)
    df["update_cantidad"] = df["update_cantidad"].replace(200,198)
    df["update_cantidad"] = df["update_cantidad"].replace(35,32)
    #cantidad de vendidos
    df["cantidad_vendidos"] = df["cantidad_disponible"] - df["update_cantidad"]
    print(df)
    #crear un nuevo dataframe con las columans nombre y cantidad de cada producto
    nuevo_df = pd.DataFrame(df, columns=["nombre"])
    nuevo_df["cantidad"] = df["update_cantidad"]

    return nuevo_df



dataframe = operaciones(productos)
print(dataframe)