import csv
from datetime import datetime
from math import sqrt, pi, cos, log10


def grados_a_radianes(numero):
    return numero * pi / 180


class Solution:

    def __init__(self, fileName):
        # id,first_name,last_name,dateOfBirth,interests,latitude,longitude
        self.students = []
        with open(fileName) as file:
            reader = csv.reader(file, delimiter=',', skipinitialspace=True)
            i = 0
            for line in reader:
                self.students.append(line[1:])
                # Se convierten los tipos de datos correspondientes
                self.students[i][2] = datetime.strptime(
                    self.students[i][2], '%Y-%m-%d')
                self.students[i][3] = float(self.students[i][3])
                self.students[i][4] = float(self.students[i][4])
                for j in range(5, 11):
                    self.students[i][j] = bool(int(self.students[i][j]))

                i += 1

    def d(self, id1, id2):
        student_1 = self.students[id1 - 1]
        student_2 = self.students[id2 - 1]
        latitud1 = grados_a_radianes(float(student_1[3]))
        latitud2 = grados_a_radianes(float(student_2[3]))
        longitud1 = grados_a_radianes(float(student_1[4]))
        longitud2 = grados_a_radianes(float(student_2[4]))
        R = 6371.009
        diferencial_latitud = abs(latitud1 - latitud2)
        diferencial_longitud = abs(longitud1 - longitud2)
        segundo_operando = diferencial_longitud * \
            cos((latitud1 + latitud2) / 2)
        d = R * sqrt(pow(diferencial_latitud, 2) + pow(segundo_operando, 2))
        return round(d, 3)

    # Distancia entre estudiantes
    def ejercicio1(self, id1, id2):
        return self.d(id1, id2)

    # Compatibilidad entre estudiantes
    def ejercicio2(self, id1, id2):
        student_1 = self.students[id1 - 1]
        student_2 = self.students[id2 - 1]
        age_1 = student_1[2]
        age_2 = student_2[2]
        anosdif = abs(age_1 - age_2).days / 365.2425
        ageDif = 1 if(anosdif) <= 1 else (1 / (anosdif))
        cont = 5
        sum = 0
        while cont <= 10:
            if student_1[cont] == student_2[cont]:
                sum += 1
            cont += 1
        return round((1 / log10(self.d(id1, id2))) + ageDif + sum, 3)

    def distances(self, id):
        dist = []
        for x in range(len(self.students)):
            if id != x + 1:
                dist.append((self.d(id, x + 1), x + 1))
        return dist

    # Estudiantes mas cercanos
    def ejercicio3(self, id, n):
        dist = self.distances(id)
        dist.sort()
        DISTANCIA = dist[:n]
        r = []
        for x in DISTANCIA:
            r.append(x[1])
        return r

    # Estudiantes mas cercanos
    def ejercicio4(self, id, n):
        dist = self.distances(id)
        dist.sort(reverse=True)
        DISTANCIA = dist[:n]
        r = []
        for x in DISTANCIA:
            r.append(x[1])
        return r

    # Estudiantes mas compatibles
    def compatibilities(self, id):
        comp = []
        for x in range(len(self.students)):
            if id != x + 1:
                comp.append((self.ejercicio2(id, x+1), x+1))
        return comp

    def ejercicio5(self, id, n):
        comp = self.compatibilities(id)
        comp.sort(reverse=True)
        Compat = comp[:n]
        r = []
        for x in Compat:
            r.append(x[1])
        return r

    # Estudiantes menos compatibles
    def ejercicio6(self, id, n):
        comp = self.compatibilities(id)
        comp.sort()
        Compat = comp[:n]
        r = []
        for x in Compat:
            r.append(x[1])
        return r


solution = Solution("data.csv")


