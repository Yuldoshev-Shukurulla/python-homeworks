# ### Homework: Pandas Basics
import os
os.chdir('D:\MAAB\python-homeworks\lesson-16')
# #### Part 1: Reading Files  
# 1. **`chinook.db`**  
#    - Use the `sqlite3` library to connect to the database.  
#    - Read the `customers` table into a pandas DataFrame. Display the first 10 rows.  
import pandas as pd
import sqlite3
with sqlite3.connect('data/chinook.db') as connection:
    df_customers = pd.read_sql(
        "SELECT * FROM customers",
        con= connection
    )
print(df_customers.head(10))
# 2. **`iris.json`**  
#    - Load the JSON file into a DataFrame. Show the shape of the dataset and the column names.  
df_iris = pd.read_json('data/iris.json')
print(df_iris.shape)

# 3. **`titanic.xlsx`**  
#    - Load the Excel file into a DataFrame. Use `head` to display the first 5 rows.  
df_titanic = pd.read_excel('data/titanic.xlsx')
print(df_titanic.head())

# 4. **Flights parquet file**  
#    - Read the Parquet file into a DataFrame and use `info` to summarize it.  
flights = pd.read_parquet('data/flights')
flights.info()
# 5. **`movie.csv`**  
#    - Load the CSV file into a DataFrame and display a random sample of 10 rows.
df_movie = pd.read_csv('data/movie.csv')
print(df_employee.sample(10))
# ---

# #### Part 2: Exploring DataFrames  
# 1. Using the DataFrame from **`iris.json`**:  
#    - Rename the columns to lowercase.  
#    - Select only the `sepal_length` and `sepal_width` columns.  
df_iris.columns = [column.lower() for column in df_iris.columns]
print(df_iris[['sepallength', 'sepalwidth']]))
# 2. From the **`titanic.xlsx`** DataFrame:  
#    - Filter rows where the age of passengers is above 30.  
   - Count the number of male and female passengers (`value_counts`).  
above30 = df_titanic[df_titanic['Age'] > 30]
gender_counts = df_titanic['Sex'].value_counts()
print(above30)
print(gender_counts )
# 3. From the **Flights parquet file**:  
#    - Extract and print only the `origin`, `dest`, and `carrier` columns.  
#    - Find the number of unique destinations.
print(flights[['Origin', 'Dest', 'Carrier']])
unique_dest_count = flights['Dest'].nunique()
print(f"Takrorlanmas (unikal) yo'nalishlar soni: {unique_dest_count}")
# 4. From the **`movie.csv`** file:  
#    - Filter rows where `duration` is greater than 120 minutes.  
#    - Sort the filtered DataFrame by `director_facebook_likes` in descending order.  
filtered = df_movie[df_movie['duration'] > 120]
print(filtered.sort_values(by=['director_facebook_likes'], ascending=False))
# ---

# #### Part 3: Challenges and Explorations  
 
# - From **`iris.json`**: Calculate the mean, median, and standard deviation for each numerical column.  
print(df_iris.select_dtypes(include='number').agg(['mean', 'median', 'std']))

# - From **`titanic.xlsx`**: Find the minimum, maximum, and sum of passenger ages.  
min_age = df_titanic['Age'].min()
max_age = df_titanic['Age'].max()
sum_ages = df_titanic['Age'].sum()
print("--- Titanic Yo'lovchilar Yoshlari ---")
print(f"Minimal yosh:      {min_age}")
print(f"Maksimal yosh:     {max_age}")
print(f"Yoshlar yig'indisi: {sum_ages}")
# - From **`movie.csv`**:  
#     - Identify the director with the highest total `director_facebook_likes`.  
#     - Find the 5 longest movies and their respective directors. 
director_likes = df_movie.groupby('director_name')['director_facebook_likes'].sum()

best_director = director_likes.idxmax()
max_likes = director_likes.max()

print(f"Eng ko'p layk olgan rejissyor: {best_director} ({int(max_likes)} layk)")
print("-" * 60)

# - From **Flights parquet file**:  
#     - Check for missing values in the dataset. Fill missing values in a numerical column with the column’s mean.
print("Har bir ustundagi bo'sh qiymatlar soni:")
print(flights.isnull().sum())
print("-" * 60)

dep_delay_mean = flights['DepDelay'].mean()

flights['DepDelay'] = flights['DepDelay'].fillna(dep_delay_mean)

print(f"DepDelay ustunidagi bo'sh qiymatlar ustun o'rtachasi ({dep_delay_mean:.2f}) bilan to'ldirildi.")