from participante import Participante
import math
import random


class Disparo(Participante):
    
    contador_disparos = 0
    
    
    def __init__(self, nombre, apellido, edad, sexo):
        Disparo.contador_disparos += 1
        super().__init__(nombre, apellido, edad, sexo)
        self.__id_disparo = Disparo.contador_disparos
        self.__disparos = []
        
        
    def get_id_disparo(self):
        return self.__id_disparo
    
    
    def get_disparos(self):
        return self.__disparos
    
    
    def set_disparos(self, disparos):
        self.__disparos = disparos
            
            
    def armar_datos(self):
        """
        Devuelve -> formatea los datos en un diccionario
        """        
        datos = {
            "idDisparo": self.__id_disparo,
            "disparos": self.__disparos,
            "nroParticipante": self._numero_participante,
            "nombre": self._nombre,
            "apellido": self._apellido,
            "edad": self._edad,
            "sexo": self._sexo
        }
        return datos
        
    
    def hacer_disparos(self):
        """
        Llena el atributo __disparos con lista con los tres disparos del participante
        """      
        for i in range(3):
            distancia = self.__distancia_disparo(random.randrange(1, 80), random.randrange(1, 80) )
            self.__disparos.append(distancia)
            #print(f"Disparo Numero {i+1} -> {distancia}")
    
    
    def __distancia_disparo(self, x, y):
        """
        Me devuelve la distancia del disparo hacia el origen
        """
        ejeX = pow(x, 2)
        ejeY = pow(y, 2)
        resultado = ejeX + ejeY
        distancia = int(math.sqrt( resultado ))
        return distancia
    
    
    def __str__(self):
        return (
            f"""
            =================================
            ====== PARTICIPANTE Nº: {self._numero_participante} ======
            =================================
            id disparo: {self.__id_disparo},
            Disparos: {self.__disparos}
            {super().__str__()}
            =================================
            =================================
            """
        )