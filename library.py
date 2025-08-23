class ventas:
  def generar_df_ventas(fecha, Bool_tabla):
    import pandas as pd
    import random as r
    import sqlite3 as sql
    abcdario = [
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
      'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
      'U', 'V', 'W', 'X', 'Y', 'Z'
      ]

    papelerias = [
      'Xochimilco', 'Cuemanco', 'Coapa', 'Milpa Alta',
      'CU', 'Zócalo', 'Narvarte', 'Santa Fé', 'Polanco',
      'Centro'
      ]

    lineas = [
        'Cuadernos', 'Libretas', 'Lápices', 'Plumones', 'Borradores', 'Sacapuntas',
        'Laptops', 'Tablets', 'Mochilas', 'Bolsas', 'Cajas', 'Pegamento', 'Tijeras',
        'Monitores', 'Teclados', 'Mouse', 'Audífonos', 'Cables', 'Cargadores', 'Baterías',
        'Pc', 'Uniformes', 'Pinturas', 'Pinceles', 'Papel', 'Cartulinas'
        ]

    # =========================== Parte II ==========================
    # Definimos listas vacias que posteriormente iremos llenando
    # con los datos de cada venta mediante la funcion append()
    # y el bucle for

    fechas = []
    productos = []
    claves = []
    cantidades = []
    precios = []
    totales = []
    sucursales = []

    # ========================= Parte III ==========================
    # Repetimos un bucle for 1000 times, where in each iteration
    # or each turn, we add a new element to each list
    for i in range(1, r.randint(1000, 50000)):
      # Zona de definicion de variables
        producto = r.choice(lineas)
        clave = r.choice(abcdario) + r.choice(abcdario) + r.choice(abcdario) + '-' + str(r.randint(1, 9)) + str(r.randint(1, 9)) + str(r.randint(1, 9))
        cantidad = r.randint(1, 50)
        precio = round(r.randint(1, 10000) * r.random(), 2)
        total = round(precio * cantidad, 2)
        sucursal = r.choice(papelerias)

        # Agregamos los datos a las listas
        fechas.append(fecha)
        productos.append(producto)
        claves.append(clave)
        cantidades.append(cantidad)
        precios.append(precio)
        totales.append(total)
        sucursales.append(sucursal)

    # ========================= Parte IV ==========================
    # Definimos un diccionario donde las claves seran los nombres
    # de las columnas y los valores seran las listas que llenamos
    dict_pre_ventas = {
        # clave: valores asociados
        #      : listas
        "Fecha": fechas,
        "Producto": productos,
        "Clave": claves,
        "Cantidad": cantidades,
        "Precio": precios,
        "Total": totales,
        "Sucursal": sucursales
    }

    # ========================== Parte V ==========================
    # Creamos el dataframe with the pandas function pd.DataFrame()
    df = pd.DataFrame(dict_pre_ventas)

    print(f"información del {fecha} generada con éxito")

    #Aquí quitamos el return para añadir la condicional y subir la info con sql

    #1 crearemos nuevamente la tabla de cero, abriendo por primera vez la conexión
    conexion= sql.connect("ventas_1.db")
    #2 incorporamos pd con el .to_sql si bool_tabla es true se crea la tabla por primera vez, si no añadiremos más info
    if Bool_tabla == True:
      df.to_sql(name="ventas_2025", if_exists="replace", con=conexion)
    else:
      df.to_sql(name="ventas_2025", if_exists="append", con=conexion)
    #3 cerramos la conexión
    conexion.close()
    print(f"información del {fecha} subida a la BBDD con éxito")

    #añadimos la función inicializadora
  def inicializador(fecha):
    ventas.generar_df_ventas(fecha, True)
  #añadimos la función de fecha
  def rango_fechas(fecha1, fecha2=None):
    import pandas as pd
    import sqlite3 as sql
    if fecha2 == None:
      ventas.generar_df_ventas(fecha1, False)
    else:
      #aquí formamos un parámetro predeterminado por si solo queremos una sola fecha en lugra de un rango de fechas
      #generamos la info para los demás días
      rango_fechas= pd.date_range(start=fecha1, end=fecha2, freq="d")
      for fecha in rango_fechas:
        ventas.generar_df_ventas(fecha, False)
  #añadimos la función de consulta
  def consulta(sentencia_sql):
    import sqlite3 as sql
    import pandas as pd
    #abrimos la conexion
    conexion = sql.connect("ventas_1.db")

    #para tener un mejor formato de tabla se pone esto, esto nos permite hacer consultas y extraer dataframes de pandas
    df_consulta= pd.read_sql_query(sentencia_sql, conexion)
    conexion.close()
    #mandamos a llamar a la variable
    return df_consulta