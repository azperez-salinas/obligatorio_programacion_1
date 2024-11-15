from .aventurero import Aventurero

class Ranger(Aventurero):
    def __init__(self, nombre:str, id:int, puntos_habilidad:int, dinero:float):
        super().__init__(nombre, id, puntos_habilidad, dinero)
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__dinero = dinero
        self.__mascota = None
        
    @property
    def mascota(self):
        return self.__mascota
    
    @mascota.setter
    def mascota(self, mascota):
        return self.__mascota    
    
    def __eq__(self, other):
        if isinstance(self, Ranger):
            return self.id == other.id