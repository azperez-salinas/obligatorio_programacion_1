from abc import ABC

class Aventurero(ABC):
    def __init__(self, nombre:str, id:int, puntos_habilidad:int, dinero:float):
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__dinero = dinero
    
    @property
    def id(self):
        return self.__id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad

    def actualizar_puntos_habilidad(self, puntos_obtenidos:int):
        self.__puntos_habilidad = self.__puntos_habilidad + puntos_obtenidos
    
    #Revisar letra con respecto a dinero, FUERZA y MANA, evaluar getter y setter 
    