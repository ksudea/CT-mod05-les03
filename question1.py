import mysql.connector

db_name = "fitness_center_db"
user = "root"
password = "0711"
host = "127.0.0.1"

# Task 1

def add_member(id, name, age):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host)
        cursor = conn.cursor()

        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(query, (id, name, age))
        conn.commit()
        print("Successfully added member!")
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


# Task 2
# Existing WorkoutSessions table from last assignment has completely different columns
# Created New WorkoutSessionsUpdated table in db with the following

"""USE fitness_center_db;
        CREATE TABLE WorkoutSessionsDetailed (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    duration INT,
    calories_burned INT,
    FOREIGN KEY (member_id) REFERENCES Members(id));
"""
import random
# Keeping a set of used session ids so we don't attempt to create a duplicate session id 
used_session_id = {-1,-2}

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host)
        cursor = conn.cursor()
        session_id = random.randint(200, 3000)
        while session_id in used_session_id:
            session_id = random.randint(200, 3000)
        query = """INSERT INTO 
        WorkoutSessionsDetailed (session_id, member_id, session_date, duration, calories_burned) 
        VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (session_id, member_id, date, duration_minutes, calories_burned))
        conn.commit()
        used_session_id.add(session_id)
        print(f"Successfully added workout session with ID {session_id}")
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close() 

# Task 3

def update_member_age(member_id, new_age):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host)
        cursor = conn.cursor()

        query = "UPDATE Members SET age = %s WHERE id = %s"
        cursor.execute(query, (new_age, member_id))
        conn.commit()
        print("Successfully updated age")
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


# Task 4

def delete_workout_session(session_id):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host)
        cursor = conn.cursor()
        query = "DELETE FROM WorkoutSessionsDetailed WHERE session_id = %s"
        cursor.execute(query, (session_id,))
        conn.commit()
        print("Successfully deleted workout session")
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
