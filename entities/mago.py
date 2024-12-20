from .aventurero import Aventurero

class Mago(Aventurero):
    def __init__(self, nombre:str, id:int, puntos_habilidad:int, dinero:float, mana:int):
        super().__init__(nombre, id, puntos_habilidad, dinero)
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__dinero = dinero
        self.__mana = mana
    
    @property
    def mana(self):
        return self.__mana
    
    def __eq__(self, other):
        if isinstance(self, Mago):
            return self.id == other.id