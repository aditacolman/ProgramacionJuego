from tkinter import *
import bd_utils



class Interfaz:
    indice = 0
    
    def __init__(self):
        self.vs = self.tipos[0](self)
        self.ve = self.tipos[1](self)
        self.vj = self.tipos[2](self)
        self.windows = [self.vs, self.ve, self.vj]
        
    def crear_ventana_sesion(self):
        ventanaSesion = ScreenLogin()
        return ventanaSesion

    def crear_ventana_eleccion(self):
        ventanaEleccion= ScreenChoice()
        ventanaEleccion.withdraw()
        return ventanaEleccion
    
    def crear_ventana_juego(self):
        ventanaJuego= ScreenGame()
        ventanaJuego.withdraw()
        return ventanaJuego
    
    def siguiente(self):
        self.windows[self.indice].withdraw()
        self.indice += 1
        self.windows[self.indice].deiconify()

    tipos = [crear_ventana_sesion, crear_ventana_eleccion, crear_ventana_juego]

class ScreenLogin:

    def __init__(self):
        self.ventlogin = Tk()
        self.ventlogin.title("Login Usuario")
        #self.logueado = False
        mainFrame = Frame(self.ventlogin)
        mainFrame.pack()
        titulo = Label(mainFrame, text="Login de Usuario", font=("Arial 24"))
        titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        mainFrame.config(width=400, height=200) #bg= "#1AA1EE")
        iniciarSesion = Button(mainFrame, command=self.verificar_uc, text="Iniciar sesión")
        iniciarSesion.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        registroUsuario = Button(mainFrame, command=self.registrar_usuario, text="Registrar")
        registroUsuario.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        nombreLabel = Label(mainFrame, text="Nombre: ")
        nombreLabel.grid(column=0, row=1)
        contrasenaLabel = Label(mainFrame, text="Contraseña: ")
        contrasenaLabel.grid(column=0, row=2)
        self.nombreUsuario= StringVar()
        nombreEntry = Entry(mainFrame, textvariable=self.nombreUsuario)
        nombreEntry.grid(column=1, row=1)
        self.contrasenaUsuario= StringVar()
        contrasenaEntry = Entry(mainFrame, textvariable=self.contrasenaUsuario, show="*")
        contrasenaEntry.grid(column=1, row=2)
        self.base = bd_utils.Base()
    
    def registrar_usuario(self):
        nombre= self.nombreUsuario.get()
        contrasena= self.contrasenaUsuario.get()
        if nombre  and contrasena:
            resp = self.base.registro_usuario(nombre, contrasena)
            print(self.base.respuestas_registrousuario[resp])
        else:
            print("Faltan datos")
    
    def verificar_uc(self):
        nombre= self.nombreUsuario.get()
        contrasena= self.contrasenaUsuario.get()
        if nombre and contrasena:
            resp = self.base.iniciar_sesion(nombre, contrasena)
            print(self.base.respuestas_login[resp])
            sig= Interfaz()
            Interfaz.siguiente()
        else:
            print("Faltan datos")
    
class ScreenChoice:
    
    def __init__(self):
        self.ventchoice = Tk()
        self.ventchoice.title("")
        mainFrame = Frame(self.ventchoice)
        mainFrame.pack()
        titulo = Label(mainFrame, text="Elección de juego", font=("Arial 24"))
        titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        mainFrame.config(width=400, height=200) #bg= "#1AA1EE")
        serieBoton = Button(mainFrame, text="Iniciar sesión")
        serieBoton.grid(column=1, row=3, ipadx=2, ipady=2, padx=5, pady=5)
        peliBoton = Button(mainFrame, text="Registrar")
        peliBoton.grid(column=0, row=3, ipadx=2, ipady=2, padx=5, pady=5)


class ScreenGame:

    def __init__(self):
        self.ventgame = Tk()
        self.ventgame.title("")
        elegirPeli = Button(self.ventgame, command=self.siguiente, text="Película").place(x=100, y=100)
        elegirSerie = Button(self.ventgame, command=self.siguiente, text="Serie").place(x=40, y=100)
