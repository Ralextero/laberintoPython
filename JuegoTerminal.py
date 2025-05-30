from Director import Director

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

    def mostrar_estado(self):
        print(f"\nEstado del personaje:")
        print(f"Nombre: {self.personaje.nombre}")
        print(f"Vidas: {self.personaje.vidas}")
        print(f"Poder: {getattr(self.personaje, 'poder', 1)}")
        print(f"Posición actual: Habitación {self.personaje.posicion.num}")

    def mostrar_comandos(self):
        print("\nAcciones disponibles:")
        self.comando_accion = {}
        orientaciones = self.personaje.posicion.obtenerOrientaciones()
        for orientacion in orientaciones:
            nombre = str(orientacion)
            elem = self.personaje.posicion.obtenerElementoOr(orientacion)
            if hasattr(elem, "esPuerta") and elem.esPuerta():
                estado = "abierta" if elem.estaAbierta() else "cerrada"
                print(f"  ir_{nombre.lower()} - Ir al {nombre} (Puerta {estado})")
                self.comando_accion[f"ir_{nombre.lower()}"] = ("mover", orientacion)
                print(f"  abrir_{nombre.lower()} - Abrir puerta al {nombre}")
                self.comando_accion[f"abrir_{nombre.lower()}"] = ("abrir_puerta", orientacion)
                print(f"  cerrar_{nombre.lower()} - Cerrar puerta al {nombre}")
                self.comando_accion[f"cerrar_{nombre.lower()}"] = ("cerrar_puerta", orientacion)
            elif hasattr(elem, "esPared") and elem.esPared():
                print(f"  ir_{nombre.lower()} - Ir al {nombre} (Pared)")
                self.comando_accion[f"ir_{nombre.lower()}"] = ("mover", orientacion)
            elif elem.__class__.__name__ == "Cofre":
                print(f"  ir_{nombre.lower()} - Ir al {nombre} (Cofre)")
                self.comando_accion[f"ir_{nombre.lower()}"] = ("mover", orientacion)
                print(f"  cofre_{nombre.lower()} - Interactuar con cofre al {nombre}")
                self.comando_accion[f"cofre_{nombre.lower()}"] = ("cofre", orientacion)
            elif hasattr(elem, "esTunel") and elem.esTunel():
                print(f"  tunel_{nombre.lower()} - Entrar en tunel al {nombre}")
                self.comando_accion[f"tunel_{nombre.lower()}"] = ("tunel", orientacion)
            else:
                print(f"  ir_{nombre.lower()} - Ir al {nombre} ({elem})")
                self.comando_accion[f"ir_{nombre.lower()}"] = ("mover", orientacion)
        # Objetos en el centro de la habitación (no en orientaciones)
        objetos_centro = [obj for obj in getattr(self.personaje.posicion, "hijos", []) if hasattr(obj, "interactuar")]
        for idx, obj in enumerate(objetos_centro, 1):
            print(f"  recoger_{idx} - Recoger {obj}")
            self.comando_accion[f"recoger_{idx}"] = ("recoger_objeto", obj)
        # Acciones generales
        print("  tienda - Ver tienda (gastar monedas)")
        print("  inventario - Ver inventario")
        print("  atacar - Atacar bicho en la habitación")
        print("  abrir_todas - Abrir todas las puertas")
        print("  cerrar_todas - Cerrar todas las puertas")
        print("  salir - Salir del juego")

    def menu_tienda(self):
        while True:
            monedas = self.personaje.mochila.contarMonedas()
            print("\n--- Tienda ---")
            print(f"Tienes {monedas} monedas.")
            print("1. Aumentar vida (+10) - 5 monedas")
            print("2. Aumentar poder (+1) - 10 monedas")
            print("3. Salir")
            op = input("Elige una opción: ").strip()
            if op == "1":
                if monedas >= 5:
                    self.personaje.vidas += 10
                    self._gastar_monedas(5)
                    print("¡Vida aumentada en 10!")
                else:
                    print("No tienes suficientes monedas.")
            elif op == "2":
                if monedas >= 10:
                    self.personaje.poder = getattr(self.personaje, "poder", 1) + 1
                    self._gastar_monedas(10)
                    print("¡Poder aumentado en 1!")
                else:
                    print("No tienes suficientes monedas.")
            elif op == "3":
                break
            else:
                print("Opción no válida.")

    def _gastar_monedas(self, cantidad):
        gastadas = 0
        nuevos_objetos = []
        for obj in self.personaje.mochila.objetos:
            if hasattr(obj, "esMoneda") and obj.esMoneda() and gastadas < cantidad:
                gastadas += 1
                continue
            nuevos_objetos.append(obj)
        self.personaje.mochila.objetos = nuevos_objetos

    def menu_cofre(self, cofre):
        while True:
            if not cofre.hijos:
                print("El cofre está vacío.")
                break
            print("\nEl cofre contiene:")
            for idx, obj in enumerate(cofre.hijos, 1):
                print(f"{idx}. {obj}")
            print(f"{len(cofre.hijos)+1}. Salir")
            op = input("¿Qué quieres hacer? (elige número): ").strip()
            try:
                op = int(op)
                if 1 <= op <= len(cofre.hijos):
                    self.personaje.recoger_de_cofre(cofre, op-1)
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
                    if elem.__class__.__name__ == "PuertaConLlave":
                        elem.abrir(self.personaje)
                    else:
                        elem.abrir()
                else:
                    print("No hay puerta que abrir en esa dirección.")
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
            elif accion == "tunel":
                orientacion = dato
                elem = self.personaje.posicion.obtenerElementoOr(orientacion)
                elem.entrar(self.personaje)
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
            self.menu_tienda()
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
        self.mostrar_estado()
        cont = 0
        while True:
            self.mostrar_comandos()
            comando = input("\nIngresa un comando: ").strip().lower()
            if not self.ejecutar_comando(comando):
                break
            self.mostrar_estado()
            #if cont == 0:
             #   self.juego.lanzarBichos()
              #  cont += 1

if __name__ == "__main__":
    # Ruta al archivo JSON
    ruta_json = "C:\\Users\\alexr\\Desktop\\UCLM\\Ano_3\\Cuatrimestre 2\\Diseño software\\laberintos\\labPruebaCofreMonLlave.json"
    # Iniciar el juego en el terminal
    juego_terminal = JuegoTerminal(ruta_json)
    juego_terminal.iniciar()