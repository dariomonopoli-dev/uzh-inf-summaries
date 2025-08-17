class Dog:
    def __init__(self):
        pass
    @staticmethod
    def print_you():
        return 'hello world'


print(Dog.print_you())


class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []

    def find_doctor(self, sickness):
        for doctor in self.doctors:
            if sickness in doctor.can_heal:
                return doctor
        return None

    def treat(self,patient):
        print(patient)
        still_sick = []
        for sickness in patient.sicknesses:
            print(sickness)
            if not self.find_doctor(sickness):
                still_sick.append(sickness)
        patient.sicknesses = still_sick
        return patient
            


class Doctor:
    def __init__(self, can_heal):
        self.can_heal = can_heal

class Patient:
    def __init__(self, sicknesses):
        self.sicknesses = sicknesses

    def __str__(self):
        return str(self.sicknesses)


h = Hospital('Triemli')
d1 = Doctor(['Huten', 'Rote Augen'])
d2 = Doctor(['Durchfall', 'Kopfweh'])
h.doctors.append(d1)
h.doctors.append(d2)
p1 = Patient(['Husten','Kopweh','Krebs'])
p1 = h.treat(p1)

s1 = 'j onumnpn mpuu8U9U9MQ U'

def recursive_upper(s):
    if s=='':
        return s
    first=s[0]
    return first.upper() + recursive_upper(s[1:])

res = recursive_upper(s1)
print(res)

