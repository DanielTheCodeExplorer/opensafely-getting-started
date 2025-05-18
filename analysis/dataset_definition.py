from ehrql import create_dataset
from ehrql.tables.tpp import patients, practice_registrations

dataset = create_dataset()

index_date = "2020-03-31"

# Getting patients with the index date of 31 of march 2020
has_registration = practice_registrations.for_patient_on(
    index_date
).exists_for_patient()

#Probably changing data type 
dataset.define_population(has_registration)

#Setting some values in the dataset
dataset.sex = patients.sex
dataset.age = patients.age_on(index_date)