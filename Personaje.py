from Cabeza import Cabeza
from Ente import Ente
from InventarioMochila import InventarioMochila
from Manos import Manos
from Piernas import Piernas
from Pies import Pies
from Tronco import Tronco
from Cabeza import Cabeza

class Personaje(Ente):

    def __init__(self,unaCadena):
        super().__init__()
        self.vidas = 1000
        self.poder = 1
        self.nombre = unaCadena
        self.mochila = InventarioMochila()
        self.cabeza = Cabeza()
        self.tronco = Tronco()
        self.piernas = Piernas()
        self.pies = Pies()
        self.mano = Manos()

    def mostrar_estado(self):
        print(f"\nEstado del personaje:")
        print(f"Nombre: {self.nombre}")
        print(f"Vidas: {self.vidas}")
        print(f"Ataque: {self.ataque_total()}")
        print(f"Defensa: {self.defensa_total()}")
        if hasattr(self.posicion, 'num'):
            print(f"Posición actual: Habitación {self.posicion.num}")
        else:
            print(f"Posición actual: {self.posicion}")

    def recoger(self, objeto):
        # Si es arma o armadura, pregunta si quiere equipar o guardar en mochila
        if objeto.esArma() or objeto.esArmadura():
            self.equipar(objeto)
        else:
            self.mochila.agregar(objeto)

    def equipar(self, objeto):
        objeto.equipando(self)
        print(f"Has equipado {objeto}")

    def comprar(self,cantidad):
        if self.mochila.contarMonedas() >= cantidad:
            self.mochila.gastarMonedas(cantidad)
            print(f"Has comprado un objeto por {cantidad} monedas.")
        else:
            print("No tienes suficientes monedas para comprar.")

    def defensa_total(self):
        return(
            self.cabeza.bonificacion_defensa() +
            self.tronco.bonificacion_defensa() +
            self.piernas.bonificacion_defensa() +
            self.pies.bonificacion_defensa()
        )

    def ataque_total(self):
        return (
            self.mano.bonificacion_ataque() + self.poder
        )

    def esAtacadoPor(self, alguien):
        print(f"{self} es atacado por {alguien}")
        self.vidas = self.vidas - max(0, alguien.poder - self.defensa_total())
        print(f"Vidas: {self.vidas}")
        if self.vidas <= 0:
            self.heMuerto()

    def puedeAtacar(self):
        self.juego.buscarBicho()

    def irAlEste(self):
        self.posicion.irAlEste(self)

    def irAlNorte(self):
        self.posicion.irAlNorte(self)

    def irAlOeste(self):
        self.posicion.irAlOeste(self)
    
    def irAlSur(self):
        self.posicion.irAlSur(self)

    def irAlNoroeste(self):
        self.posicion.irAlNoroeste(self)

    def irAlNoreste(self):
        self.posicion.irAlNoreste(self)

    def irAlSuroeste(self):
        self.posicion.irAlSuroeste(self)
    
    def irAlSureste(self):
        self.posicion.irAlSureste(self)

    def avisar(self):
        self.juego.muerePersonaje()

    def crearNuevoLaberinto(self,unTunel):
        unTunel.crearNuevoLaberinto(self)

    def obtenerComandos(self):
        lista = []
        self.posicion.recorrer(lambda each: lista.extend(each.obtenerComandos()))
        return lista

    def esPersonaje(self):
        return True

    def esBicho(self):
        return False

    def __str__(self):
        return f"Personaje {self.nombre}"