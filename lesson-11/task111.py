import sqlite3

values = [
    ('Benjamin Sisko', 'Human', 40), 
    ('Jadzia Dax', 'Trill', 300), 
    ('Kira Nerys', 'Bajoran', 29)
]

create_query = "CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, Age INT)"
insert_query = 'INSERT INTO Roster VALUES(?, ?, ?)'
update = "UPDATE Roster SET Name = 'Ezri Dax' WHERE Age = 300"
display = "SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'"
add = "ALTER TABLE Roster ADD COLUMN Rank TEXT"

add1 = "UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'"
add2 = "UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'"
add3 = "UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'"

delete = "DELETE FROM Roster WHERE Age > 100"
sorted_query = "SELECT * FROM Roster ORDER BY Age DESC"

with sqlite3.connect('roster.db') as f:
    cursor = f.cursor()
    cursor.execute(create_query)
    cursor.executemany(insert_query, values)
    cursor.execute(update)
    cursor.execute(display)
    print("Bajoran species before delete:", cursor.fetchall())
    cursor.execute(add)
    cursor.execute(add1)
    cursor.execute(add2)
    cursor.execute(add3)
    cursor.execute(delete)
    cursor.execute(sorted_query)
    print("Final Roster State (Sorted by Age):")
    for row in cursor.fetchall():
        print(row)


values1 = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]

create_query1 = "CREATE TABLE IF NOT EXISTS Books(Title TEXT, Author TEXT, Year_Published INT, Genre TEXT)"
insert_query1 = 'INSERT INTO Books VALUES(?, ?, ?, ?)'
update1 = "UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'"
display1 = "SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'"
add0 = "ALTER TABLE Books ADD COLUMN Rating REAL"

add10 = "UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'"
add20 = "UPDATE Books SET Rating = 4.7 WHERE Title = '1984'"
add30 = "UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'"

delete1 = "DELETE FROM Books WHERE Year_Published < 1950"
sorted1 = "SELECT * FROM Books ORDER BY Year_Published ASC"

with sqlite3.connect('library.db') as f:
    cursor = f.cursor()
    cursor.execute(create_query1)
    cursor.executemany(insert_query1, values1)
    cursor.execute(update1)
    cursor.execute(display1)
    print("Dystopian books:", cursor.fetchall())
    cursor.execute(add0)
    cursor.execute(add10)
    cursor.execute(add20)
    cursor.execute(add30)
    cursor.execute(delete1)
    cursor.execute(sorted1)
    print("Final Books State (Sorted by Year):")
    for row in cursor.fetchall():
        print(row)