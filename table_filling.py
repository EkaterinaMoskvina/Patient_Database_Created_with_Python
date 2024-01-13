import hashlib
from psycopg2.extensions import AsIs
import psycopg2
import random


conn = psycopg2.connect(dbname="ID_history", user="postgres", password="postgres", port="5432")
cursor = conn.cursor()


def insert_data_into_strength(id_patient, motor_f_mean, handedness, shoulder_abduction_r, elbow_extension_r, wrist_extension_r,
                              finger_abduction_r, hip_flexion_r, knee_flexion_r, ankle_dorsiflexion_r, shoulder_abduction_l, elbow_extension_l,
                              wrist_extension_l, finger_abduction_l, hip_flexion_l,
                              knee_flexion_l, ankle_dorsiflexion_l):

    insert_query_strength = 'INSERT INTO strength(id_patient, motor_f_mean,handedness,shoulder_abduction_r,elbow_extension_r,wrist_extension_r,\
                            finger_abduction_r,hip_flexion_r,knee_flexion_r,ankle_dorsiflexion_r, shoulder_abduction_l,\
                            elbow_extension_l, wrist_extension_l, finger_abduction_l, hip_flexion_l,\
                            knee_flexion_l, ankle_dorsiflexion_l) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                             %s, %s, %s, %s, %s, %s)'

    cursor.execute(insert_query_strength, (id_patient, motor_f_mean, handedness, shoulder_abduction_r, elbow_extension_r, wrist_extension_r,
                            finger_abduction_r, hip_flexion_r, knee_flexion_r, ankle_dorsiflexion_r, shoulder_abduction_l,
                            elbow_extension_l, wrist_extension_l, finger_abduction_l, hip_flexion_l, knee_flexion_l, ankle_dorsiflexion_l))


for i in range(1, 1001):
    id_patient = i
    handedness = random.choice(['r', 'l'])
    shoulder_abduction_r = random.randint(1, 5)
    elbow_extension_r = random.randint(1, 5)
    wrist_extension_r = random.randint(1, 5)
    finger_abduction_r = random.randint(1, 5)
    hip_flexion_r = random.randint(1, 5)
    knee_flexion_r = random.randint(1, 5)
    ankle_dorsiflexion_r = random.randint(1, 5)
    shoulder_abduction_l = random.randint(1, 5)
    elbow_extension_l = random.randint(1, 5)
    wrist_extension_l = random.randint(1, 5)
    finger_abduction_l = random.randint(1, 5)
    hip_flexion_l = random.randint(1, 5)
    knee_flexion_l = random.randint(1, 5)
    ankle_dorsiflexion_l = random.randint(1, 5)

# mean of strength
    motor_f_mean = round((shoulder_abduction_r + elbow_extension_r + wrist_extension_r + finger_abduction_r +
                          hip_flexion_r + knee_flexion_r + ankle_dorsiflexion_r + shoulder_abduction_l +
                          elbow_extension_l + wrist_extension_l + finger_abduction_l + hip_flexion_l +
                          knee_flexion_l + ankle_dorsiflexion_l) / 14, 1)

    insert_data_into_strength(id_patient, motor_f_mean, handedness, shoulder_abduction_r, elbow_extension_r, wrist_extension_r,
                              finger_abduction_r, hip_flexion_r, knee_flexion_r, ankle_dorsiflexion_r, shoulder_abduction_l, elbow_extension_l,
                              wrist_extension_l, finger_abduction_l, hip_flexion_l,
                              knee_flexion_l, ankle_dorsiflexion_l)


"""TABLE SLEEP"""
def insert_data_into_sleep(id_patient,sum_of_score, Epwortli_Sleepiness_Scale, PSQI):
    insert_query_sleep = 'INSERT INTO sleep(id_patient, sum_of_score, Epwortli_Sleepiness_Scale, PSQI) VALUES (%s, %s, %s, %s)'
    cursor.execute(insert_query_sleep, (id_patient, sum_of_score, Epwortli_Sleepiness_Scale, PSQI))

for i in range(1, 1001):
    id_patient = i
    Epwortli_Sleepiness_Scale = random.randint(0,24)
    PSQI = random.randint(0,21)
    sum_of_score = sum([Epwortli_Sleepiness_Scale, PSQI])

    insert_data_into_sleep(id_patient, sum_of_score, Epwortli_Sleepiness_Scale, PSQI)

"""TABLE psychoemotional_state"""
def insert_data_into_psychoemotional_state(id_patient, sum_of_score, DASS_21, MFI_20):
    insert_query_psychoemotional_state = 'INSERT INTO psychoemotional_state(id_patient, sum_of_score, DASS_21, MFI_20) VALUES (%s, %s, %s, %s)'
    cursor.execute(insert_query_psychoemotional_state, (id_patient, sum_of_score, DASS_21, MFI_20))

for i in range(1, 1001):
    id_patient = i
    DASS_21 = random.randint(0,63)
    MFI_20 = random.randint(20,100)
    sum_of_score = sum([DASS_21, MFI_20])

    insert_data_into_psychoemotional_state(id_patient, sum_of_score, DASS_21, MFI_20)


"""TABLE cranial_nerves"""

def insert_data_into_cranial_nerves(id_patient, I=None, II=None, III_IV_VI=None, V=None, VII=None, VIII=None, IX_X=None, XI=None, XII=None):
    insert_query_cranial_nerves = 'INSERT INTO cranial_nerves(id_patient, I, II, III_IV_VI, V, VII, VIII, IX_X, XI, XII) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(insert_query_cranial_nerves, (id_patient, I, II, III_IV_VI, V, VII, VIII, IX_X, XI, XII))

for i in range(1, 1001):
    id_patient = i

    insert_data_into_cranial_nerves(id_patient)


"""TABLE coordination"""
def insert_data_into_coordination(id_patient, sum_of_score, finger_to_nose_r, finger_to_nose_l, heel_to_shin_r, heel_to_shin_l, romberg_test):
    insert_query_coordination = 'INSERT INTO coordination(id_patient, sum_of_score, finger_to_nose_r, finger_to_nose_l, heel_to_shin_r,heel_to_shin_l, romberg_test) VALUES\
     (%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(insert_query_coordination, (id_patient, sum_of_score, finger_to_nose_r, finger_to_nose_l, heel_to_shin_r, heel_to_shin_l, romberg_test))

for i in range(1, 1001):
    id_patient = i
    finger_to_nose_r = random.randint(0,5)
    finger_to_nose_l = random.randint(0,5)
    heel_to_shin_r = random.randint(0,5)
    heel_to_shin_l = random.randint(0,5)
    romberg_test = random.randint(0,5)
    sum_of_score = sum([finger_to_nose_r, finger_to_nose_l, heel_to_shin_r, heel_to_shin_l, romberg_test])

    insert_data_into_coordination(id_patient, sum_of_score, finger_to_nose_r, finger_to_nose_l, heel_to_shin_r, heel_to_shin_l, romberg_test)

"""TABLE mental_state"""
def insert_data_into_mental_state(id_patient, sum_of_score, SDMT, PASAT, CVLT_II, BVMT_R, Frontal_Assessment_Battery):
    insert_query_mental_state = 'INSERT INTO mental_state(id_patient, sum_of_score, SDMT, PASAT, CVLT_II, BVMT_R, Frontal_Assessment_Battery) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(insert_query_mental_state, (id_patient, sum_of_score, SDMT, PASAT, CVLT_II, BVMT_R, Frontal_Assessment_Battery))

for i in range(1, 1001):
    id_patient = i
    SDMT = random.randint(0,110)
    PASAT = random.randint(0,1500)
    CVLT_II = random.randint(0,100)
    BVMT_R = random.randint(0,100)
    Frontal_Assessment_Battery = random.randint(0,18)

    sum_of_score = sum([id_patient, SDMT, PASAT, CVLT_II, BVMT_R, Frontal_Assessment_Battery])

    insert_data_into_mental_state(id_patient, sum_of_score, SDMT, PASAT, CVLT_II, BVMT_R, Frontal_Assessment_Battery)


"""TABLE sensation"""
def insert_data_into_sensation(id_patient, sum_of_score, light_touch, pain_temperature, proprioception, vibration):
    insert_query_sensation = 'INSERT INTO sensation(id_patient, sum_of_score, light_touch, pain_temperature, proprioception, vibration) VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.execute(insert_query_sensation, (id_patient, sum_of_score,light_touch, pain_temperature, proprioception, vibration))

for i in range(1, 1001):
    id_patient = i
    light_touch = random.randint(0,3)
    pain_temperature = random.randint(0,3)
    proprioception = random.randint(0,3)
    vibration = random.randint(0,3)
    sum_of_score = sum([light_touch, pain_temperature, proprioception, vibration])

    insert_data_into_sensation(id_patient, sum_of_score, light_touch, pain_temperature, proprioception, vibration)


"""TABLE neurological_exam"""
def insert_data_into_neurological_exam(id_patient, handedness, EDSS_score, cranial_nerves_f,
                coordination_f, motor_f, sensation_f, mental_state_f, sleep_f, psychoemotional_state_f):
    insert_query_neurological_exam = 'INSERT INTO neurological_exam(id_patient, handedness, EDSS_score,cranial_nerves_f, coordination_f, motor_f, sensation_f, mental_state_f,sleep_f,psychoemotional_state_f)\
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(insert_query_neurological_exam, (id_patient, handedness, EDSS_score, cranial_nerves_f,
                coordination_f, motor_f, sensation_f, mental_state_f, sleep_f, psychoemotional_state_f))

for i in range(1, 1001):
    id_patient = i
    handedness = random.choice(['r', 'l'])
    EDSS_score = random.randint(0,10)
    cranial_nerves_f = i
    coordination_f = i
    motor_f = i
    sensation_f = i
    mental_state_f = i
    sleep_f = i
    psychoemotional_state_f = i

    insert_data_into_neurological_exam(id_patient, handedness, EDSS_score, cranial_nerves_f,
                                       coordination_f, motor_f, sensation_f, mental_state_f, sleep_f,
                                       psychoemotional_state_f)


"""TABLE patient_history"""
def insert_data_into_patient_history(id_patient, age, gender, neurological_exam_f):
    insert_query_patient_history = "INSERT INTO patient_history (id_patient, age, gender, concomitant_illnesses, medication_history, education, substance_use, employment, job_category,\
     diet, neurological_exam_f) VALUES (%s, %s, %s, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, %s)"
    cursor.execute(insert_query_patient_history, (id_patient, age, gender, neurological_exam_f))

#Random data generation and query execution
for i in range(1, 1001):
    id_patient = i
    age = random.randint(1,65)
    gender = random.choice(["m", "f"])
    neurological_exam_f = i

    insert_data_into_patient_history(id_patient, age, gender, neurological_exam_f)


#Fixing changes in the database
conn.commit()
print("Data successfully inserted")

# close connection
cursor.close()
conn.close()



# Function for executing a query and inserting data into the database
# def insert_data(id_patient, age, gender, neurological_exam_f):
#     insert_query = "INSERT INTO patient_history (id_patient, age, gender, concomitant_illnesses, medication_history, education, substance_use, employment, job_category,\
#      diet, neurological_exam_f) VALUES (%s, %s, %s, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, %s)"
#     cursor.execute(insert_query, (id_patient, age, gender, neurological_exam_f))
#
# #Random data generation and query execution
# for i in range(1, 1001):
#     id_patient = i
#     age = random.randint(1,65)
#     gender = random.choice(["m", "f"])
#     neurological_exam_f = random.randint(0, 1)
#
#     insert_data(id_patient, age, gender, neurological_exam_f)
#
# #Fixing changes in the database
# conn.commit()
# print("Data successfully inserted")
#
# #close connection
# cursor.close()
# conn.close()


