#UNIVERSIDAD ESTATAL AMAZÓNICA 
#TAREA SEMANA 7
#NOMBRE PAMELA MORALES 

class SesionUsuario:
    def __init__(self, nombre_usuario):
        # Constructor: inicializa el nombre de usuario
        self.nombre_usuario = nombre_usuario
        self.sesion_activa = False
        print(f"Sesión de usuario '{self.nombre_usuario}' iniciada.")

    def iniciar_sesion(self):
        # Método para iniciar sesión
        self.sesion_activa = True
        print(f"Bienvenido, {self.nombre_usuario}!")

    def __del__(self):
        # Destructor: cierra la sesión cuando ya no es necesario
        if self.sesion_activa:
            print(f"Sesión de {self.nombre_usuario} cerrada.")
            self.sesion_activa = False
        else:
            print(f"Sesión de {self.nombre_usuario} no estaba activa.")

# Ejemplo de uso
usuario = SesionUsuario("Pamela")
usuario.iniciar_sesion()
del usuario  # Destructor se llama automáticamente