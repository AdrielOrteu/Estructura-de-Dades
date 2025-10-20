from Reserva import Reserva
import copy
from datetime import datetime, timedelta


class ReservesHotel:
    
    def __init__(self, resNom="", preu=0.0, nHab=0):
        if type(resNom) == str:
            self._resNom = resNom
        else:
            raise TypeError("resNom must be str")
        
        if type(preu) == float:
            self._preu = preu
        else:
            raise TypeError("preu must be float")
        
        if type(nHab) == int:
            if nHab >= 0:
                self._nHab = nHab
            else:
                raise ValueError("nHab must be positive")
        else:
            raise TypeError("nHab must be int")
        self._reserves: list = []
    
    def llegeixReserves(self, nomFitxer):
        
        if nomFitxer == "reserves2.txt":
            print("### reserves2.txt ###")
            with open(nomFitxer, "r") as r2:
                for line in r2:
                    print(line)
            print("#######")
        
        print("llegeixReserves()")
        with open(nomFitxer, "r") as reserves:
            for reserva in reserves:
                reserva = reserva.split()
                self.afegeixReserva(nomClient=reserva[0],
                                    dataEntrada=datetime(int(reserva[3]), int(reserva[2]), int(reserva[1])),
                                    nHabitacions=int(reserva[4]),
                                    nDies=int(reserva[5]))
        
        for reserva in self._reserves:
            print(reserva)
    
    def reservesDia(self, data: datetime):
        print("reservesDia()")
        r = []
        for reserva in self._reserves:
            if reserva.dataSortida > data >= reserva.dataEntrada:
                r.append(reserva)
        for _r in r:
            print(_r)
        return r
    
    def nReservesDia(self, data: datetime):
        print("nReservesDia()")
        r_dia = self.reservesDia(data)
        return sum([r.nHabitacions for r in r_dia])
    
    def afegeixReserva(self, nomClient, dataEntrada, nDies, nHabitacions):
        print("afegeixReserva()")
        tmp_r = Reserva(nomClient=nomClient,
                        dataEntrada=dataEntrada,
                        dataSortida=dataEntrada + timedelta(nDies),
                        nHabitacions=nHabitacions,
                        preu=self._preu * nHabitacions * nDies)
        print(tmp_r)
        for i in range(nDies):
            r_dia = self.reservesDia(dataEntrada + timedelta(i))
            for reserva in r_dia:
                print(reserva)
            if self._nHab <= nHabitacions + sum([r.nHabitacions for r in r_dia]) or tmp_r in r_dia:
                return False
        
        self._reserves.append(tmp_r)
        # date = dataEntrada
        # n = 0
        # while self._nHab - self.nReservesDia(date) >= nHabitacions and n < nDies:
        #    date = date + timedelta(1)
        #    n += 1
        # if n == nDies:
        #    self._reserves.append(Reserva(nomClient=nomClient,
        #                                  dataEntrada=dataEntrada,
        #                                  dataSortida=date,
        #                                  nHabitacions=nHabitacions,
        #                                  preu=(
        #                                              self._preu * nHabitacions * nDies)))  # TODO Check if I add the right amounts to n and date with the while loop
    
    def consultaReserva(self, nomClient, dataEntrada):
        for reserva in self._reserves:
            if reserva.dataEntrada == dataEntrada and reserva.nomClient == nomClient:
                return True, reserva.dataSortida, reserva.nHabitacions, reserva.preu
        return False, None, None, None
    
    def __str__(self):
        return self._reserves.__str__()