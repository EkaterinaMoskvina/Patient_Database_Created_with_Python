import psycopg2

conn = psycopg2.connect(dbname="ID_history", user="postgres", password="postgres", port="5432")
cursor = conn.cursor()


# create table strength
cursor.execute("CREATE TABLE strength (id_patient SERIAL NOT NULL PRIMARY KEY, motor_f_mean INT, handedness CHAR(1),\
                shoulder_abduction_r INTEGER, elbow_extension_r INTEGER, wrist_extension_r INTEGER,\
                finger_abduction_r INTEGER,hip_flexion_r INTEGER,knee_flexion_r INTEGER,\
                ankle_dorsiflexion_r INTEGER, shoulder_abduction_l INTEGER, elbow_extension_l INTEGER,\
                wrist_extension_l INTEGER, finger_abduction_l INTEGER, hip_flexion_l INTEGER,\
                knee_flexion_l INTEGER, ankle_dorsiflexion_l INTEGER)")

# create table sleep
cursor.execute("CREATE TABLE sleep (id_patient SERIAL NOT NULL PRIMARY KEY, sum_of_score INT,\
               Epwortli_Sleepiness_Scale INTEGER, PSQI INTEGER)")

# create table psychoemotional_state
cursor.execute("CREATE TABLE psychoemotional_state (id_patient SERIAL NOT NULL PRIMARY KEY, sum_of_score INT,\
                DASS_21 INTEGER, MFI_20 INTEGER)")

# create table cranial_nerves
cursor.execute("CREATE TABLE cranial_nerves (id_patient SERIAL NOT NULL PRIMARY KEY,\
                I VARCHAR(50), II VARCHAR(50), III_IV_VI VARCHAR(50), V VARCHAR(50),\
                VII VARCHAR(50), VIII VARCHAR(50), IX_X VARCHAR(50),\
                XI VARCHAR(50),  XII VARCHAR(50))")

# create table coordination
cursor.execute("CREATE TABLE coordination (id_patient SERIAL NOT NULL PRIMARY KEY, sum_of_score INT,\
                finger_to_nose_r INTEGER, finger_to_nose_l INTEGER, heel_to_shin_r INTEGER,\
                heel_to_shin_l INTEGER, romberg_test INTEGER)")

# create table mental_state
cursor.execute("CREATE TABLE mental_state (id_patient SERIAL NOT NULL PRIMARY KEY, sum_of_score INT,\
                SDMT INTEGER, PASAT INTEGER, CVLT_II INTEGER,\
                BVMT_R INTEGER, Frontal_Assessment_Battery INTEGER)")

# create table sensation
cursor.execute("CREATE TABLE sensation (id_patient SERIAL NOT NULL PRIMARY KEY, sum_of_score INT,\
                light_touch INTEGER, pain_temperature INTEGER, proprioception INTEGER,\
                vibration INTEGER)")

# create table neurological_exam
cursor.execute("CREATE TABLE neurological_exam (id_patient SERIAL NOT NULL PRIMARY KEY, handedness CHAR(1),\
                EDSS_score INTEGER,\
                cranial_nerves_f INTEGER NOT NULL, FOREIGN KEY (cranial_nerves_f) REFERENCES cranial_nerves(id_patient),\
                coordination_f INTEGER NOT NULL, FOREIGN KEY (coordination_f) REFERENCES coordination(id_patient),\
                motor_f INT NOT NULL, FOREIGN KEY (motor_f) REFERENCES strength(id_patient), \
                sensation_f INTEGER NOT NULL, FOREIGN KEY (sensation_f) REFERENCES sensation(id_patient),\
                mental_state_f INTEGER NOT NULL, FOREIGN KEY (mental_state_f) REFERENCES mental_state(id_patient),\
                sleep_f INTEGER NOT NULL, FOREIGN KEY (sleep_f) REFERENCES sleep(id_patient),\
                psychoemotional_state_f INTEGER NOT NULL, FOREIGN KEY (psychoemotional_state_f) REFERENCES psychoemotional_state(id_patient))")


# create table patient_history
cursor.execute("CREATE TABLE patient_history (id_patient SERIAL PRIMARY KEY, age INTEGER,\
                gender CHAR(1), concomitant_illnesses VARCHAR(40), medication_history VARCHAR(40),\
                education INTEGER, substance_use VARCHAR(40), employment VARCHAR(40), job_category VARCHAR(40),\
                 diet VARCHAR(40), neurological_exam_f INTEGER NOT NULL, FOREIGN KEY(neurological_exam_f) REFERENCES neurological_exam(id_patient))")


# validate the transaction
conn.commit()
print("Tables successfully created")

cursor.close()
conn.close()