from patient_sarah import *

import matplotlib.pyplot as plt

import numpy as np

import statistics
#imports necessary extensions and patient_sarah file

Patient.instantiate_from_csv(
    "C:/Users/sarah/BME 2315/Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv"
) #opens csv data file

#Sort & print useful patient data
Patient.all_patients.sort(
    key=Patient.get_age_of_death,
    reverse=False
)
for patient in Patient.all_patients:

    print(patient) 

#Bar Graph

female_dementia = [] #empty list to iterate over for loop for female pt

male_dementia = [] #empty list to iterate over for loop for male pt


for patient in Patient.filter(Patient.all_patients, sex="Female"):
    female_dementia.append(int(patient.dementia))  #adds a 1 for female dementia pt and 0 for female non dementia pt


for patient in Patient.filter(Patient.all_patients, sex="Male"):
    male_dementia.append(int(patient.dementia))  #adds a 1 for male dementia pt and 0 for male non dementia pt


x_Female_bar = statistics.mean(female_dementia) * 100  #calculates mean percentage of female with dementia

x_Male_bar = statistics.mean(male_dementia) * 100 #calculates mean percentage of male with dementia



female_stdev = statistics.stdev(female_dementia) * 100 #calculates stdevof perecentage of female with dementia


male_stdev = statistics.stdev(male_dementia) * 100 #calculates stdevof perecentage of male with dementia


print(f'x_Female_bar = {x_Female_bar}, female_stdev = {female_stdev}') #prints data that we are about to graph

print(f'x_Male_bar = {x_Male_bar}, male_stdev = {male_stdev}')


sex_cols = ["Female", "Male"] #names the columns

mean_sex = [x_Female_bar, x_Male_bar] #names y-axis values

stdev_sex = [female_stdev, male_stdev] #names stdev values

yerr = [np.zeros(len(mean_sex)), stdev_sex] #sets up error bars


plt.bar(
    sex_cols,
    mean_sex,
    yerr=yerr,
    capsize=10
) #plots on a bar graph

plt.title("Percentage of Patients with Dementia by Sex") #title

plt.xlabel("Sex") #label for x axis

plt.ylabel("Percent with Dementia") #label for y axis

plt.show() #shows us the graph


#Scatterplot

age_death = [] #intializes empty list for age of death data

abeta42_levels = [] #intializes empty list for abeta level data


for patient in Patient.all_patients:

    if patient.abeta42 is not None:

        age_death.append(patient.age_of_death)

        abeta42_levels.append(patient.abeta42)#goes through for loop and adds data to each respective list if it's not an empty cell


X = age_death #defines x and y valyes for each variable

y = abeta42_levels


plt.scatter(X, y) #plots values on scatterplot

plt.xlabel("Age at Death") #adds x-axis label

plt.ylabel("Amyloid-Beta42 (pg/ug)") #adds y-axis label

plt.title("Amyloid-Beta42 Levels vs Age at Death") #adds title

plt.show() #shows us the graph


