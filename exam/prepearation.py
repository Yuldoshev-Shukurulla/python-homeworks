**1.** Return uncommon elements of lists. Order of elements does not matter.

input:
    list1 = [1, 1, 2]
    list2 = [2, 3, 4]
output: [1, 1, 3, 4]



input:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
output: [1, 2, 3, 4, 5, 6]



input:
    list1 = [1, 1, 2, 3, 4, 2]
    list2 = [1, 3, 4, 5]
output: [2, 2, 5]


**3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.


input: hello
output: hel_lo



input: assalom
output: ass_alom



input: abcabcdabcdeabcdefabcdefg
output: abc_abcd_abcdeab_cdef_abcdefg


**6. Prime Numbers**
Task: Write a Python program that prints all prime numbers between 1 and 100.


## Employee Records Manager (OOP Version)
**Objective**: Create a program to manage employee records using classes and file handling.

### **Tasks and Requirements**

1. **Class Design**  
   - Create a class `Employee` to represent individual employees with the following attributes:
     - `employee_id`
     - `name`
     - `position`
     - `salary`
   - Create a class `EmployeeManager` to handle operations such as adding, viewing, searching, updating, and deleting employee records. This class will manage the file **"employees.txt"**.

2. **File Handling**  
   - All employee records should be stored in **"employees.txt"**.  
   - Each operation (add, view, update, delete) should interact with the file to ensure data persistence.

3. **Menu Options**  
   Implement a menu within the `EmployeeManager` class with the following options:
   

   1. Add new employee record
   2. View all employee records
   3. Search for an employee by Employee ID
   4. Update an employee's information
   5. Delete an employee record
   6. Exit
   


4. **Functional Requirements**  
   - **Option 1**: Add a new employee by creating an `Employee` object and appending it to **"employees.txt"**.  
   - **Option 2**: Read all records from **"employees.txt"** and display them.  
   - **Option 3**: Search for an employee by **Employee ID** and display their details.  
   - **Option 4**: Update an employee's information (name, position, or salary) based on the Employee ID.  
   - **Option 5**: Delete an employee's record from the file using the Employee ID.  
   - **Option 6**: Exit the program.


### **Example Usage**  
plaintext
Welcome to the Employee Records Manager!
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit

Enter your choice: 1
Enter Employee ID: 1001
Enter Name: John Doe
Enter Position: Software Engineer
Enter Salary: 75000
Employee added successfully!

Enter your choice: 2
Employee Records:
1001, John Doe, Software Engineer, 75000

Enter your choice: 3
Enter Employee ID to search: 1001
Employee Found:
1001, John Doe, Software Engineer, 75000

Enter your choice: 6
Goodbye!


### **Additional Instructions**
1. Use the `Employee` class to encapsulate individual employee data and functionality (e.g., a `__str__` method for displaying employee details).  
2. Use the `EmployeeManager` class for managing operations such as file handling, record searching, and updates.  
3. Ensure your code is modular, with methods for each operation (e.g., `add_employee`, `view_all_employees`).  


### **Bonus Challenge**
1. Add validation to ensure unique Employee IDs.  
2. Implement error handling for invalid inputs and file operations.  
3. Allow users to sort employee records (e.g., by salary or name) before displaying them.  



## Task 2: Movie Recommendation System
   1. Use this url https://developer.themoviedb.org/docs/getting-started/ to fetch information about movies.
   2. Create a program that asks users for a movie genre and recommends a random movie from that genre.



Scrape job listings from the website https://realpython.github.io/fake-jobs and store the data into an SQLite database.

1. **Scraping Requirements**:
   - Extract the following details for each job listing:
     - **Job Title**
     - **Company Name**
     - **Location**
     - **Job Description**
     - **Application Link**

2. **Data Storage**:
   - Store the scraped data into an SQLite database in a table named `jobs`.

3. **Incremental Load**:
   - Ensure that your script performs **incremental loading**:
     - Scrape the webpage and add only **new job listings** to the database.
     - Avoid duplicating entries. Use `Job Title`, `Company Name`, and `Location` as unique identifiers for comparison.

4. **Update Tracking**:
   - Add functionality to detect if an existing job listing has been updated (e.g., description or application link changes) and update the database record accordingly.

5. **Filtering and Exporting**:
   - Allow filtering job listings by **location** or **company name**.
   - Write a function to export filtered results into a CSV file.



**Image Manipulation with NumPy and PIL**

Image file: `images/birds.jpg`. Your task is to perform the following image manipulations using the **NumPy** library while leveraging **PIL** for reading and saving the image.

**Instructions:**

1. **Flip the Image**:
   - Flip the image horizontally and vertically (left-to-right and up-to-down).

2. **Add Random Noise**:
   - Add random noise to the image.

3. **Brighten Channels**:
   - Increase the brightness of the channels (r.g. red channel) by a fixed value (e.g., 40). Clip the values to ensure they stay within the 0 to 255 range.

4. **Apply a Mask**:
   - Mask a rectangular region in the image (e.g., a 100x100 area in the center) by setting all pixel values in this region to black (0, 0, 0).

**Requirements:**
- Use the **PIL** module onyl to:
  - Read the image.
  - Convert numpy array to image.
  - Save the modified image back to a file.
- Perform all manipulations using NumPy functions. Avoid using image editing functions from PIL or other libraries.


**Bonus Challenge**:
- Create a function for each manipulation (e.g., `flip_image`, `add_noise`, `brighten_channels`, `apply_mask`) to promote modularity and reusability of code.
   

#### **8. Stacked Bar Chart**
- **Task**: Create a stacked bar chart that shows the contribution of three different categories (`'Category A'`, `'Category B'`, and `'Category C'`) over four time periods (`'T1'`, `'T2'`, `'T3'`, `'T4'`). Use sample data for each category at each time period. Customize the chart with a title, axis labels, and a legend.


#### **6. 3D Plotting**
- **Task**: Create a 3D surface plot for the function $ f(x, y) = \cos(x^2 + y^2) $ over the range of $ x $ and $ y $ values from -5 to 5. Use a suitable colormap and add a colorbar. Set appropriate labels for the axes and title.


1. **Pipeline on Titanic**
   - Create a pipeline to:
     - Filter passengers who survived (`Survived == 1`).
     - Fill missing `Age` values with the mean.
     - Create a new column, `Fare_Per_Age`, by dividing `Fare` by `Age`.

3. **Custom Function on Movies**
   - Write a function that returns `Short`, `Medium`, or `Long` based on the duration of a movie:
     - `Short`: Less than 60 minutes.
     - `Medium`: Between 60 and 120 minutes.
     - `Long`: More than 120 minutes.
   - Apply this function to classify movies in the `movie.csv` dataset.