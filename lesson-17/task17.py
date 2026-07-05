# #### **Merging and Joining**
# 1. **Inner Join on Chinook Database**
#    - Load the `chinook.db` database.
#    - Perform an inner join between the `customers` and `invoices` tables on the `CustomerId` column.
#    - Find the total number of invoices for each customer.

import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')
customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
conn.close()

merged_inner = pd.merge(customers, invoices, on='CustomerId', how='inner')

invoice_counts = merged_inner.groupby(['CustomerId', 'FirstName', 'LastName']).size().reset_index(name='TotalInvoices')
print("Inner Join natijasi (Mijozlar invoice soni):\n", invoice_counts.head())


# 2. **Outer Join on Movie Data**
#    - Load the `movie.csv` file.
#    - Create two smaller DataFrames:
#      - One with only `director_name` and `color`.
#      - Another with `director_name` and `num_critic_for_reviews`.
#    - Perform a left join and then a full outer join on `director_name`.
#    - Count how many rows are in the resulting DataFrames for each join type.
movie_df = pd.read_csv('movie.csv')

df_color = movie_df[['director_name', 'color']]
df_reviews = movie_df[['director_name', 'num_critic_for_reviews']]

left_joined = pd.merge(df_color, df_reviews, on='director_name', how='left')
print(f"Left Join qatorlar soni: {len(left_joined)}")

outer_joined = pd.merge(df_color, df_reviews, on='director_name', how='outer')
print(f"Full Outer Join qatorlar soni: {len(outer_joined)}")


# ---

# #### **Grouping and Aggregating**
# 1. **Grouped Aggregations on Titanic**
#    - Group passengers by `Pclass` and calculate the following:
#      - Average age.
#      - Total fare.
#      - Count of passengers.
#    - Save the results to a new DataFrame.
titanic_df = pd.read_csv('titanic.csv')  

titanic_agg = titanic_df.groupby('Pclass').agg(
    Average_Age=('Age', 'mean'),
    Total_Fare=('Fare', 'sum'),
    Passenger_Count=('PassengerId', 'count') 
).reset_index()

print("Titanic guruhlash natijasi:\n", titanic_agg)


# 2. **Multi-level Grouping on Movie Data**
#    - Group the movies by `color` and `director_name`.
#    - Find:
#      - Total `num_critic_for_reviews` for each group.
#      - Average `duration` for each group.
movie_grouped = movie_df.groupby(['color', 'director_name']).agg(
    Total_Critics=('num_critic_for_reviews', 'sum'),
    Average_Duration=('duration', 'mean')
).reset_index()

print("Movie ko'p darajali guruhlash:\n", movie_grouped.head())


# 3. **Nested Grouping on Flights**
#    - Group flights by `Year` and `Month` and calculate:
#      - Total number of flights.
#      - Average arrival delay (`ArrDelay`).
#      - Maximum departure delay (`DepDelay`).

flights_df = pd.read_csv('flights.csv')

flights_grouped = flights_df.groupby(['Year', 'Month']).agg(
    Total_Flights=('Year', 'count'),
    Avg_ArrDelay=('ArrDelay', 'mean'),
    Max_DepDelay=('DepDelay', 'max')
).reset_index()

print("Parvozlar guruhlash natijasi:\n", flights_grouped.head())


# ---

# #### **Applying Functions**
# 1. **Apply a Custom Function on Titanic**
#    - Write a function to classify passengers as `Child` (age < 18) or `Adult`.
#    - Use `apply` to create a new column, `Age_Group`, with these values.
def classify_age(age):
    if pd.isna(age):
        return 'Unknown'
    return 'Child' if age < 18 else 'Adult'

titanic_df['Age_Group'] = titanic_df['Age'].apply(classify_age)
print(titanic_df[['Age', 'Age_Group']].head())


# 2. **Normalize Employee Salaries**
#    - Load the `employee.csv` file.
#    - Normalize the salaries within each department.
employee_df = pd.read_csv('employee.csv')

# Har bir departament ichida maoshlarni min-max normallash funksiyasi
def normalize_salary(group):
    min_val = group.min()
    max_val = group.max()
    if min_val == max_val:  # Agar departamentda 1 ta xodim bo'lsa yoki hamma maosh teng bo'lsa
        return 1.0
    return (group - min_val) / (max_val - min_val)

employee_df['Normalized_Salary'] = employee_df.groupby('department')['salary'].transform(normalize_salary)
print(employee_df[['department', 'salary', 'Normalized_Salary']].head())


# 3. **Custom Function on Movies**
#    - Write a function that returns `Short`, `Medium`, or `Long` based on the duration of a movie:
#      - `Short`: Less than 60 minutes.
#      - `Medium`: Between 60 and 120 minutes.
#      - `Long`: More than 120 minutes.
#    - Apply this function to classify movies in the `movie.csv` dataset.
def classify_duration(duration):
    if pd.isna(duration):
        return 'Unknown'
    if duration < 60:
        return 'Short'
    elif 60 <= duration <= 120:
        return 'Medium'
    else:
        return 'Long'

movie_df['Duration_Class'] = movie_df['duration'].apply(classify_duration)
print(movie_df[['duration', 'Duration_Class']].head())
# ---

# #### **Using `pipe`**
# 1. **Pipeline on Titanic**
#    - Create a pipeline to:
#      - Filter passengers who survived (`Survived == 1`).
#      - Fill missing `Age` values with the mean.
#      - Create a new column, `Fare_Per_Age`, by dividing `Fare` by `Age`.
def filter_survived(df):
    return df[df['Survived'] == 1]

def fill_missing_age(df):
    
    df = df.copy()
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df

def add_fare_per_age(df):
    df = df.copy()
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df

titanic_piped = (titanic_df
                 .pipe(filter_survived)
                 .pipe(fill_missing_age)
                 .pipe(add_fare_per_age))

print("Titanic Pipeline natijasi:\n", titanic_piped[['Survived', 'Age', 'Fare', 'Fare_Per_Age']].head())


# 2. **Pipeline on Flights**
#    - Create a pipeline to:
#      - Filter flights with a departure delay greater than 30 minutes.
#      - Add a column `Delay_Per_Hour` by dividing the delay by the scheduled flight duration.

def filter_delays(df):
    return df[df['DepDelay'] > 30]

def add_delay_per_hour(df):
    df = df.copy()
    df['Delay_Per_Hour'] = df['DepDelay'] / (df['AirTime'] / 60)
    return df

flights_piped = (flights_df
                 .pipe(filter_delays)
                 .pipe(add_delay_per_hour))

print("Flights Pipeline natijasi:\n", flights_piped[['DepDelay', 'AirTime', 'Delay_Per_Hour']].head())