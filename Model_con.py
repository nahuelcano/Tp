import basedatos
from sqlalchemy import Column, Integer, String

class ModelConcurso(basedatos.Base):
    
    __tablename__ = "concurso"
    
    id = Column(Integer, primary_key=True)
    nro_participante = Column(Integer, nullable=False)
    nombre = Column(String(15), nullable=False)
    apellido = Column(String(15), nullable=False)
    edad = Column(String(2), nullable=False)
    sexo = Column(String(1), nullable=False)
    primer_disparo = Column(Integer, nullable=False)
    segundo_disparo = Column(Integer, nullable=False)
    tercer_disparo = Column(Integer, nullable=False)
    mejor_disparo = Column(Integer, nullable=True)
    promedio = Column(Integer, nullable=True)
    
    
    def __init__(self, nro_participante, nombre, apellido, edad, sexo, primer_disparo, segundo_disparo, tercer_disparo, mejor_disparo, promedio):
        #self.id = id
        self.nro_participante = nro_participante
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.primer_disparo = primer_disparo
        self.segundo_disparo = segundo_disparo
        self.tercer_disparo = tercer_disparo
        self.mejor_disparo = mejor_disparo
        self.promedio = promedio
        
    
    def __str__(self):
        return (
            f"""
            =================================
            ======                     ======
            =================================
            id: {self.id},
            Número participante: {self.nro_participante},
            Nombre: {self.nombre},
            Apellido: {self.apellido},
            Edad: {self.edad},
            sexo: {self.sexo},
            Primer disparo: {self.primer_disparo}
            Segundo disparo: {self.segundo_disparo}
            Tercer disparo: {self.tercer_disparo}
            Mejor disparo: {self.mejor_disparo}
            Promedio: {self.promedio}
            =================================
            =================================
            """
        )
        