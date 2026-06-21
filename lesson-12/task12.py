# ### Task 1

# Scrape weather information from an HTML file and process it using Python and BeautifulSoup.

# <h4>5-Day Weather Forecast</h4>
# <table>
#     <thead>
#         <tr>
#             <th>Day</th>
#             <th>Temperature</th>
#             <th>Condition</th>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td>Monday</td>
#             <td>25°C</td>
#             <td>Sunny</td>
#         </tr>
#         <tr>
#             <td>Tuesday</td>
#             <td>22°C</td>
#             <td>Cloudy</td>
#         </tr>
#         <tr>
#             <td>Wednesday</td>
#             <td>18°C</td>
#             <td>Rainy</td>
#         </tr>
#         <tr>
#             <td>Thursday</td>
#             <td>20°C</td>
#             <td>Partly Cloudy</td>
#         </tr>
#         <tr>
#             <td>Friday</td>
#             <td>30°C</td>
#             <td>Sunny</td>
#         </tr>
#     </tbody>
# </table>


# Assume you are given the following HTML structure (you can save it as `weather.html`):

# html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Weather Forecast</title>
# </head>
# <body>
#     <h4>5-Day Weather Forecast</h4>
#     <table>
#         <thead>
#             <tr>
#                 <th>Day</th>
#                 <th>Temperature</th>
#                 <th>Condition</th>
#             </tr>
#         </thead>
#         <tbody>
#             <tr>
#                 <td>Monday</td>
#                 <td>25°C</td>
#                 <td>Sunny</td>
#             </tr>
#             <tr>
#                 <td>Tuesday</td>
#                 <td>22°C</td>
#                 <td>Cloudy</td>
#             </tr>
#             <tr>
#                 <td>Wednesday</td>
#                 <td>18°C</td>
#                 <td>Rainy</td>
#             </tr>
#             <tr>
#                 <td>Thursday</td>
#                 <td>20°C</td>
#                 <td>Partly Cloudy</td>
#             </tr>
#             <tr>
#                 <td>Friday</td>
#                 <td>30°C</td>
#                 <td>Sunny</td>
#             </tr>
#         </tbody>
#     </table>

# </body>
# </html>


# 1. **Parse the HTML File**:
#    - Load the `weather.html` file using BeautifulSoup and extract the weather forecast details.

# 2. **Display Weather Data**:
#    - Print the **day**, **temperature**, and **condition** for each entry in the forecast.

# 3. **Find Specific Data**:
#    - Identify and print the day(s) with:
#      - The highest temperature.
#      - The "Sunny" condition.

# 4. **Calculate Average Temperature**:
#    - Compute and print the **average temperature** for the week.

from bs4 import BeautifulSoup

with open('weather.html', 'r', encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')
sections = soup.find_all('td')

weather = {}
i = 0
while i < len(sections):
    weather[sections[i].text.strip()] = [int(sections[i+1].text.strip()[:2]), sections[i+2].text.strip()]
    i += 3

print(f"{'Day':<12} | {'Temperature':<14} | {'Condition':<15}")
print('-'*48)
for i in weather.keys():
    print(f"{i:<12} | {f'{weather[i][0]}°C':<14} | {weather[i][1]:<15}")
maxtemp = max(weather, key=lambda k: weather[k][0])
print(f'Highest temperature is in {maxtemp} with {weather[maxtemp][0]}°C.')
sunny = ', '.join(k for k in weather.keys() if weather[k][1] == 'Sunny')
print(f'Days with sunny weather condition is: {sunny}')
avg = sum(k[0] for k in weather.values())/len(weather.keys())
print(f'Average temperature is: {avg}°C')



# ---

# ### Task 2

# Scrape job listings from the website https://realpython.github.io/fake-jobs and store the data into an SQLite database.

# 1. **Scraping Requirements**:
#    - Extract the following details for each job listing:
#      - **Job Title**
#      - **Company Name**
#      - **Location**
#      - **Job Description**
#      - **Application Link**
# 2. **Data Storage**:
#    - Store the scraped data into an SQLite database in a table named `jobs`.

# 3. **Incremental Load**:
#    - Ensure that your script performs **incremental loading**:
#      - Scrape the webpage and add only **new job listings** to the database.
#      - Avoid duplicating entries. Use `Job Title`, `Company Name`, and `Location` as unique identifiers for comparison.

# 4. **Update Tracking**:
#    - Add functionality to detect if an existing job listing has been updated (e.g., description or application link changes) and update the database record accordingly.

# 5. **Filtering and Exporting**:
#    - Allow filtering job listings by **location** or **company name**.
#    - Write a function to export filtered results into a CSV file.

import sqlite3
from bs4 import BeautifulSoup
import requests
import csv

url = 'https://realpython.github.io/fake-jobs'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

jobs = soup.find_all('h2', class_='title')
companies = soup.find_all('h3', class_='company')
locations = soup.find_all('p', class_='location')
apply_links = soup.find_all('a', string='Apply')
descriptions = []
for i in range(len(jobs)):
    description_url  = apply_links[i]['href']
    result = requests.get(description_url)
    job_soup = BeautifulSoup(result.content, 'html.parser')
    content_div = job_soup.find('div', class_='content')
    if content_div:
        desc = content_div.find('p')
        descriptions.append(desc.text.strip())
    else:
        descriptions.append("Description not found")

create = """CREATE TABLE IF NOT EXISTS Jobs(
Job_title TEXT, 
Company_name TEXT, 
Location TEXT, 
Job_Description TEXT, 
Application_link TEXT,
UNIQUE(Job_title, Company_name, Location))"""
add_data = """INSERT INTO Jobs (
Job_title, Company_name, Location, Job_Description, Application_link)
VALUES (?, ?, ?, ?, ?)
ON CONFLICT(Job_title, Company_name, Location) 
DO UPDATE SET 
    Job_Description = excluded.Job_Description,
    Application_link = excluded.Application_link;"""
with sqlite3.connect('Jobs.db') as f:
    cursor = f.cursor()
    cursor.execute(create)
    for i in range(len(jobs)):
        values = (jobs[i].text.strip(), companies[i].text.strip(), locations[i].text.strip(), descriptions[i], apply_links[i]['href'])
        cursor.execute(add_data, values)

def export_jobs_to_csv(filename = 'filtered_jobs.csv', location = None, company = None):
    with sqlite3.connect('Jobs.db') as f:
        cursor = f.cursor()

        query = "SELECT * FROM Jobs WHERE 1=1 "
        params = []
        if location:
            query += "AND Location LIKE ?"
            params.append(f'%{location}%') 
        if location:
            query += "AND Location LIKE ?"
            params.append(f'%{location}%') 
        if company:
            query += "AND Company_name LIKE ?"
            params.append(f'%{company}%')

        cursor.execute(query, params)
        rows = cursor.fetchall()
        if not rows:
            print('No such jobs found.')
            return
        headers = ['Job_title', 'Company_name', 'Location', 'Job_Description', 'Application_link']
        with open(filename, 'w', newline='', encoding='utf-8') as cf:
            writer = csv.writer(cf)
            writer.writerow(headers)
            for row in rows:
                writer.writerow(row)
        print(f'Filtred result added to {filename} succesfully.')
export_jobs_to_csv(location='Stewartbury, AA') 


# ### Task 3

# You are tasked with scraping laptop data from the "Laptops" section of the [Demoblaze website](https://www.demoblaze.com/) and storing the extracted information in JSON format.

# **Steps:**

# 1. **Navigate to the Website:**
#    - Visit the [Demoblaze homepage](https://www.demoblaze.com/).
#    - Click on the **Laptops** section to view the list of available laptops.

# 2. **Navigate to the Next Page:**
#    - After reaching the Laptops section, locate and click the **Next** button to navigate to the next page of laptop listings.

# 3. **Data to Scrape:**
#    For each laptop on the page, scrape the following details:
#    - **Laptop Name**
#    - **Price**
#    - **Description**

# 4. **Data Storage:**
#    - Save the extracted information in a structured **JSON format** with fields like:
#      json
#      [
#        {
#          "name": "Laptop Name",
#          "price": "Laptop Price",
#          "description": "Laptop Description"
#        },
#        ...
#      ]


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.demoblaze.com')
laptop = driver.find_element(By.LINK_TEXT, 'Laptops')
laptop.click()
time.sleep(3)
next_button = driver.find_element(By.ID, 'next2')
next_button.click()

cards = driver.find_elements(By.CLASS_NAME, 'card-block')


laptops_list = []
for card in cards:
    name = card.find_element(By.CLASS_NAME, 'card-title').text.strip()
    price = card.find_element(By.TAG_NAME, 'h5').text.strip()
    description = card.find_element(By.ID, 'article').text.strip()
    
    laptop_data = {
        "name": name,
        "price": price,
        "description": description.replace('\n', ' ')
        }
    
    laptops_list.append(laptop_data)

with open('laptops.json', mode='w', encoding='utf-8') as json_file:
    json.dump(laptops_list, json_file, indent=4, ensure_ascii=False)

driver.quit()