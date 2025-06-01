from Director import Director
from Personaje import Personaje
from Tienda import Tienda

class JuegoTerminal:

    ORIENTACION_COMANDOS = {
        "Norte": ("w", "Norte"),
        "Sur": ("s", "Sur"),
        "Este": ("d", "Este"),
        "Oeste": ("a", "Oeste"),
        "Noreste": ("e", "Noreste"),
        "Noroeste": ("q", "Noroeste"),
        "Sureste": ("o", "Sureste"),
        "Suroeste": ("z", "Suroeste"),
    }

    def __init__(self, ruta_json):
        self.director = Director()
        self.director.procesar(ruta_json)
        self.juego = self.director.obtenerJuego()
        self.juego.agregarPersonaje("Héroe")
        self.personaje = self.juego.person

    def mostrar_comandos(self):
        print("\nAcciones disponibles:")
        self.comando_accion = {}
        orientaciones = self.personaje.posicion.obtenerOrientaciones()
        for orientacion in orientaciones:
            nombre = str(orientacion)
            elem = self.personaje.posicion.obtenerElementoOr(orientacion)
            if hasattr(elem, "esPuerta") and elem.esPuerta():
                es_con_llave = hasattr(elem, "esPuertaConLlave") and elem.esPuertaConLlave()
                tipo_puerta = "Puerta con llave" if es_con_llave else "Puerta"
                if elem.estaAbierta():
                    print(f"  ir_{nombre.lower()} - Ir al {nombre} ({tipo_puerta} abierta)")
                    self.comando_accion[f"ir_{nombre.lower()}"] = ("mover", orientacion)
                    print(f"  cerrar_{nombre.lower()} - Cerrar {tipo_puerta} al {nombre}")
                    self.comando_accion[f"cerrar_{nombre.lower()}"] = ("cerrar_puerta", orientacion)
                else:
                    print(f"  abrir_{nombre.lower()} - Abrir {tipo_puerta} al {nombre}")
                    self.comando_accion[f"abrir_{nombre.lower()}"] = ("abrir_puerta", orientacion)
            elif hasattr(elem, "esCofre") and elem.esCofre():
                print(f"  cofre_{nombre.lower()} - Interactuar con cofre al {nombre}")
                self.comando_accion[f"cofre_{nombre.lower()}"] = ("cofre", orientacion)
            elif hasattr(elem, "esTunel") and elem.esTunel():
                print(f"  tunel_{nombre.lower()} - Entrar en tunel al {nombre}")
                self.comando_accion[f"tunel_{nombre.lower()}"] = ("tunel", orientacion)
            
            elif hasattr(elem, "esPared") and elem.esPared():
                pass
            else:
                print(f"  ir_{nombre.lower()} - Ir al {nombre} ({elem})")
                self.comando_accion[f"ir_{nombre.lower()}"] = ("mover", orientacion)
        if hasattr(self.personaje.posicion, "esArmario") and self.personaje.posicion.esArmario():
            print("  salir_armario - Salir del armario")
            self.comando_accion["salir_armario"] = ("salir_armario", None)
    # Objetos en el centro de la habitación (no en orientaciones)
        objetos_centro = [obj for obj in getattr(self.personaje.posicion, "hijos", []) if hasattr(obj, "interactuar")]
        for idx, obj in enumerate(objetos_centro, 1):
            if hasattr(obj, "esTunel") and obj.esTunel():
                print(f"  tunel_centro - Entrar en túnel en el centro")
                self.comando_accion["tunel_centro"] = ("tunel_centro", obj)
            else:
                print(f"  recoger_{idx} - Recoger {obj}")
                self.comando_accion[f"recoger_{idx}"] = ("recoger_objeto", obj)
    # Acciones generales
        print("  tienda - Ver tienda (gastar monedas)")
        print("  inventario - Ver inventario")
        print("  atacar - Atacar bicho en la habitación")
        print("  abrir_todas - Abrir todas las puertas")
        print("  cerrar_todas - Cerrar todas las puertas")
        print("  salir - Salir del juego")

    def menu_cofre(self, cofre):
        while True:
            cofre.mostrar_menu()
            if not cofre.hijos:
                break
            try:
                op = int(input("¿Qué quieres hacer? (elige número): ").strip())
                if 1 <= op <= len(cofre.hijos):
                    cofre.recoger_objeto(self.personaje, op-1)
                elif op == len(cofre.hijos)+1:
                    break
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Introduce un número válido.")

    def ejecutar_comando(self, comando):
        # Comandos dinámicos de orientación y acción
        if comando in self.comando_accion:
            accion, dato = self.comando_accion[comando]
            if accion == "mover":
                metodo = f"irAl{dato}"
                if hasattr(self.personaje, metodo):
                    getattr(self.personaje, metodo)()
                else:
                    print(f"No puedes moverte al {dato.lower()}.")
            elif accion == "abrir_puerta":
                orientacion = dato
                elem = self.personaje.posicion.obtenerElementoOr(orientacion)
                if hasattr(elem, "abrir"):
                    if elem.esPuerta():
                        elem.abrir(self.personaje)
                    else:
                        elem.abrir()
                else:
                    print("No hay puerta que abrir en esa dirección.")
            elif accion == "salir_armario":
    # Cambia la posición del personaje a la habitación padre
                self.personaje.posicion.salir(self.personaje)
                print("Has salido del armario.")
            elif accion == "cerrar_puerta":
                orientacion = dato
                elem = self.personaje.posicion.obtenerElementoOr(orientacion)
                if hasattr(elem, "cerrar"):
                    elem.cerrar()
                else:
                    print("No hay puerta que cerrar en esa dirección.")
            elif accion == "cofre":
                orientacion = dato
                elem = self.personaje.posicion.obtenerElementoOr(orientacion)
                self.menu_cofre(elem)
            elif accion == "tunel_centro":
                obj = dato  # dato es el objeto túnel
                obj.entrar(self.personaje)
            elif accion == "recoger_objeto":
                obj = dato
                obj.interactuar(self.personaje)
            return True
        # Comandos generales
        if comando == "abrir_todas":
            self.juego.abrirPuertas()
            print("Todas las puertas han sido abiertas.")
        elif comando == "cerrar_todas":
            self.juego.cerrarPuertas()
            print("Todas las puertas han sido cerradas.")
        elif comando == "tienda":
            if not hasattr(self, 'tienda'):
                self.tienda = Tienda()
                self.tienda.personaje = self.personaje
            self.tienda.menu_tienda()
        elif comando == "inventario":
            self.personaje.mochila.mostrar()
        elif comando == "atacar":
            self.juego.buscarBicho()
        elif comando == "salir":
            print("Saliendo del juego...")
            return False
        else:
            print("Comando no reconocido. Intenta nuevamente.")
        return True

    def iniciar(self):
        print("¡Bienvenido al Juego del Laberinto!")
        self.personaje.mostrar_estado()
        cont = 0
        while True:
            self.mostrar_comandos()
            comando = input("\nIngresa un comando: ").strip().lower()
            if not self.ejecutar_comando(comando):
                break
            self.personaje.mostrar_estado()
            if cont == 0:
               self.juego.lanzarBichos()
               cont += 1

if __name__ == "__main__":
    # Ruta al archivo JSON
    ruta_json = "C:\\Users\\alexr\\Desktop\\UCLM\\Ano_3\\Cuatrimestre 2\\Diseño software\\laberintos\\labPruebaCofreMonLlave.json"
    # Iniciar el juego en el terminal
    juego_terminal = JuegoTerminal(ruta_json)
    juego_terminal.iniciar()