import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('schedule.db')

# Create a cursor object
cursor = conn.cursor()

# Function to drop existing tables | Info
def drop_existing_tables_info(info_schedule_name):
    cursor.execute(f'DROP TABLE IF EXISTS {info_schedule_name}')
    cursor.execute(f'DROP TABLE IF EXISTS {info_schedule_name}_data')
    # commit the changes
    conn.commit()

# Function to drop existing tables
def drop_existing_tables(schedule_name):
    cursor.execute(f'DROP TABLE IF EXISTS {schedule_name}')
    # commit the changes
    conn.commit()

# Function to create a info-schedule table
def create_schedule_table_info(schedule_name):
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {schedule_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timer INTEGER,
        data_id INTEGER,
        hide BOOLEAN,
        type TEXT,
        FOREIGN KEY (data_id) REFERENCES {schedule_name}_data(id)
    )
    ''')
    
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {schedule_name}_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        logo TEXT,
        flight TEXT,
        arrival TEXT,
        departure TEXT,
        status TEXT
    )
    ''')
    # commit the changes
    conn.commit()


# Function to create a schedule table
def create_schedule_table(schedule_name):
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {schedule_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timer INTEGER,
        data TEXT,
        hide BOOLEAN,
        type TEXT
    )
    ''')
    # commit the changes
    conn.commit()
    

# Drop existing tables and create new ones
# schedules = ['schedule1', 'schedule2']  # Add more schedules as needed
# for schedule in schedules:
#     drop_existing_tables(schedule)
#     create_schedule_table(schedule)

# Function to insert data into the info_schedule table | Info
def insert_info_schedule_data(schedule_name, timer, data, hide, type):
    cursor.execute(f'''
    INSERT INTO {schedule_name}_data (logo, flight, arrival, departure, status)
    VALUES (?, ?, ?, ?, ?)
    ''', (data['logo'], data['flight'], data['arrival'], data['departure'], data['status']))
    
    data_id = cursor.lastrowid
    
    cursor.execute(f'''
    INSERT INTO {schedule_name} (timer, data_id, hide, type)
    VALUES (?, ?, ?, ?)
    ''', (timer, data_id, hide, type))

# Function to insert data into the schedule table
def insert_schedule_data(schedule_name, timer, data, hide, type):
    cursor.execute(f'''
    INSERT INTO {schedule_name} (timer, data, hide, type)
    VALUES (?, ?, ?, ?)
    ''', (timer, str(data), hide, type))

# Example usage
# insert_schedule_data('schedule1', 3000, {
#     'logo': 'static/images/delta-logo.png',
#     'flight': 'AA123',
#     'arrival': '10:00 AM',
#     'departure': '12:00 PM',
#     'status': 'On Time'
# }, False, 'info')

# GET DATA

# Create a cursor object

create_schedule_table_info('schedule2')

# insert_schedule_data(schedule_name='schedule1', timer=3000, data='/src/', hide=False, type='image')
# insert_info_schedule_data(
#     schedule_name='schedule2',
#     timer=3000,
#     data={
#         'logo': 'static/images/delta-logo.png',
#         'flight': 'AA123',
#         'arrival': '10:00 AM',
#         'departure': '12:00 PM',
#         'status': 'On Time'
#     },
#     hide=False,
#     type='info'
# )

# GET ALL SCHEDULES
def get_all_schedules() -> list:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    schedules = [schedule[0] for schedule in cursor.fetchall() if schedule[0] != 'sqlite_sequence']
    print(schedules)
    return schedules

# get_all_schedules()
# print(_:=cursor.execute("SELECT * FROM schedule2_data").fetchall())
# drop_existing_tables('schedule2')
# print(schedules)
# for schedule in schedules:
#     cursor.execute(f"SELECT * FROM {schedule[0]}")
#     print(cursor.fetchall())
# print(cursor.fetchall())

# Commit the changes and close the connection
conn.commit()
conn.close()