from entities.aventurero           import Aventurero
from entities.guerrero             import Guerrero
from entities.mago                 import Mago
from entities.ranger               import Ranger
from entities.mascota              import Mascota
from entities.mision               import Mision
from entities.grupal               import Grupal
from entities.individual           import Individual
from exceptions.datosInvalidos     import DatosInvalidos 
from exceptions.entidadYaExiste    import EntidadYaExiste 
from exceptions.entidadNoExiste    import EntidadNoExiste
from exceptions.misionYaCompletada import MisionYaCompletada

class Gremio():
    def __init__(self):
        self.aventureros_registrados = []
        self.misiones_creadas = []
        self.aventureros_con_habilidad = []
    
    def registrar_aventurero(self, nombre:str, id:int, puntos_habilidad:int, dinero:float, clase:str):
        if not (nombre or id or puntos_habilidad or dinero or clase):
            raise DatosInvalidos('[ERROR]: Los datos ingresados son inválidos.')
        if puntos_habilidad < 0 or puntos_habilidad > 100 or dinero < 0:
            raise DatosInvalidos('[ERROR]: Los datos ingresados son inválidos.')
               
        clase = clase.lower()
        match clase:
            case 'mago':
                mana = int(input('Ingrese por favor su mana (1-1000): '))
                if mana < 1 or mana > 1000:
                    raise DatosInvalidos('[ERROR]: Los datos ingresados son inválidos.')

                nuevo_aventurero = Mago(nombre, id, puntos_habilidad, dinero, mana)   
            case 'guerrero':
                fuerza = int(input('Ingrese por favor su fuerza (1-100): '))
                if fuerza < 1 or fuerza > 100:
                    raise DatosInvalidos('[ERROR]: Los datos ingresados son inválidos.')

                nuevo_aventurero = Guerrero(nombre, id, puntos_habilidad, dinero, fuerza)
                
            case 'ranger':
                mascota_bool = input('¿Quieres tener mascota? (S/N) ').upper()
                mascota_bool = True if mascota_bool == 'S' else False
                
                nuevo_aventurero = Ranger(nombre, id, puntos_habilidad, dinero)
                if mascota_bool:
                    nombre_mascota = input('Ingrese por favor el nombre de la mascota: ')
                    puntos_habilidad_mascota = int(input(f'Ingrese los puntos de habilidad de {nombre_mascota}: '))
                    if not (puntos_habilidad_mascota or nombre_mascota):
                        raise DatosInvalidos('[ERROR]: Los datos ingresados son inválidos.')
                    if puntos_habilidad_mascota < 1 or puntos_habilidad_mascota > 50:
                        raise DatosInvalidos('[ERROR]: Los datos ingresados son inválidos.')
                    mascota = Mascota(nombre_mascota, puntos_habilidad_mascota)
            case _:
                raise DatosInvalidos('[ERROR]: No existe otro tipo de aventurero.')
        
        #VERIFICA SI EL AVENTURERO YA EXISTE
        for aventurero in self.aventureros_registrados:
            if aventurero.id == nuevo_aventurero.id:
                raise EntidadYaExiste('[ERROR]: La entidad Aventurero ya existe.')
        
        self.aventureros_registrados.append(nuevo_aventurero)
        if clase == 'ranger' and mascota_bool:
            nuevo_aventurero.mascota = mascota

        #MENSAJE DE OK/NOK DE LA CREACION
        if nuevo_aventurero in self.aventureros_registrados:
            print('Aventurero creado y asociado al gremio exitosamente')
        else:
            print('No se ha creado y asociado el aventurero al gremio')
            
    def registrar_mision(self, nombre:str, rango:int, recompensa:float, completado:bool, tipo:str):
        if not(nombre or rango or recompensa):
            raise DatosInvalidos('[ERROR]: Los datos ingresados son inválidos.')
        if rango < 1 or rango > 5:
            raise DatosInvalidos('[ERROR]: Los datos ingresados son inválidos.')
        
        tipo = tipo.lower()
        match tipo:
            case 'individual':
                nueva_mision = Individual(nombre, rango, recompensa, completado)
            
            case 'grupal':
                cantidad_minima = int(input('Ingrese, por favor, la cantidad minima de jugadores para realizar la mision: '))
                nueva_mision = Grupal(nombre, rango, recompensa, completado, cantidad_minima)
                
            case _:
                raise DatosInvalidos('[ERROR]: No existe otro tipo de mision.')
        
        #VERIFICA SI LA MISION YA EXISTE
        for mision in self.misiones_creadas:
            if mision.nombre == nueva_mision.nombre:
                raise EntidadYaExiste('[ERROR]: La entidad Mision ya existe.')
        
        self.misiones_creadas.append(nueva_mision)
        
        #MENSAJE DE OK/NOK DE LA CREACION
        if nueva_mision in self.misiones_creadas:
            print('Mision creada y asociada al gremio exitosamente')
        else:
            print('No se ha creado y asociado la mision al gremio')
        
    def realizar_mision(self, lista_ids, nombre_mision):
        if not(lista_ids or nombre_mision):
            raise DatosInvalidos('[ERROR] Los datos ingresados son inválidos.')
        
        #OBTENER OBJETO MISION
        for m in self.misiones_creadas:
            if m.nombre == nombre_mision:
                mision = m
                
        if not isinstance(mision, Mision):
            raise EntidadNoExiste('[ERROR]: La mision no existe.')
        
        if mision.completado == True:
            raise MisionYaCompletada('[ERROR] Mision ya completada.')
        
        if isinstance(mision, Individual) and len(lista_ids) > 1:
            raise Exception('[ERROR] Un grupo de aventureros no puede realizar misiones individuales.')
        
        if isinstance(mision, Grupal) and len(lista_ids) == 1 :
            raise Exception('[ERROR] Un aventurero no puede realizar misiones grupales.')
        
        aventureros = []
        id_encontrados = []
        for id in lista_ids:
            for aventurero in self.aventureros_registrados:
                if id == aventurero.id:
                    aventureros.append(aventurero)
                    id_encontrados.append(id)
        
        if len(id_encontrados) != len(lista_ids):
            raise EntidadNoExiste('[ERROR] Alguno/s de los identificadores ingresados no existe.')
        
        if isinstance(mision, Grupal):
            if len(aventureros) < mision.cantidad_minima_miembros:
                raise Exception('[ERROR] Cantidad insuficiente de aventureros para realizar la mision.')
        
        habilidad_total_aventureros = []
        #UTILIZADO EN OTRAS CONSULTAS
        self.aventureros_con_habilidad = []
        for aventurero in aventureros:
            if isinstance(aventurero, Ranger):
                habilidad_aventurero = aventurero.puntos_habilidad
                if aventurero.puntos_habilidad <= 80 and aventurero.mascota:
                    habilidad_aventurero += aventurero.mascota.puntos_habilidad

            if isinstance(aventurero, Mago):
                habilidad_aventurero = (aventurero.mana / 10) + aventurero.puntos_habilidad

            if isinstance(aventurero, Guerrero):
                habilidad_aventurero = (aventurero.fuerza / 2) + aventurero.puntos_habilidad
    
            habilidad_total_aventureros.append(habilidad_aventurero)
            self.aventureros_con_habilidad.append((aventurero, habilidad_aventurero))    
        
        rangos_aventureros_total = []
        for habilidad in habilidad_total_aventureros:
            match habilidad:
                case _ if 1 <= habilidad <= 20:
                    rango_aventurero = 1
                case _ if 21 <= habilidad <= 40:
                    rango_aventurero = 2
                case _ if 41 <= habilidad <= 60:
                    rango_aventurero = 3
                case _ if 61 <= habilidad <= 80:
                    rango_aventurero = 4
                case _ if habilidad > 80:
                    rango_aventurero = 5
            rangos_aventureros_total.append(rango_aventurero)
        
        for rango in rangos_aventureros_total:
            if rango < mision.rango:
                raise Exception('[ERROR]: Rango insuficiente.')
            
        mision.completado = True
        if mision not in self.misiones_creadas or mision.completado != True:
                raise Exception('Hubo un error, no se ha realizado la mision')
        
        print('Mision realizada exitosamente!')
        
        recompensa_total = mision.recompensa / len(aventureros)
        
        for aventurero in aventureros:
            match mision.rango:
                case 1:
                    aventurero.actualizar_puntos_habilidad(5) 
                case 2:
                    aventurero.actualizar_puntos_habilidad(10) 
                case 3:
                    aventurero.actualizar_puntos_habilidad(20) 
                case 4:
                    aventurero.actualizar_puntos_habilidad(50) 
                case 5:
                    aventurero.actualizar_puntos_habilidad(100) 
            
            aventurero.actualizar_dinero(recompensa_total)
            aventurero.actualizar_misiones()

    def top_10_aventureros_misiones(self):                                                               
        top_aventureros = sorted(self.aventureros_registrados,key=lambda a: (-a.misiones_completadas, a.nombre))                                                           
        return top_aventureros[:10]
    
    def top_5_misiones(self):
        top_misiones = sorted(self.misiones_creadas,key=lambda m: (-m.recompensa, m.nombre))                                                        
        return top_misiones[:5]
    
    def top_10_aventureros_habilidad(self):
        aventureros_ordenados = sorted(self.aventureros_con_habilidad,key=lambda x: (-x[1], x[0].nombre))
        return aventureros_ordenados
     
    

            