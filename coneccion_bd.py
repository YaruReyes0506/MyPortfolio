import mysql.connector
from mysql.connector import Error

def obtener_coneccion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='contactos',
            user='root',
            password='@Carrillo0508'
        )
        if conexion.is_connected():
            print('Conexion exitosa a la base de datos')
            return conexion
        else: 
            print('No se pudo establecer una conexion')
            return None
    except Error as e:
        print(f'Error al conectar a la base de datos {e}')
        return None
