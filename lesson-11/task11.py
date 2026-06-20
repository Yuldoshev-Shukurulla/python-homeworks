# ### Task 1

# 1. **Database Creation**:
#    - Create a new SQLite database named `roster.db`.
#    - Define a table called **Roster** with the following schema:
#      - **Name**: TEXT
#      - **Species**: TEXT
#      - **Age**: INTEGER

# 2. **Insert Data**:
#    - Populate the **Roster** table with the following entries:

# | Name           | Species  | Age |
# |----------------|----------|-----|
# | Benjamin Sisko | Human    | 40  |
# | Jadzia Dax     | Trill    | 300 |
# | Kira Nerys     | Bajoran  | 29  |

# 3. **Update Data**:
#    - Update the `Name` of **Jadzia Dax** to **Ezri Dax**.

# 4. **Query Data**:
#    - Retrieve and display the **Name** and **Age** of all characters where the `Species` is **Bajoran**.

# 5. **Delete Data**:
#    - Remove all characters aged over 100 years from the table.

# 6. **Bonus Task**:
#    - Add a new column called `Rank` to the **Roster** table and update the data with the following values:
   
# | Name           | Rank       |
# |----------------|------------|
# | Benjamin Sisko | Captain    |
# | Ezri Dax       | Lieutenant |
# | Kira Nerys     | Major      |

# 7. **Advanced Query**:
#    - Retrieve all characters sorted by their `Age` in descending order.
import os
os.chdir('D:\MAAB\python-homeworks\lesson-11')
import sqlite3
values = [('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)]
create_query = "Create table Roster(Name TEXT, Species TEXT, Age INT)"
insert_query = 'INSERT INTO Roster VALUES(?, ?, ?)'
update = "UPDATE Roster Set Name = 'Ezri Dax' WHERE Age = 300"
display = "SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'"
delete = "DELETE FROM Roster WHERE age>100"
add = "ALTER TABLE Roster ADD COLUMN Rank TEXT"
add1 = "UPDATE Roster SET Rank = 'Captain' Where Name = 'Benjamin Sisko'"
add2 = "UPDATE Roster SET Rank = 'Lieutenant' Where Name = 'Ezri Dax'"
add3 = "UPDATE Roster SET Rank = 'Major' Where Name = 'Kira Nerys'"
sorted = "Select * FROM Roster order by age desc"
with sqlite3.connect('roster.db') as f:
    cursor = f.cursor()
    cursor.execute(create_query)
    cursor.executemany(insert_query,values)
    cursor.execute(update)
    data = cursor.execute(display)
    print(data.fetchall())
    cursor.execute(add)
    cursor.execute(add1)
    cursor.execute(add2)
    cursor.execute(add3)
    cursor.execute(delete)




# ### Task 2

# 1. **Database Creation**:
#    - Create a new SQLite database named `library.db`.
#    - Define a table called **Books** with the following schema:
#      - **Title**: TEXT
#      - **Author**: TEXT
#      - **Year_Published**: INTEGER
#      - **Genre**: TEXT

# 2. **Insert Data**:
#    - Populate the **Books** table with the following entries:

# | Title                  | Author          | Year_Published | Genre      |
# |------------------------|-----------------|----------------|------------|
# | To Kill a Mockingbird  | Harper Lee      | 1960           | Fiction    |
# | 1984                   | George Orwell   | 1949           | Dystopian  |
# | The Great Gatsby       | F. Scott Fitzgerald | 1925        | Classic    |

# 3. **Update Data**:
#    - Update the `Year_Published` of **1984** to **1950**.

# 4. **Query Data**:
#    - Retrieve and display the **Title** and **Author** of all books where the `Genre` is **Dystopian**.

# 5. **Delete Data**:
#    - Remove all books published before the year 1950 from the table.

# 6. **Bonus Task**:
#    - Add a new column called `Rating` to the **Books** table and update the data with the following values:

# | Title                  | Rating |
# |------------------------|--------|
# | To Kill a Mockingbird  | 4.8    |
# | 1984                   | 4.7    |
# | The Great Gatsby       | 4.5    |

# 7. **Advanced Query**:
#    - Retrieve all books sorted by their `Year_Published` in ascending order.

# ---
import os
os.chdir('D:\MAAB\python-homeworks\lesson-11')
import sqlite3
values1 = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]
create_query1 = "Create table Books(Title TEXT, Author TEXT, Year_Published INT, Genre TEXT)"
insert_query1 = 'INSERT INTO Books VALUES(?, ?, ?, ?)'
update1 = "UPDATE Books Set Title = '1950' WHERE Title = '1984'"
display1 = "SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'"
delete1 = "DELETE FROM Books WHERE Year_Published < 1950"
add0 = "ALTER TABLE Books ADD COLUMN Rating Int"
add10 = "UPDATE Books SET Rating = 4.8 Where Title = 'To Kill a Mockingbird'"
add20 = "UPDATE Books SET Rating = 4.7 Where Title = '1984'"
add30 = "UPDATE Books SET Rating = 4.5 Where Title = 'The Great Gatsby'"
sorted1 = "Select * FROM Books order by Year_Published ASC"
with sqlite3.connect('library.db') as f:
    cursor = f.cursor()
    cursor.execute(create_query1)
    cursor.executemany(insert_query1,values1)
    cursor.execute(update1)
    data = cursor.execute(display1)
    print(data.fetchall())
    cursor.execute(add0)
    cursor.execute(add10)
    cursor.execute(add20)
    cursor.execute(add30)
    cursor.execute(delete1)