import psycopg2
conn = psycopg2.connect(dbname="ID_history", user="postgres", password="postgres", port="5432")
print('Connection is successful')

cursor = conn.cursor()

print('-subquery_1-')

subquery_1 = '''
SELECT id_patient, 
       ROUND(avg_coordination.avg_coordination_f, 2) AS avg_coordination_f,
       ROUND(avg_motor.avg_motor_f, 2) AS avg_motor_f,
       ROUND(avg_EDSS.avg_EDSS_score, 2) AS avg_EDSS_score
FROM neurological_exam
CROSS JOIN (
    SELECT AVG(coordination_f) AS avg_coordination_f FROM neurological_exam
) AS avg_coordination
CROSS JOIN (
    SELECT AVG(motor_f) AS avg_motor_f FROM neurological_exam
) AS avg_motor
CROSS JOIN (
    SELECT AVG(EDSS_score) AS avg_EDSS_score FROM neurological_exam
) AS avg_EDSS
LIMIT 3
'''

cursor.execute(subquery_1)
result = cursor.fetchall()

for row in result:
    id_patient, avg_coordination_f, avg_motor_f, avg_EDSS_score = row
    print(f"ID Patient: {id_patient}, Avg Coordination: {avg_coordination_f}, Avg Motor: {avg_motor_f}, Avg EDSS: {avg_EDSS_score}")

print('----------------')
print('-subquery_2-')

subquery_2 = '''
SELECT id_patient, avg_coordination_f, avg_motor_f, avg_EDSS_score, (avg_coordination_f + avg_motor_f) AS total_avg
FROM (
    SELECT id_patient,
        ROUND(AVG(coordination_f),2) AS avg_coordination_f,
        ROUND(AVG(motor_f),2) AS avg_motor_f,
        ROUND(AVG(EDSS_score),2) AS avg_EDSS_score
    FROM neurological_exam
    GROUP BY id_patient
) AS avg_values
ORDER BY total_avg DESC
LIMIT 5
'''

cursor.execute(subquery_2)
result = cursor.fetchall()

for row in result:
    id_patient, avg_coordination_f, avg_motor_f, avg_EDSS_score, total_avg = row
    print(f"ID Patient: {id_patient}, Avg Coordination: {avg_coordination_f}, Avg Motor: {avg_motor_f}, Avg EDSS: {avg_EDSS_score}, Total Avg: {total_avg}")

conn.close()