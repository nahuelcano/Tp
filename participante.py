class Participante:
    
    contador_participantes = 0
    
    def __init__(self, nombre, apellido, edad, sexo):
        Participante.contador_participantes += 1
        self._numero_participante = Participante.contador_participantes
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._sexo = sexo
        
        
    def get_numero_participante(self):
        return self._numero_participante
        
        
    def get_nombre(self):
        return self._nombre
    
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    
    def get_apellido(self):
        return self._apellido
    
    
    def set_apellido(self, apellido):
        self._apellido = apellido
        
        
    def get_edad(self):
        return self._edad
    
    
    def set_edad(self, edad):
        self._edad = edad
        
    
    def get_sexo(self):
        return self._sexo
    
    
    def set_sexo(self, sexo):
        self._sexo = sexo
        
        
    def __str__(self):
        return (
            f"""
            Numero participante: {self._numero_participante},
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            Edad: {self._edad},
            sexo: {self._sexo}
            """
        )
