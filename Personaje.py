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

    def recoger(self, objeto):
        # Si es arma o armadura, pregunta si quiere equipar o guardar en mochila
        if hasattr(objeto, "esArma") and objeto.esArma():
            self.equipar(objeto)
        elif hasattr(objeto, "esArmadura") and objeto.esArmadura():
            self.equipar(objeto)
        else:
            self.mochila.agregar(objeto)

    # Ejemplo de método en Personaje.py
    def recoger_de_cofre(self, cofre, indice):
        if 0 <= indice < len(cofre.hijos):
            objeto = cofre.hijos[indice]
            self.recoger(objeto)
            cofre.eliminarHijo(objeto)
        else:
            print("No hay objeto en esa posición del cofre.")

    def equipar(self, objeto):
        # Decora la parte correspondiente
        if objeto.esArma():
            self.mano = objeto.__class__(self.mano, objeto.material)
            print(f"Has equipado {objeto}")
        elif objeto.esArmadura():
            tipo = objeto.__class__.__name__.lower()
            if tipo == "casco":
                self.cabeza = objeto.__class__(self.cabeza, objeto.material)
            elif tipo == "pechera":
                self.tronco = objeto.__class__(self.tronco, objeto.material)
            elif tipo == "pantalones":
                self.piernas = objeto.__class__(self.piernas, objeto.material)
            elif tipo == "botas":
                self.pies = objeto.__class__(self.pies, objeto.material)
            print(f"Has equipado {objeto}")

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
        self.vidas = self.vidas - max(0, self.defensa_total() - alguien.poder)
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

    def __str__(self):
        return f"Personaje {self.nombre}"