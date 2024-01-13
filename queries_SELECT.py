import psycopg2
conn = psycopg2.connect(dbname="ID_history", user="postgres", password="postgres", port="5432")
print('Connection is successful')

cursor = conn.cursor()

'''SELECT'''
# def getAllRows():
#     try:
#         conn = psycopg2.connect(dbname="ID_history", user="postgres", password="postgres", port="5432")
#         print('Connection is successful')
#
#         cursor = conn.cursor()
#         sql_query = 'SELECT * FROM sleep'
#         cursor.execute(sql_query)
#         # fetch all the rows of a query result
#         rows = cursor.fetchall()
#
#         print("Total rows are:  ", len(rows))
#         print("Printing each row")
#         for row in rows:
#             print("id_patient: ", row[0])
#             print("sum_of_score: ", row[1])
#             print("Epwortli_Sleepiness_Scale: ", row[2])
#             print("PSQI: ", row[3])
#             print("\n")
#
#         cursor.close()
#
#     except psycopg2.Error as error:
#         print("Failed to read data from table", error)
#     finally:
#         if conn:
#             conn.close()
#             print("The connection is closed")
#
# getAllRows()



# cursor.execute("SELECT id_patient, PSQI FROM sleep")
#
#
# rows = cursor.fetchmany(3)
#
# for row in rows:
#     print("id_patient: ", row[0])
#     print("PSQI: ", row[1])
#     print("\n")
#
#
# cursor.close()
# conn.close()


# cursor.execute("SELECT id_patient, SDMT FROM mental_state\
#                WHERE SDMT = 50")
# rows = cursor.fetchmany(3)
# for row in rows:
#     print("id_patient: ", row[0])
#     print("SDMT: ", row[1])
#     print("\n")
#
# cursor.close()
# conn.close()


# cursor.execute("SELECT id_patient, SDMT FROM mental_state\
#                WHERE SDMT > 70")
# rows = cursor.fetchmany(3)
# for row in rows:
#     print("id_patient: ", row[0])
#     print("SDMT: ", row[1])
#     print("\n")
#
# cursor.close()
# conn.close()

# cursor.execute("SELECT id_patient, motor_f_mean FROM strength\
#                WHERE handedness = 'r' and motor_f_mean > 2")
# rows = cursor.fetchmany(3)
# for row in rows:
#     print("id_patient: ", row[0])
#     print("motor_f_mean: ", row[1])
#     print("\n")
#
# cursor.close()
# conn.close()

# cursor.execute("SELECT id_patient, motor_f_mean FROM strength\
#                WHERE handedness = 'r' and motor_f_mean > 2")
# rows = cursor.fetchmany(3)
# for row in rows:
#     print("id_patient: ", row[0])
#     print("motor_f_mean: ", row[1])
#     print("\n")
#
# cursor.close()
# conn.close()