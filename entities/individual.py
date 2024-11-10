from mision import Mision

class Individual(Mision):
    def __init__(self, nombre:str, rango:int, recompensa:float, completado:bool):
        super().__init__(nombre, rango, recompensa, completado)
        self.__nombre = nombre
        self.__rango = rango
        self.__recompensa = recompensa
        self.__completado = completado