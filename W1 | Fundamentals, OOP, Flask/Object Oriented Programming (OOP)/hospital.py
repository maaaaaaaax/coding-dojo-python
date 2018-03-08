class Patient(object):
    def __init__(self, id_number, name, allergies):
        self.id_number = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = 0

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.next_bed_number = 1
    # add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.
    def admit(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            patient.bed_number = self.next_bed_number
            self.next_bed_number += 1
            print "{} has been successfully admitted.".format(patient.name)
            return self
        else:
            print "I'm sorry, this hospital is full and can't accept new patients."

    # look up and remove a patient from the list of patients. Change bed number for that patient back to none.
    def discharge(self, patient_name):
        for patient in self.patients:
            if patient.name == patient_name:
                self.patients.remove(patient)
                print "{} successfully discharged.".format(patient.name)
                return self
        else:
            print "Ummm... who do you know here?"


patient1 = Patient(000, "Max", "cats and dust")
patient2 = Patient(001, "Caesar", "Brutus")
patient3 = Patient(002, "Harry Potter", "dementors")

# print patient1.name, patient1.allergies
# output is Max cats and dust

hospital1 = Hospital("Hogwarts",2)

# print hospital1.name
# output is Hogwarts

hospital1.admit(patient1)
# output is Max has been successfully admitted.
hospital1.admit(patient2)
# output is Caesar has been successfully admitted.
hospital1.discharge("Caesar")
# output is Caesar successfully discharged.
hospital1.discharge("Ron")
# output is Ummm... who do you know here?
