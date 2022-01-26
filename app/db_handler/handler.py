import os, time
import psycopg2

def GetCities(username):
    qry = f'''SELECT * from notes;'''
    cursor.execute(qry)
    return cursor.fetchall()


while True:
    try:
        conn = psycopg2.connect(
            host = os.environ['DB_HOST'],
            database = os.environ['DB_NAME'],
            user = os.environ['DB_USERNAME'],
            password = os.environ['DB_PASSWORD']
        )
        cursor = conn.cursor()
        print("Database Connected Successifully :-)")
        break
        
    except Exception as error:
        print("Connecting to database failed...Trying Again...")
        print("Error:", error)
        time.sleep(2)
        
