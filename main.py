from gremio                         import Gremio
from .utils.clean_console           import clear
from .exceptions.datosInvalidos     import DatosInvalidos 
from .exceptions.entidadYaExiste    import EntidadYaExiste 
from .exceptions.entidadNoExiste    import EntidadNoExiste
from .exceptions.misionYaCompletada import MisionYaCompletada

gremio_1 = Gremio()

def otras_consultas():
        aux=False
        while aux ==False:
            print("  1. Ver Top 10 Aventureros con Más Misiones Resueltas:") 
            print("  2. Ver top 10 Aventureros por mayor habilidad:")
            print("  3. Ver Top 5 Misiones con Mayor Recompensa:")
            print("  4. Volver al Menú Principal")
            print()
            numero_ingresado=int(input())
            match numero_ingresado:
                case 1:
                    clear()
                    print("Top 10 Aventureros con Más Misiones Resueltas:")
                    for i, aventurero in enumerate(gremio_1.top_10_aventureros_misiones(), start=1): 
                        print(f"{i+1}. {gremio_1.aventurero.nombre} - Misiones Resueltas: {gremio_1.aventurero.misiones_resueltas}")
                        
                case 2:
                    clear()
                    print("Top 5 Misiones con Mayor Recompensa:")
                    for i, mision in enumerate(gremio_1.top_5_misiones(), start=1):
                        print(f"{i+1}. {mision.nombre} - Recompensa: {mision.recompensa}")
                        
                case 3:
                    clear()
                    print("Top 10 Aventureros con Mayor Habilidad Total:")
                    top_aventureros = gremio_1.top_10_aventureros_habilidad()
                    for i, (aventurero, habilidad_total) in enumerate(top_aventureros, start=1):
                        print(f"{i}. {aventurero.nombre} - Habilidad Total: {habilidad_total}")
                        
                case 4:
                    aux=True
                case _:
                    print("El número seleccionado no esta dentro de las opciones del menú.\nVuelva a intentarlo")
                    
def menu_principal():
    exit = False

    while exit == False:
        print("Bienvenido al Simulador de Gremio de Aventureros")
        print("Seleccione una opción:")
        print("   1. Registrar Aventurero")
        print("   2. Registrar Misión")
        print("   3. Realizar Misión")
        print("   4. Otras Consultas")
        print("   5. Salir")
        print()
        seleccion_menu = int(input())

        match seleccion_menu:
            case 1:
                try:
                    clear()
                    nombre = input('Por favor, ingrese el nombre: ')
                    id = input('Ingrese el id: ')
                    puntos_habilidad = input('Ingrese los puntos de habilidad: ')
                    dinero = input('Ingrese el dinero: ')
                    clase = input('Ingrese la clase de aventurero que quiere crear (mago, guerrero, ranger): ')
                    gremio_1.registrar_aventurero(nombre, id, puntos_habilidad, dinero, clase)
                except DatosInvalidos as e:
                    print(e)                      
                except EntidadYaExiste as e:
                    print(e)
                except Exception as e:
                    print(e)
            case 2:
                try: 
                    nombre = input('Por favor, ingrese el nombre: ')
                    rango = input('Ingrese el rango: ')
                    recompensa = input('Ingrese la recompensa (con decimales): ')
                    completado = False
                    tipo = input('Ingrese el tipo de mision que quiere crear (individual, grupal): ')
                    gremio_1.registrar_mision(nombre, rango, recompensa, completado, tipo)
                except DatosInvalidos as e:
                    print(e)                      
                except EntidadYaExiste as e:
                    print(e)
                except Exception as e:
                    print(e)
                    
            case 3:
                try:
                    lista_ids = []
                    auxiliar_cant_ids = 'S'
                    while auxiliar_cant_ids == 'S':
                        id = input('Ingrese el id del aventurero: ')
                        lista_ids.append(id)
                        auxiliar_cant_ids = input('Desea ingresar otro aventuero? (S/N)').upper()
                    nombre_mision = input('Ingrese el nombre de la mision que desea realizar: ')
                    gremio_1.realizar_mision(lista_ids, nombre_mision)
                except DatosInvalidos as e:
                    print(e)                      
                except EntidadNoExiste as e:
                    print(e)
                except MisionYaCompletada as e:
                    print(e)
                except Exception as e:
                    print(e)
            case 4:
                otras_consultas()
            case 5:
                print("Hasta pronto!")
                exit = True
            case _:
                print("El número seleccionado no esta dentro de las opciones del menú.\nVuelva a intentarlo")

