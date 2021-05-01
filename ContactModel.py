#Modelo de contacto
import db_manager

DATABASE_NAME = "ContactManager.db" 

dbmngr = db_manager.DbManager(DATABASE_NAME)

class contact:

    def __init__ (self):

        self.Id = ""
        self.Nombre = ""
        self.Apellido = ""
        self.Telefono = ""
        self.email = ""
        self.Puesto = ""
        self.company = ""
        self.ubicacion = ""

    def createContact(self):
        self.Id = int(input("Ingrese el ID: "))
        self.Nombre = input("Ingrese el nombre: ")
        self.Apellido = input("Ingrese el apellido: ")
        self.Telefono = int(input("Ingrese el teléfono: "))
        self.email = input("Ingrese el email")
        self.Puesto = input("Ingrese el puesto: ")
        self.company = input("Ingrese la compañía: ")
        self.ubicacion = input("Ingrese la ubicación: ")

        dbmngr.connectDB()
        conexion = dbmngr.conn
        cursor = conexion.cursor()
        cursor.execute("Insert into contacts (id, nombre, apellido, telefono, email, puesto, company, ubicacion) values (?,?,?,?,?,?,?,?)",
                        (self.Id, self.Nombre, self.Apellido, self.Telefono, self.Email, self.Puesto, self.Company, self.Ubicacion))
        
        conexion.commit()

        dbmngr.closeconnection()

        print(f'comunicacion realizada, contacto {self.id} creado excelente')

def main():
    usuario = Usuario()
    usuario.createUser()

if __name__ == '__main__':
    main()