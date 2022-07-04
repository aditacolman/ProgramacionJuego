import requests
import json
import random
from tkinter import *
from pruebabd import registrar_usuario
import funciones
from functools import partial

#Ventana de sesión
ventanaSesion = Tk()
ventanaSesion.title("Login Usuario")

#mainFrame de sesión
mainFrame= Frame(ventanaSesion)
mainFrame.pack()
mainFrame.config(width=400, height=200) #bg= "#1AA1EE")

#Textos y titulos de sesión
titulo= Label(mainFrame, text="Login de Usuario", font=("Arial 24"))
titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

#Label's de sesión
nombreLabel= Label(mainFrame, text="Nombre: ")
nombreLabel.grid(column=0, row=1)
contrasenaLabel = Label(mainFrame, text="Contraseña: ")
contrasenaLabel.grid(column=0, row=2)

#Entradas de texto
nombreUsuario= StringVar()
nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
nombreEntry.grid(column=1, row=1)
contrasenaUsuario= StringVar()
contrasenaEntry = Entry(mainFrame, textvariable=contrasenaUsuario, show="*")
contrasenaEntry.grid(column=1, row=2)

def usuario_contrasena():
    nombre= nombreUsuario.get()
    contrasena= contrasenaUsuario.get()
    registrar_usuario(nombre, contrasena)


#Ventana elección
ventanaEleccion= Tk()
ventanaEleccion.title("")
ventanaEleccion.withdraw()
elegirPeli= Button(ventanaEleccion,command=funciones.Eleccion, text="Película").place(x=100, y=100)
elegirSerie= Button(ventanaEleccion,command=funciones.Eleccion, text="Serie").place(x=40, y=100)

#Ventana de juego
ventanaJuego= Tk()
ventanaJuego.title("")
ventanaJuego.withdraw()

lista_ventanas = [ventanaSesion, ventanaEleccion, ventanaJuego]

#Botones de sesión
iniciarSesion= Button(mainFrame, command= partial(funciones.AparecerVP, lista_ventanas), text="Iniciar sesión")
iniciarSesion.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)
registrarUsuario= Button(mainFrame, command= usuario_contrasena, text="Registrar")
registrarUsuario.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)       


ventanaSesion.mainloop()