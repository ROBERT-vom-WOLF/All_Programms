# create table animals(
#     name TEXT,
#     breed TEXT,
#     age INTEGER
# );
# insert into animals (name, breed, age) values ('blue', 'Scottish Fold', 3);

import sqlite3 as sq
connection = sq.connect('friends.db')
cursor = connection.cursor()

# cursor.execute("create table friends (first_name TEXT, laste_name TEXT, closeness INTEGER);")
# cursor.execute("insert into friends values('Lewis', 'Hammilton', 7);")
people = [
    # ("Roald", "Amundsen", 5),
    # ("Rosa", "Parks", 8),
    # ("Henry", "Hudson", 7),
    # ("Neil", "Armstrong", 7),
    # ("Daniel", "Boone", 3),
    # ("Max", "Verstappen", 0)
]
# cursor.executemany("insert into friends values(?, ?, ?)", people)

cursor.execute("select * from friends")
print(cursor.fetchall())
cursor.execute("select * from friends where closeness < 5 order by closeness desc")
print(cursor.fetchall())
cursor.execute("update friends set closeness=10 where laste_name='Armstrong'")
connection.commit()
connection.close()
