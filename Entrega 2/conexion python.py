import psycopg2

conexion = psycopg2.connect(
host= "localhost",
user= "postgres",
password= "123456789",
database= "BD Amazon Books",
port = 5432
)

############### Base de datos de la tabla -> autor ########
#Utilizar cursor
cursor=conexion.cursor()

#Crear sentencia SQL
sql ='SELECT * FROM autor'

#Utilizar metodo execute
cursor.execute(sql)

#Mostrar resultado
registro = cursor.fetchall()
print(registro)
print("\n")

#Cerrar la conexion
cursor.close()
conexion.close()


############### Base de datos de la tabla -> usuario ########
cursor=conexion.cursor()
sql ='SELECT * FROM usuario'
cursor.execute(sql)
registro = cursor.fetchall()
print(registro)
print("\n")
cursor.close()
conexion.close()

############### Base de datos de la tabla -> categoria ########
cursor=conexion.cursor()
sql ='SELECT * FROM categoria'
cursor.execute(sql)
registro = cursor.fetchall()
print(registro)
print("\n")
cursor.close()
conexion.close()

############### Base de datos de la tabla -> ubicacion ########
cursor=conexion.cursor()
sql ='SELECT * FROM ubicacion'
cursor.execute(sql)
registro = cursor.fetchall()
print(registro)
print("\n")
cursor.close()
conexion.close()

############### Base de datos de la tabla -> libro ########
cursor=conexion.cursor()
sql ='SELECT * FROM libro'
cursor.execute(sql)
registro = cursor.fetchall()
print(registro)
print("\n")
cursor.close()
conexion.close()

############### Base de datos de la tabla -> evaluar ########
cursor=conexion.cursor()
sql ='SELECT * FROM evaluar'
cursor.execute(sql)
registro = cursor.fetchall()
print(registro)
print("\n")
cursor.close()
conexion.close()


