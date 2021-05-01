import sqlite3
from sqlite3 import Error
from time import sleep
from tables import usersTable, contactsTable

class DbManager:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn= None
    
    

    def createTables(self):

        if self.conn is not None:
            try:
                cursor = self.conn.cursor()
                cursor.execute(usersTable)
                print("Tabla de usuarios creada exitosa")
            except Error as err:
                print(err)
        else:
            print("No hay conexion a DB")

        if self.conn is not None:
            try:
                cursor = self.conn.cursor()
                cursor.execute(contactsTable)
                print("Tabla de contactos creada exitosa")
            except Error as err:
                print(err)
        else:
            print("No hay conexion a DB")

    def connectDB(self):
        self.conn = sqlite3.connect(self.db_name)
        print("Conexión a la matrix existosa")

    def validateDB(self):
        try:
            print(f'verificando si {self.db_name} existe o no, de no ser asi, se ejecuta la creacion...')
            self.conn = sqlite3.connect(self.db_name, uri=True)
            print(f'La base existe, conexion a {self.db_name}')
        except:
            print('Error: la base de datos no existe,Inicializacion Instalacion')
            self.conn = sqlite3.connect(self.db_name, uri=True)
            print('Base de datos creada exitosamente')

    def closeConnection(self):
        if self.conn == None:
            print('La conexion se cerró')
        else:
            self.conn.close()
            print("Conexión terminada") 

def main():
 
    DATABASE_NAME = input("Como se va a llamar la base de datos?: ")
    DATABASE_NAME = DATABASE_NAME + ".db"
    dbmngr = DbManager(DATABASE_NAME)
    dbmngr.validateDB()
    dbmngr.createTables()
    dbmngr.connectDB()
    dbmngr.closeConnection()

if __name__ == '__main__':

    main()

