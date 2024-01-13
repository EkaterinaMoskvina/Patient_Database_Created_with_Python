import psycopg2
conn = psycopg2.connect(dbname="ID_history", user="postgres", password="postgres", port="5432")
print('Connection is successful')

cursor = conn.cursor()

''' JOIN'''

sensation_strength = '''
SELECT sensation.light_touch, sensation.pain_temperature, sensation.proprioception, sensation.vibration,
       strength.motor_f_mean, strength.shoulder_abduction_r, strength.shoulder_abduction_l, wrist_extension_r
FROM sensation
LEFT JOIN strength ON sensation.id_patient = strength.id_patient
LIMIT 5
'''
cursor.execute(sensation_strength)
result = cursor.fetchall()
columns = [description[0] for description in cursor.description]
print(columns)

for row in result:
    print(row)


patient_history_neuroexam = '''
SELECT patient_history.id_patient, patient_history.age, patient_history.gender,
neurological_exam.EDSS_score, neurological_exam.handedness
FROM patient_history
JOIN neurological_exam ON patient_history.id_patient = neurological_exam.id_patient
LIMIT 3
'''

cursor.execute(patient_history_neuroexam)
result = cursor.fetchall()

columns = [description[0] for description in cursor.description]
print(columns)

for row in result:
    print(row)

conn.close()