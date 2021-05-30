#creacion de tablas de contactos:

usersTable = """ CREATE TABLE IF NOT EXISTS Users (
                    id integer PRIMARY KEY,
                    password text not null,
                    nombre text null,
                    apellidos text null,
                    perfil text null,
                    area text null,
                    fechaCreacion text DEFAULT (datetime('now')),
                    activo integer DEFAULT 0
                ); """
contactsTable = """CREATE TABLE IF NOT EXISTS Contacts (
                   id integer PRIMARY KEY,
                   nombre text null, 
                   apellido text null,
                   Telefono integer, 
                   email text null, 
                   puesto text null, 
                   company text null, 
                   ubicacion text null, 
                   fechaCreacion text DEFAULT (datetime('now')), 
                   eliminado integer DEFAULT 0
                )
            """