from .mision import Mision

class Grupal(Mision):
    def __init__(self, nombre:str, rango:int, recompensa:float, completado:bool, cantidad_minima_miembros:int):
        super().__init__(nombre, rango, recompensa, completado)
        self.__nombre = nombre
        self.__rango = rango
        self.__recompensa = recompensa
        self.__completado = completado
        self.__cantidad_minima_miembros = cantidad_minima_miembros
        
    @property
    def cantidad_minima_miembros(self):
        return self.__cantidad_minima_miembros