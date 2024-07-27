import mysql.connector

db_name = "fitness_center_db"
user = "root"
password = "0711"
host = "127.0.0.1"

# Task 1

def get_members_in_age_range(start_age, end_age):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host)
        cursor = conn.cursor()

        query = """SELECT * FROM Members
        WHERE age BETWEEN %s AND %s"""
        cursor.execute(query, (start_age, end_age))
        print(f"Members between {start_age} and {end_age} years of age:")
        for member in cursor.fetchall():
            print(member)
        conn.commit()
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

get_members_in_age_range(25, 30)
