from copy import deepcopy

patient_data = {'heart_rate': [60, 61, 62, 60, 61]}
patient_data_copy = patient_data.copy() # неправильно
patient_data_copy['heart_rate'].append(63)
print(patient_data)
print(patient_data_copy)

print('==='*15)

patient_data = {'heart_rate': [60, 61, 62, 60, 61]}
patient_data_copy = deepcopy(patient_data) # правильно!
patient_data_copy['heart_rate'].append(63)
print(patient_data)
print(patient_data_copy)