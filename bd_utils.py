import sqlite3

class Base:
    def __init__(self):
        self.conexion = sqlite3.connect("/home/alumno/ProgramacionJuego/BDJuego.db")
        self.cursor = conexion.cursor()
        self.respuestas_registrousuario = ["El registro de usuario ha sido exitoso", "La contraseña es incorrecta", "El usuario no existe"]

    def guardar_ps(self, id_imdb, nombre, nom_ac, nom_su, tipo, url):
        sql = '''insert into PELICULASYSERIES(ID_IMDB, Nombre, Nombre_aceptado, Nombre_sugerido, Tipo, URL)
    values ("{}", "{}", "{}", "{}", "{}", "{}");'''
        cursor.execute(sql.format(id_imdb, nombre, nom_ac, nom_su, tipo, url))
        conexion.commit()

    def existe_usuario(self, usuario):
        self.cursor.execute('SELECT * FROM USUARIOS WHERE Usuario ="{usuario}";')
        respuesta = self.cursor.fetchall()
        if respuesta:
            return True
        return False

    def registro_usuario(self, usuario, contrasena):
        if not self.existe_usuario(usuario):
            self.cursor.execute('INSERT INTO USUARIOS (Usuario, Contrasena) VALUES ("{usuario}", "{contrasena}");'))
            self.conexion.commit()
            return 0
        else:
            return 1
'''
sql = '''insert into USUARIOS(Usuario, Contrasena) values ("{}", "{}");'''
self.cursor.execute(sql.format(usuario, contrasena))
self.conexion.commit()
'''

    def login(self, usuario, contrasena):
        self.cursor.execute(f'SELECT * FROM USUARIOS WHERE Usuario ="{usuario}";')
        respuesta= self.cursor.fetchall()
        self.conexion.commit()
        if resp:
            if respuesta[0][2] == contrasena:
                return 0
            else:
                return 1
        else:
            return 2

def actualizar_ps(id_imdb, nom_su):
    pass


def aceptar_nombre(id_imdb):
    pass


def obtener_ps():
    pass


