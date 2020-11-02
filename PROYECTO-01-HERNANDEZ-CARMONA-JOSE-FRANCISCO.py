from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products

Users = [["JFHC", "hola1"], 
         ["DHC", "PC2"]]

# ***************************USUARIO Y CONTRASEÑA***********************

acierto = 0
contador = 0

while acierto == 0:
  Usuario = str(input("Usuario: "))
  contraseña = str(input("Contraseña: "))

  acierto = 0

  for usuarios in Users:
    for contras in Users:

      if Usuario == usuarios[0] and contraseña == contras[1]:
        acierto = 1
       
  if acierto == 0:
    print("Error en Usuario y/o Contraseña, vuelva a Intentarlo...")  
    
# *********************************************************************


# ********* MENÚ DE OPCIONES *****************************************

print("""Menú de Opciones:
 1.- Categoría con menores Ventas.
 2.- Categoría con menores Búsquedas.
 3.- Categoría con mayores Ventas.
 4.- Categoría con mayores Búsquedas.
 5.- Sugerencia para el Retiro de Productos y reducción de acumulación de Inventario.
 6.- 50 Productos con mayores ventas.
 7.- 100 Productos con mayores búsquedas.
 8.- 50 Productos con menores ventas.
 9.- 100 Productos con menores Búsquedas.
 10.- Productos por reseña en el servicio.
 11.- Total de ingresos y ventas promedio mensuales y Total Anual y meses con mas ventas al año.""")

seleccion = int(input("\n\nSu selección: "))

contador_productos_ventas = 0
lista_productos_vendidos = [] 
lista_ventas_producto = []

#***MENORES VENTAS [[ID_SALE], [ID_PRODUCT], [SCORE 1 DE VENTAS BAJAS]]

#menores_ventas = []

#if seleccion == 1:
#  print("Respuesta en formato [[Id_Sale], [Id_Product], [Score bajo en este caso = 1]")
#  for low_sale in lifestore_sales:
#    if low_sale[2] == 1:
#      menores_ventas.append([low_sale[0],low_sale[1], low_sale[2]])
#print('\n ',menores_ventas)

if seleccion == 1:
  for producto in lifestore_products:
    for venta in lifestore_sales:
      if producto[0] == venta[1] and venta[2] == 1:
        contador += 1

    lista_ventas_producto.append([producto[0], contador])
    contador = 0
lista_ordenada = []

while lista_ventas_producto:
  menor = lista_ventas_producto[0][1]
  lista_actual = lista_ventas_producto[0]
  for producto in lista_ventas_producto:
    if producto[1] < menor:
      menor = producto[1]
      lista_actual = producto
  lista_ordenada.append(lista_actual)
  lista_ventas_producto.remove(lista_actual)
print(lista_ordenada)

#***********************************************************************

#********************MENORES BUSQUEDAS *********************************

lista_menor_busqueda = []
contador = 0

if seleccion == 2:
  for producto in lifestore_products:
    for busqueda in lifestore_searches:
      if producto[0] == busqueda[1]:
        contador += 1

    lista_menor_busqueda.append([producto[0], contador])
    contador = 0

lista_ordenada_menor = []

while lista_menor_busqueda:
  menor = lista_menor_busqueda[0][1]
  lista_actual_menor = lista_menor_busqueda[0]
  for producto in lista_menor_busqueda:
    if producto[1] < menor:
      menor = producto[1]
      lista_actual_menor = producto
  lista_ordenada_menor.append(lista_actual_menor)
  lista_menor_busqueda.remove(lista_actual_menor)
print(lista_ordenada_menor)

#********************************************************************

#*************MAYORES VENTAS ****************************************
if seleccion == 3:
  for producto in lifestore_products:
    for venta in lifestore_sales:
      if producto[0] == venta[1] and venta[2] == 5:
        contador += 1

    lista_ventas_producto.append([producto[0], contador])
    contador = 0
lista_ordenada = []

while lista_ventas_producto:
  mayor = lista_ventas_producto[0][1]
  lista_actual = lista_ventas_producto[0]
  for producto in lista_ventas_producto:
    if producto[1] > mayor:
      mayor = producto[1]
      lista_actual = producto
  lista_ordenada.append(lista_actual)
  lista_ventas_producto.remove(lista_actual)
print(lista_ordenada)

#*********************************************************************

#****************MAYORES BUSQUEDAS ***********************************

lista_mayor_busqueda = []
contador = 0

if seleccion == 4:
  for producto in lifestore_products:
    for busqueda in lifestore_searches:
      if producto[0] == busqueda[1]:
        contador += 1

    lista_mayor_busqueda.append([producto[0], contador])
    contador = 0

lista_ordenada_mayor = []

while lista_mayor_busqueda:
  mayor = lista_mayor_busqueda[0][1]
  lista_actual_mayor = lista_mayor_busqueda[0]
  for producto in lista_mayor_busqueda:
    if producto[1] > mayor:
      menor = producto[1]
      lista_actual_mayor = producto
  lista_ordenada_mayor.append(lista_actual_mayor)
  lista_mayor_busqueda.remove(lista_actual_mayor)
print(lista_ordenada_mayor)

#**********************************************************************

if seleccion == 5:
   print("""Se sugiere para el retiro de productos revisar la categoría de Menores ventas y menores Búsquedas, cuyos puntos muestran la problemática de este negocio en cuanto a pocas ventas, y de la mano tomar la decisión de reducir la acumulación de inventario visualizando la categoría de menores búsquedas para reducir los productos que no son de interes para el comprador, evitando así tener un sobre inventario eliminandolo y teniendo unicamente el inventario de rotación.""")

#**********************************************************************

#*************** 50 PRODUCTOS CON MAYORES VENTAS *********************

if seleccion == 6:
  categorias = [lifestore_products[0][3]]

  for producto in lifestore_products:
    nueva_categoria = 0
    for categoria in categorias:
      if producto[3] == categoria:
        continue
      else:
        nueva_categoria += 1

      if nueva_categoria+1 > len(categorias):
        categorias.append(producto[3])

 
  for categoria in categorias:
    top_50 = []
    for producto in lifestore_products:
      ventas_producto = 0
      for venta in lifestore_sales:
        if producto[0] == venta[1] and producto[3] == categoria:
          ventas_producto += 1
      if producto[3] == categoria:
        top_50.append([ventas_producto, producto])
    
    for i in range(len(top_50)):
      for j in range(len(top_50)):
        if top_50[i] > top_50[j]:
          auxiliar = top_50[j]
          top_50[j] = top_50[i]
          top_50[i] = auxiliar

    print("\n El top de productos con MAYORES ventas de la categoría", categoria, "es: \n")
    top_50 = top_50[0:50]
    for producto in top_50:
      print(producto)

#**********************************************************************

#***********100 PRODUCTOS CON MAYORES BÚSQUEDAS.********************

lista_mayor_busqueda = []
contador = 0
top100 = []

if seleccion == 7:
  for producto in lifestore_products:
    for busqueda in lifestore_searches:
      if producto[0] == busqueda[1]:
        contador += 1

    lista_mayor_busqueda.append([producto[0], contador])
    contador = 0

lista_ordenada_mayor = []

while lista_mayor_busqueda:
  mayor = lista_mayor_busqueda[0][1]
  lista_actual_mayor = lista_mayor_busqueda[0]
  for producto in lista_mayor_busqueda:
    if producto[1] > mayor:
      mayor = producto[1]
      lista_actual_mayor = producto
  lista_ordenada_mayor.append(lista_actual_mayor)
  lista_mayor_busqueda.remove(lista_actual_mayor)

for imprime in lista_ordenada_mayor:
  print(imprime)
#**********************************************************************

#******50 PRODUCTOS CON MENORES VENTAS*********************************

if seleccion == 8:
  categorias = [lifestore_products[0][3]]

  for producto in lifestore_products:
    nueva_categoria = 0
    for categoria in categorias:
      if producto[3] == categoria:
        continue
      else:
        nueva_categoria += 1

      if nueva_categoria+1 > len(categorias):
        categorias.append(producto[3])

 
  for categoria in categorias:
    top_50 = []
    for producto in lifestore_products:
      ventas_producto = 0
      for venta in lifestore_sales:
        if producto[0] == venta[1] and producto[3] == categoria:
          ventas_producto += 1
      if producto[3] == categoria:
        top_50.append([ventas_producto, producto])
    
    for i in range(len(top_50)):
      for j in range(len(top_50)):
        if top_50[i] < top_50[j]:
          auxiliar = top_50[j]
          top_50[j] = top_50[i]
          top_50[i] = auxiliar

    print("\n El top de productos con MENORES ventas de la categoría", categoria, "es: \n")
    top_50 = top_50[0:50]
    for producto in top_50:
      print(producto)

#*********************************************************************************

#****100 PRODUCTOS CON MENORES BÚSQUEDAS.****************************

lista_menor_busqueda = []
contador = 0
prod_100 = []

if seleccion == 9:
  for producto in lifestore_products:
    for busqueda in lifestore_searches:
      if producto[0] == busqueda[1]:
        contador += 1

    lista_menor_busqueda.append([producto[0], contador])
    contador = 0

  lista_ordenada_menor = []

while lista_menor_busqueda:
  menor = lista_menor_busqueda[0][1]
  lista_actual_menor = lista_menor_busqueda[0]
  for producto in lista_menor_busqueda:
    if producto[1] < menor:
      menor = producto[1]
      lista_actual_menor = producto
  prod_100.append(lista_actual_menor)
  lista_menor_busqueda.remove(lista_actual_menor)
  prod_100 = prod_100[0:101]
for visualiza in prod_100:  
  print(visualiza)

#*********************************************************************************

#*******20 PRODUCTOS MEJORES RESEÑAS**********************************

lista_mejores_20 = []
productos_mas_score = []
variable = 0
incrementa = 0
lista_mayor = []

if seleccion == 10:
  for producto in lifestore_products:
   for score in lifestore_sales:
     if producto[0] == score[1] and score[2] == 5:
       incrementa += 1
   productos_mas_score.append([producto[0], incrementa])
  incrementa = 0  
  print("Las 20 Peores reseñas son:\n")
  for k in range(20):
    print(productos_mas_score[k])



  while productos_mas_score:
    mayor = productos_mas_score[0][1]
    lista_actual_mayor = productos_mas_score[0]
    for producto in productos_mas_score:
      if producto[1] > mayor:
        mayor = producto[1]
        lista_actual_mayor = producto
    lista_mayor.append(lista_actual_mayor)
    productos_mas_score.remove(lista_actual_mayor)

  print("\nLos 20 mejores reseñas son: \n")
  for i in range(20):
    print(lista_mayor[i])

#*********************************************************************************

#*******************TOTAL DE INGRESOS Y VENTAS PROMEDIO MENSUALES*****************

if seleccion == 11:

  lista_precios = []
  total = 0
  contador = 0
  suma = 0
  lista_por_mes = []

  for productos in lifestore_products:
    for sales in lifestore_sales:
      if productos[0] == sales[1]:
        lista_precios.append([sales[3], productos[2]])
  
  for scan in lista_precios:
    total = total + int(scan[1])
  print("\nEl total de ingresos Anual es: ", total, "\n")

  print("\nSub-totales por mes y su promedio: \n")
  #*********************ENERO*************************************
  for enero in lista_precios:
    if enero[0][3] == '0' and enero[0][4] == '1':
      suma = suma + enero[1]
      contador += 1
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Enero: ", suma, ",    Promedio: ", promedio)
#***********************************************************************
  suma = 0
  contador = 0
#***********************FEBRERO*****************************************
  for febrero in lista_precios:
    if febrero[0][3] == '0' and febrero[0][4] == '2':
      suma = suma + febrero[1]
      contador += 1
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Febrero: ", suma, ",  Promedio: ", promedio)
#***********************************************************************
  suma = 0
#***********************MARZO*****************************************
  for marzo in lista_precios:
    if marzo[0][3] == '0' and marzo[0][4] == '3':
      suma = suma + marzo[1]
      contador += 1
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Marzo: ", suma, ",    Promedio: ", promedio)
#***********************************************************************
  suma = 0
#***********************ABRIL*****************************************
  for abril in lista_precios:
    if abril[0][3] == '0' and abril[0][4] == '4':
      suma = suma + abril[1]
      contador += 1
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Abril: ", suma, ",    Promedio: ", promedio)
#***********************************************************************
  suma = 0
#***********************MAYO*****************************************
  for mayo in lista_precios:
    if mayo[0][3] == '0' and mayo[0][4] == '5':
      suma = suma + mayo[1]
      contador += 1
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Mayo: ", suma, ",      Promedio: ", promedio)
#***********************************************************************
  suma = 0
#***********************JUNIO*****************************************
  for junio in lista_precios:
    if junio[0][3] == '0' and junio[0][4] == '6':
      suma = suma + junio[1]
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Junio: ", suma, ",     Promedio: ", promedio)
#***********************************************************************
  suma = 0
#***********************JULIO*****************************************
  for julio in lista_precios:
    if julio[0][3] == '0' and julio[0][4] == '7':
      suma = suma + julio[1]
      contador += 1
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Julio: ", suma, ",     Promedio: ", promedio)
#***********************************************************************
  suma = 0
#***********************AGOSTO*****************************************
  for agosto in lista_precios:
    if agosto[0][3] == '0' and agosto[0][4] == '8':
      suma = suma + agosto[1]
      contador += 1
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Agosto: ", suma, ",     Promedio: ", promedio)
#***********************************************************************
  suma = 0
#***********************SEPTIEMBRE**************************************
  for septiembre in lista_precios:
    if septiembre[0][3] == '0' and septiembre[0][4] == '9':
      suma = suma + septiembre[1]
      contador += 1
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Septiembre: ", suma, ", Promedio: ", promedio)
#***********************************************************************
  suma = 0
#***********************OCTUBRE*****************************************
  for octubre in lista_precios:
    if octubre[0][3] == '1' and octubre[0][4] == '0':
      suma = suma + octubre[1]
      contador += 1
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Octubre: ", suma, ",       Promedio: ", promedio)
#***********************************************************************
  suma = 0
#***********************NOVIEMBRE*****************************************
  for noviembre in lista_precios:
    if noviembre[0][3] == '1' and noviembre[0][4] == '1':
      suma = suma + noviembre[1]
      contador += 1
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Noviembre: ", suma, ",  Promedio: ", promedio)
#***********************************************************************
  suma = 0
#***********************DICIEMBRE*****************************************
  for diciembre in lista_precios:
    if diciembre[0][3] == '1' and diciembre[0][4] == '2':
      suma = suma + diciembre[1]
      contador += 1
  lista_por_mes.append(suma)
  promedio = suma / contador
  print("Ingresos de Diciembre: ", suma, ",     Promedio: ", promedio)
#***********************************************************************
  suma = 0

#***********************TOTAL ANUAL Y MESES CON MAS VENTAS**************

  lista_precios = []
  total = 0
  lista_promedio_mensual = []
  conteo = 0
  total_mes = 0
  contador2 = 0
  total2 = 0
  suma = 0
  auxiliar = 0
  lista_ordenada = []
  lista_actual = []


#*******************ORDENAMIENTO DE MAYOR A MENOR VENTAS DE CADA MES*************
   
  while lista_por_mes:
    mayor = lista_por_mes[0]
    lista_actual = lista_por_mes[0]
    for producto in lista_por_mes:
      producto2 = int(producto)
      if producto2 > mayor:
        mayor = producto
        lista_actual = producto
    lista_ordenada.append(lista_actual)
    lista_por_mes.remove(lista_actual)

  print("\nA Continuación la lista Ordenada de los meses de Mayor a Menor ventas.")

  print("\nAbril: ",      lista_ordenada[0])
  print("\nMarzo: ",      lista_ordenada[1])
  print("\nEnero: ",      lista_ordenada[2])
  print("\nFebrero: ",    lista_ordenada[3])
  print("\nMayo: ",       lista_ordenada[4])
  print("\nJunio: ",      lista_ordenada[5])
  print("\nJulio: ",      lista_ordenada[6])
  print("\nNoviembre: ",  lista_ordenada[7])
  print("\nSeptiembre: ", lista_ordenada[8])
  print("\nAgosto: ",     lista_ordenada[9])
  print("\nOctubre: ",    lista_ordenada[10])
  print("\nDiciembre: ",  lista_ordenada[11])
  
#******************************************************************************