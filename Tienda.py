class Tienda:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

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
                    self.personaje.mochila.gastarMonedas(5)
                    print("¡Vida aumentada en 10!")
                else:
                    print("No tienes suficientes monedas.")
            elif op == "2":
                if monedas >= 10:
                    self.personaje.poder = getattr(self.personaje, "poder", 1) + 1
                    self.personaje.mochila.gastarMonedas(10)
                    print("¡Poder aumentado en 1!")
                else:
                    print("No tienes suficientes monedas.")
            elif op == "3":
                break
            else:
                print("Opción no válida.")