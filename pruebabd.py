import sqlite3

conexion= sqlite3.connect("/home/alumno/ProgramacionJuego/BDJuego.db")
cursor= conexion.cursor()

def guardar_ps(id_imdb, nombre, nom_ac, nom_su, tipo, url):
    sql = '''insert into PELICULASYSERIES(ID_IMDB, Nombre, Nombre_aceptado, Nombre_sugerido, Tipo, URL)
values ("{}", "{}", "{}", "{}", "{}", "{}");'''
    cursor.execute(sql.format(id_imdb, nombre, nom_ac, nom_su, tipo, url))
    conexion.commit()
    
def registrar_usuario(usuario, contrasena):
    sql = '''insert into USUARIOS(Usuario, Contrasena)
values ("{}", "{}");'''
    cursor.execute(sql.format(usuario, contrasena))
    conexion.commit()
    
def actualizar_ps(id_imdb, nom_su):
    pass

def aceptar_nombre(id_imdb):
    pass

def obtener_ps():
    pass


