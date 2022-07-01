

def iniciarJuego():
    print("HOLA")
    pass

def ventanaP(lista_ventanas):
    #Ventana principal
    ventanaSesion = lista_ventanas[0]
    ventanaPrincipal = lista_ventanas[1]
    ventanaSesion.withdraw()
    ventanaPrincipal.deiconify()
    ventanaPrincipal.title("")
    #Boton