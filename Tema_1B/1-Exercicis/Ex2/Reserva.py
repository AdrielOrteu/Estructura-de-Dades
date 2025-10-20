from datetime import datetime


class Reserva:
    
    def __init__(self, nomClient, dataEntrada, dataSortida, nHabitacions, preu):
        self.nomClient = nomClient
        self.dataEntrada = dataEntrada
        self.dataSortida = dataSortida
        self.nHabitacions = nHabitacions
        self.preu = preu
    
    @property
    def nomClient(self):
        return self._nomClient
    
    @nomClient.setter
    def nomClient(self, nom):
        if isinstance(nom, str):
            self._nomClient: str = nom
        else:
            raise TypeError("nom must be str")
    
    @property
    def dataEntrada(self):
        return self._dataEntrada
    
    @dataEntrada.setter
    def dataEntrada(self, data):
        if isinstance(data, datetime):
            self._dataEntrada: datetime = data
        else:
            raise TypeError("dataEntrada must be datetime")
    
    @property
    def dataSortida(self):
        return self._dataSortida
    
    @dataSortida.setter
    def dataSortida(self, data):
        if isinstance(data, datetime):
            self._dataSortida: datetime = data
        else:
            raise TypeError("dataSortida must be datetime")
    
    @property
    def nHabitacions(self):
        return self._nHabitacions
    
    @nHabitacions.setter
    def nHabitacions(self, nHab):
        if isinstance(nHab, int):
            self._nHabitacions: int = nHab
        else:
            raise TypeError("nHabitacions must be int")
    
    @property
    def preu(self):
        return self._preu
    
    @preu.setter
    def preu(self, p):
        if isinstance(p, float):
            self._preu: float = p
        else:
            raise TypeError("preu must be float")
    
    def __eq__(self, other):
        if isinstance(other, Reserva):
            return self.nomClient == other.nomClient and self.nHabitacions == other.nHabitacions and self.dataEntrada == other.dataEntrada and self.dataSortida == other.dataSortida
        return False
    
    def __str__(self):
        return f"{self.nomClient} {self.dataEntrada} {self.dataSortida} {self.nHabitacions} {self.preu}"
