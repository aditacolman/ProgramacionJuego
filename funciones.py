from tkinter import *

def usuario_contrasena():
    nombre= nombreUsuario.get()
    contrasena= contrasenaUsuario.get()
    registrar_usuario(nombre, contrasena)

class ventana:
    indice = 0
    def crear_ventana_sesion(self):
        ventanaSesion = Tk()
        ventanaSesion.title("Login Usuario")
        mainFrame= Frame(ventanaSesion)
        mainFrame.pack()
        titulo= Label(mainFrame, text="Login de Usuario", font=("Arial 24"))
        titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        mainFrame.config(width=400, height=200) #bg= "#1AA1EE")
        iniciarSesion= Button(mainFrame, command=self.siguiente, text="Iniciar sesión")
        iniciarSesion.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        registrarUsuario= Button(mainFrame, command= usuario_contrasena, text="Registrar")
        registrarUsuario.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        nombreLabel= Label(mainFrame, text="Nombre: ")
        nombreLabel.grid(column=0, row=1)
        contrasenaLabel = Label(mainFrame, text="Contraseña: ")
        contrasenaLabel.grid(column=0, row=2)
        nombreUsuario= StringVar()
        nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
        nombreEntry.grid(column=1, row=1)
        contrasenaUsuario= StringVar()
        contrasenaEntry = Entry(mainFrame, textvariable=contrasenaUsuario, show="*")
        contrasenaEntry.grid(column=1, row=2)
        return ventanaSesion

    def crear_ventana_juego(self):
        ventanaJuego= Tk()
        ventanaJuego.title("")
        ventanaJuego.withdraw()
        return ventanaJuego

    def crear_ventana_eleccion(self):
        ventanaEleccion= Tk()
        ventanaEleccion.title("")
        ventanaEleccion.withdraw()
        elegirPeli= Button(ventanaEleccion,command=self.siguiente, text="Película").place(x=100, y=100)
        elegirSerie= Button(ventanaEleccion,command=self.siguiente, text="Serie").place(x=40, y=100)
        return ventanaEleccion
    
    def siguiente(self):
        self.windows[self.indice].withdraw()
        self.indice += 1
        self.windows[self.indice].deiconify()
        
    tipos = [crear_ventana_sesion, crear_ventana_eleccion, crear_ventana_juego]
    
    def __init__(self):
        self.vs = self.tipos[0](self)
        self.ve = self.tipos[1](self)
        self.vj = self.tipos[2](self)
        self.windows = [self.vs, self.ve, self.vj]