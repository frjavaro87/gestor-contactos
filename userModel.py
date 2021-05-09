#usuarios
import db_manager

DATABASE_NAME = "usuarios.db" 

dbmngr = db_manager.DbManager(DATABASE_NAME)

class users:

    def __init__ (self):

        self.Id = ""
        self.Pass = ""
        self.Nombre = ""
        self.Apellido = ""
        self.Perfil = ""
        self.Area = ""
        
    def createUser(self):
        self.Id = int(input("Ingrese el ID: "))
        self.Pass = input("Ingrese el Pass: ")
        self.Nombre = input("Ingrese el Nombre: ")
        self.Apellido = input("Ingrese el Apellido: ")
        self.Perfil = input("Ingrese el Perfil: ")
        self.Area = input("Ingrese el Area: ")
        
        dbmngr.connectDB()
        conexion = dbmngr.conn
        cursor = conexion.cursor()
        cursor.execute("Insert into UsersTable (id, password, nombre, apellidos, perfil, area) values (?,?,?,?,?,?)",
                        (self.Id, self.Pass, self.Nombre, self.Apellido, self.Perfil, self.Area))

        conexion.commit()

        dbmngr.closeconnection()

        print(f'comunicacion realizada, user {self.id} creado excelente')

def main():
    contacto = users()
    contacto.createUser()

if __name__ == '__main__':
    
    main()