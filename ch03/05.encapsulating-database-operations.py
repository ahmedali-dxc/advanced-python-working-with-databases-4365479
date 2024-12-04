import mysql.connector as mysql
from mysql.connector import Error
from sqlite3 import Cursor

def connect(db_name):
    try:
        return mysql.connect(host="localhost", user="root", password="root", database="projects")
    except Error as e:
        print(e)

def add_project(_cursor: Cursor, project_title, project_description, _tasks):
    project_data = (project_title, project_description)
    _cursor.execute('''INSERT INTO projects (title, description) VALUES (%s, %s)''', project_data)

    tasks_data = []
    for task in _tasks:
        task_data = (_cursor.lastrowid, task)
        tasks_data.append(task_data)
    _cursor.executemany('''INSERT INTO tasks (project_id, description) VALUES (%s, %s)''', tasks_data)

if __name__ == '__main__':
    db = connect("projects")
    cursor = db.cursor()

    tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
    add_project(cursor, "Clean house", "Clean house by room", tasks)
    db.commit()

    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)

    cursor.execute("SELECT * FROM tasks")
    tasks_records = cursor.fetchall()
    print(tasks_records)

    db.close()
