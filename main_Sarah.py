from patient_sarah import *

import matplotlib.pyplot as plt

import numpy as np

import statistics


Patient.instantiate_from_csv(
    "C:/Users/sarah/BME 2315/Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv"
)



female_dementia = []

male_dementia = []


for patient in Patient.filter(Patient.all_patients, sex="Female"):
    female_dementia.append(int(patient.dementia))


for patient in Patient.filter(Patient.all_patients, sex="Male"):
    male_dementia.append(int(patient.dementia))


x_Female_bar = statistics.mean(female_dementia) * 100

x_Male_bar = statistics.mean(male_dementia) * 100


female_stdev = statistics.stdev(female_dementia) * 100

male_stdev = statistics.stdev(male_dementia) * 100


print(f'x_Female_bar = {x_Female_bar}, female_stdev = {female_stdev}')

print(f'x_Male_bar = {x_Male_bar}, male_stdev = {male_stdev}')


sex_cols = ["Female", "Male"]

mean_sex = [x_Female_bar, x_Male_bar]

stdev_sex = [female_stdev, male_stdev]

yerr = [np.zeros(len(mean_sex)), stdev_sex]


plt.bar(
    sex_cols,
    mean_sex,
    yerr=yerr,
    capsize=10
)

plt.title("Percentage of Patients with Dementia by Sex")

plt.xlabel("Sex")

plt.ylabel("Percent with Dementia")

plt.show()




age_death = []

abeta42_levels = []


for patient in Patient.all_patients:

    if patient.abeta42 is not None:

        age_death.append(patient.age_of_death)

        abeta42_levels.append(patient.abeta42)


X = age_death

y = abeta42_levels


plt.scatter(X, y)

plt.xlabel("Age at Death")

plt.ylabel("Amyloid-Beta42 (pg/ug)")

plt.title("Amyloid-Beta42 Levels vs Age at Death")

plt.show()


Patient.all_patients.sort(
    key=lambda patient: patient.age_of_death,
    reverse=False
)

for patient in Patient.all_patients:

    print(patient)