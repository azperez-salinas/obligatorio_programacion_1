from exceptions.datosInvalidos      import DatosInvalidos
from exceptions.entidadYaExiste     import EntidadYaExiste
from exceptions.entidadNoExiste     import EntidadNoExiste
from exceptions.misionYaCompletada  import MisionYaCompletada
from gremio                         import Gremio

def test_gremio():
    gremio = Gremio()
    
    # Prueba de registro de aventureros
    try:
        print("\n--- Registrando Aventurero Guerrero ---")
        gremio.registrar_aventurero(nombre="Aragon", id=1, puntos_habilidad=90, dinero=100.0, clase="guerrero")
    except Exception as e:
        print(e)

    try:
        print("\n--- Registrando Aventurero Mago ---")
        gremio.registrar_aventurero(nombre="Gandalf", id=2, puntos_habilidad=80, dinero=150.0, clase="mago")
    except Exception as e:
        print(e)

    try:
        print("\n--- Registrando Aventurero Ranger ---")
        gremio.registrar_aventurero(nombre="Legolas", id=3, puntos_habilidad=85, dinero=120.0, clase="ranger")
    except Exception as e:
        print(e)

    # Prueba de registro de misiones
    try:
        print("\n--- Registrando Misión Individual ---")
        gremio.registrar_mision(nombre="Recuperar el amuleto", rango=3, recompensa=200.0, completado=False, tipo="individual")
    except Exception as e:
        print(e)
        
    try:
        print("\n--- Registrando Misión Grupal ---")
        gremio.registrar_mision(nombre="Defender el castillo", rango=4, recompensa=500.0, completado=False, tipo="grupal")
    except Exception as e:
        print(e)

    # Prueba de realizar misión
    try:
        print("\n--- Realizando Misión Individual ---")
        gremio.realizar_mision(lista_ids=[1], nombre_mision="Recuperar el amuleto")
    except Exception as e:
        print(e)
        
    try:
        print("\n--- Realizando Misión Grupal ---")
        gremio.realizar_mision(lista_ids=[1, 2, 3], nombre_mision="Defender el castillo")
    except Exception as e:
        print(e)

    # Prueba de consultas
    print("\n--- Top 10 Aventureros con Más Misiones Resueltas ---")
    for i, aventurero in enumerate(gremio.top_10_aventureros_misiones(), start=1):
        print(f"{i}. {aventurero.nombre} - Misiones Resueltas: {aventurero.misiones_completadas}")

    print("\n--- Top 10 Aventureros por Mayor Habilidad ---")
    for i, (aventurero, habilidad_total) in enumerate(gremio.top_10_aventureros_habilidad(), start=1):
        print(f"{i}. {aventurero.nombre} - Habilidad Total: {habilidad_total}")

    print("\n--- Top 5 Misiones con Mayor Recompensa ---")
    for i, mision in enumerate(gremio.top_5_misiones(), start=1):
        print(f"{i}. {mision.nombre} - Recompensa: {mision.recompensa}")

if __name__ == "__main__":
    test_gremio()