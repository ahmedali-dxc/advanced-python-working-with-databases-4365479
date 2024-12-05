import psycopg2

conn = psycopg2.connect(database="red30", user="postgres", password="postgres", host="localhost", port="5432")

cursor = conn.cursor()

sales = [
    (1100935, 'Spencer Educator', 'DK204', 'BY0D-300', 2, 89, 0, 178),
    (1100948, 'Ewan Ladd', 'TV810', 'Understanding Automation', 1, 44.95, 0, 44.95),
    (1100963, 'Stehr Group', 'DS301', 'AD-SA702 Drone', 3, 399, 1, 1077),
    (1100971, 'Hettinger and Sons', 'DS306', 'AD-SA702 Drone', 12, 250, 5, 1500),
    (1100998, "Luz O'Donohue", 'TV809', 'Understanding 3D Printing', 1, 42.99, 0, 42.99)
]

cursor.executemany("INSERT INTO SALES VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", sales)

conn.commit()
conn.close()