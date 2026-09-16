from patient import * #importing data from patient.py

import matplotlib.pyplot as plt #importing matplotlib for plotting bar graph
import numpy as np 
import statistics #importing statistics for calculating mean and standard deviation


patient_objects.instantiate_from_csv("/Users/williambarlow/Library/CloudStorage/OneDrive-UniversityofVirginia/Second Year/First Semester/BME 2315/Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv") #instantiating patient objects from the csv file


#Question 4: Printing patient objects from csv
for patient in patient_objects.all_patients:
    print(patient) #printing list of patient objects for each patient



#Question 5: Sort patients by age of diagnosis from youngest to oldest, moves empty values to the end of the list
patient_objects.all_patients.sort(
    key=patient_objects.get_age_of_diagnosis,
    reverse=False
)

for patient in patient_objects.all_patients:
    print(patient) #printing list of patient objects for each patient sorted by age of diagnosis from youngest to oldest


#Question 6: Filter patients by age of diagnosis and age of death

filtered_patients = patient_objects.filter_age_range(80, 90, 85, 95) #filtering patients by age of diagnosis between 80 and 90 and age of death between 85 and 95

for patient in filtered_patients:
    print(patient) #printing list of patient objects for each patient filtered by age of diagnosis and age of death


#Question 7: Create bar graph with standard deviation for age of symptom onset for male and female patients

age_female_patients = [] #creating an empty list to store age of symptom onset for female patients
age_male_patients = [] #creating an empty list to store age of symptom onset for male

for patient in patient_objects.all_patients:
    if patient.sex == "Female" and patient.age_of_symptom_onset != "":
        age_female_patients.append(patient.age_of_symptom_onset) #appending list of age of symptom onset for female patients

for patient in patient_objects.all_patients:
    if patient.sex == "Male" and patient.age_of_symptom_onset != "":
        age_male_patients.append(patient.age_of_symptom_onset) #appending list of age of symptom onset for male patients

#calculates mean symptom onset age for male and female patients
female_mean = statistics.mean(age_female_patients)  
male_mean = statistics.mean(age_male_patients)

#calculates standard deviation for symptom onset age for male and female patients
female_stdev = statistics.stdev(age_female_patients)
male_stdev = statistics.stdev(age_male_patients)

patient_sex = ["Female", "Male"]

mean_onset_age = [female_mean, male_mean]
stdev_onset_age = [female_stdev, male_stdev]

#creates bar graph with bar height as mean symptom onset age and error bars as plus and minus one standard deviation
plt.bar(patient_sex, mean_onset_age, yerr=stdev_onset_age, capsize=10)

plt.title("Average Age of Symptom Onset by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Age of Symptom Onset (Years)")

plt.show()


#Question 8: Scatterplot comparing age of diagnosis and age of death

diagnosis_ages = []
death_ages = []

#only displays patients with both diagnosis and death ages so all points represent one patient
for patient in patient_objects.all_patients:
    if patient.age_of_diagnosis != "" and patient.age_of_death != "":
        diagnosis_ages.append(patient.age_of_diagnosis) #appending list of age of diagnosis for patients
        death_ages.append(patient.age_of_death) #appending list of age of death for patients

#creates scatterplot for relationship between age of diagnosis and age of death for patients
plt.scatter(diagnosis_ages, death_ages)
plt.title("Age of Dementia Diagnosis vs Age of Death")
plt.xlabel("Age of Dementia Diagnosis (Years)")
plt.ylabel("Age of Death (Years)")

plt.show()

'''
Ai Usage:
I used AI to help me write and understand code for problems 5-8 while also refering to the README.md file for the dog data set assignment.
I was able to get a broad understanding of what to do using the README file but had AI speicifically help me and explain problems 5-8 when I was stuck.
'''