class DatosInvalidos(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        
'''
Para todos los métodos que requieran la introducción de datos por parte del usuario, es
obligatorio validar que los datos ingresados sean correctos y estén dentro de los rangos
establecidos (por ejemplo, puntos de habilidad entre 1 y 100, rangos de misiones entre 1 y
5). Si los datos son incorrectos, se debe notificar al usuario y volver al menú principal.
'''