import csv


class Patient:

    all_patients = []

    def __init__(self, age_of_diagnosis, age_of_death, sex, dementia, abeta42):
        self.age_of_diagnosis = age_of_diagnosis
        self.age_of_death = age_of_death
        self.sex = sex
        self.dementia = dementia
        self.abeta42 = abeta42

    def __repr__(self):
        return f"{self.age_of_diagnosis}: ({self.age_of_death} | {self.sex} | {self.dementia})"

    @classmethod
    def instantiate_from_csv(cls, filename):

        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:

                diagnosis = row["Age of Dementia diagnosis"]

                if diagnosis == "":
                    diagnosis = None
                else:
                    diagnosis = int(diagnosis)

                abeta42 = row["ABeta42 pg/ug"]

                if abeta42 == "":
                    abeta42 = None
                else:
                    abeta42 = float(abeta42)

                patient = cls(
                    diagnosis,
                    int(row["Age at Death"]),
                    row["Sex"],
                    row["Cognitive Status"] == "Dementia",
                    abeta42
                )

                cls.all_patients.append(patient)

    @classmethod
    def filter(cls, patients, sex=None, dementia=None):

        filtered_patients = []

        for patient in patients:

            if sex is not None and patient.sex != sex:
                continue

            if dementia is not None and patient.dementia != dementia:
                continue

            filtered_patients.append(patient)

        return filtered_patients