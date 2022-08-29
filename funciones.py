from tkinter import *
import bd_utils

class Interfaz:
    indice = 0
    
    def __init__(self):
        self.tipos = [self.crear_ventana_sesion, self.crear_ventana_eleccion, self.crear_ventana_juego]
        self.siguiente()
        
    def crear_ventana_sesion(self):
        ventanaSesion = ScreenLogin()
        ventanaSesion.ventana.deiconify()
        return ventanaSesion

    def crear_ventana_eleccion(self):
        ventanaEleccion= ScreenChoice()
        ventanaEleccion.ventana.deiconify()
        #ventanaEleccion.withdraw()
        return ventanaEleccion
    
    def crear_ventana_juego(self):
        ventanaJuego= ScreenGame()
        #poner deiconify()
        #ventanaJuego.withdraw()
        return ventanaJuego
    
    def siguiente(self):
        ventAct = self.tipos[self.indice]()
        ventAct.ventana.mainloop()
        self.indice += 1
        self.windows[self.indice].ventana.deiconify()

        

class ScreenLogin:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Login Usuario")
        #self.logueado = False
        mainFrame = Frame(self.ventana)
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
            sig.siguiente()
        else:
            print("Faltan datos")
    
class ScreenChoice:
    
    def __init__(self):
        
        self.ventana = Tk()
        self.ventana.title("")
        mainFrame = Frame(self.ventana)
        mainFrame.pack()
        titulo = Label(mainFrame, text="Elección de juego", font=("Arial 24"))
        titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        mainFrame.config(width=400, height=200) #bg= "#1AA1EE")
        serieBoton = Button(mainFrame, text="Serie")
        serieBoton.grid(column=1, row=3, ipadx=2, ipady=2, padx=5, pady=5)
        peliBoton = Button(mainFrame, text="Pelicula")
        peliBoton.grid(column=0, row=3, ipadx=2, ipady=2, padx=5, pady=5)
        print(self.ventana.deiconify())

class ScreenGame:
    pass
'''
    def __init__(self):
        self.ventgame = Tk()
        self.ventgame.title("")
        elegirPeli = Button(self.ventgame,text="Película").place(x=100, y=100)
        elegirSerie = Button(self.ventgame,text="Serie").place(x=40, y=100)
'''