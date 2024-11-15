from abc import ABC

class Aventurero(ABC):
    def __init__(self, nombre:str, id:int, puntos_habilidad:int, dinero:float):
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__dinero = dinero
        self.__misiones_completadas = 0
    
    @property
    def id(self):
        return self.__id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad
    
    @property
    def misiones_completadas(self):
        return self.__misiones_completadas
    
    def __eq__(self, other):
        if isinstance(self, Aventurero):
            return self.id == other.id

    def actualizar_puntos_habilidad(self, puntos_obtenidos:int):
        self.__puntos_habilidad = self.__puntos_habilidad + puntos_obtenidos
    
    def actualizar_dinero(self, recompensa_obtenida:float):
        self.__dinero = self.__dinero + recompensa_obtenida
    
    def actualizar_misiones(self):
        self.__misiones_completadas += 1
           