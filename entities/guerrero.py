from aventurero import Aventurero

class Guerrero(Aventurero):
    def __init__(self, nombre:str, id:int, puntos_habilidad:int, dinero:float, fuerza:int):
        super().__init__(nombre, id, puntos_habilidad, dinero)
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__dinero = dinero
        self.__fuerza = fuerza
    