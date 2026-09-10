#List of headers in the metadata csv
import pandas as pd

df = pd.read_csv("/Users/williambarlow/Library/CloudStorage/OneDrive-UniversityofVirginia/Second Year/First Semester/BME 2315/Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print(header)

