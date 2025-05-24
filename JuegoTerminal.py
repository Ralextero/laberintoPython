from Director import Director

class JuegoTerminal:

    # Puedes definir este diccionario al principio del archivo
    ORIENTACION_COMANDOS = {
        "Norte": ("w", "Mover al norte"),
        "Sur": ("s", "Mover al sur"),
        "Este": ("d", "Mover al este"),
        "Oeste": ("a", "Mover al oeste"),
        "Noreste": ("e", "Mover al noreste"),
        "Noroeste": ("q", "Mover al noroeste"),
        "Sureste": ("o", "Mover al sureste"),
        "Suroeste": ("z", "Mover al suroeste"),
    }

    def __init__(self, ruta_json):
        self.director = Director()
        self.director.procesar(ruta_json)
        self.juego = self.director.obtenerJuego()
        self.juego.agregarPersonaje("Héroe")
        self.personaje = self.juego.person

    def mostrar_estado(self):
        """
        Muestra el estado actual del personaje y su posición.
        """
        print(f"\nEstado del personaje:")
        print(f"Nombre: {self.personaje.nombre}")
        print(f"Vidas: {self.personaje.vidas}")
        print(f"Posición actual: Habitación {self.personaje.posicion.num}")

    def mostrar_comandos(self):
        print("\nComandos disponibles:")
        orientaciones = self.personaje.posicion.obtenerOrientaciones()
    # Creamos un diccionario inverso: comando -> orientación
        comando_a_orientacion = {}
        for orientacion in orientaciones:
            nombre = str(orientacion)
            if nombre in self.ORIENTACION_COMANDOS:
                comando, descripcion = self.ORIENTACION_COMANDOS[nombre]
                print(f"  {comando} - {descripcion}")
                comando_a_orientacion[comando] = nombre
        print("  b - Abrir todas las puertas")
        print("  c - Cerrar todas las puertas")
        print("  t - Atacar")
        print("  p - Salir del juego")
    # Guarda el diccionario para usarlo en ejecutar_comando
        self.comando_a_orientacion = comando_a_orientacion

    def ejecutar_comando(self, comando):

    # Primero, verifica si el comando es de movimiento dinámico
        if hasattr(self, 'comando_a_orientacion') and comando in self.comando_a_orientacion:
            orientacion = self.comando_a_orientacion[comando]
        # Llama al método correspondiente según la orientación
            metodo = f"irAl{orientacion}"
            if hasattr(self.personaje, metodo):
                getattr(self.personaje, metodo)()
            else:
                print(f"No puedes moverte al {orientacion.lower()}.")
        elif comando == "b":
            self.juego.abrirPuertas()
            print("Todas las puertas han sido abiertas.")
        elif comando == "c":
            self.juego.cerrarPuertas()
            print("Todas las puertas han sido cerradas.")
        elif comando == "t":
            self.personaje.puedeAtacar()
        elif comando == "p":
            print("Saliendo del juego...")
            return False
        else:
            print("Comando no reconocido. Intenta nuevamente.")
        return True

    def iniciar(self):
        """
        Inicia el bucle principal del juego en el terminal.
        """
        print("¡Bienvenido al Juego del Laberinto!")
        self.mostrar_estado()
        cont=0
        while True:
            
            self.mostrar_comandos()
            comando = input("\nIngresa un comando: ").strip().lower()
            if not self.ejecutar_comando(comando):
                break
            self.mostrar_estado()
            if cont==0:
                self.juego.lanzarBichos()
                cont+=1


if __name__ == "__main__":
    # Ruta al archivo JSON
    ruta_json = "C:\\Users\\alexr\\Desktop\\UCLM\\Ano_3\\Cuatrimestre 2\\Diseño software\\laberintos\\lab4habOct.json"
    # Iniciar el juego en el terminal
    juego_terminal = JuegoTerminal(ruta_json)
    juego_terminal.iniciar()