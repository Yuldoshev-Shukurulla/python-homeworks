# 1. Max score = 10
# Berilgan butun son n.
# Agar son palindrome bo‘lsa True, aks holda False qaytarsin.


# n = input('Enter a number: ')
# a = True if str(n)[::-1] == str(n) else False
# print(a)

# Input: 121
# Output: True

# Input: 1231
# Output: False


# 2. Max score = 15
# Berilgan string s.
# Qavslar to‘g‘ri yopilganligini tekshiring.


# To`g`ri yopilish: ()  {}  []

# Input: "()[]{}"
# Output: True

# Input: "(]"
# Output: False

def isValid(s: str) ->  bool:
    Parentheses = {")": "(", "}": "{", "]": "["}
    stack = []
    for i in s:
        if i in Parentheses.keys() or i in Parentheses.values():
            if i in Parentheses:
                top_element = stack.pop() if stack else '#'
                if Parentheses[i] != top_element:
                    return False
            else:
                stack.append(i)
        else: continue
    return len(stack) == 0
n1 = str(input('Enter parenthesis: '))
print(isValid(n1))

# 3. Max score = 15
# Berilgan butun sonlardan iborat list nums va butun son k.
# listni o‘ng tomonga k marta aylantiring.

# O‘ng tomonga aylantirish degani:
# listning oxiridagi element(lar) list boshiga o‘tkaziladi qolgan elementlar o‘ngga siljiydi.

# ⚠️ Muhim:
# k list uzunligidan katta bo‘lishi mumkin.

# Input:
# nums = [1,2,3,4,5,6,7]
# k = 3

# Output:
# [5,6,7,1,2,3,4]

# Input:
# nums = [10,20,30,40]
# k = 1

# Output:
# [40,10,20,30]
n = [1,2,3,4,5,6,7]
k = 3
while k>len(n):
    k-=len(n)
a = []
for i in range(len(n)):
    a.append(n[i-k])
print(a)


# 4. Max score = 20
# Python (Pandas) yordamida muzlatkichdagi ingredientlar bilan to‘liq tayyorlash mumkin bo‘lgan barcha taomlarni aniqlang.
#    Agar biror taom uchun kerakli ingredientlardan bittasi ham yetishmasa, u taom natijaga kiritilmasin.
import pandas as pd
recipe = pd.DataFrame({
    "recipe_name": ["hotdog","hotdog","pilov","pilov","pilov","pizza","pizza","pizza"],
    "ingredient_id": [1,2,3,4,5,6,7,8],
    "ingredient_name": ["sausage","bread","rice","carrot","meat","flour","tomato","cheese"]
})

fridge = pd.DataFrame({
    "ingredient_id": [1,2,3,4,6],
    "ingredient_name": ["sausage","bread","rice","carrot","flour"]
})
result = pd.merge(recipe, fridge, on='ingredient_id', how="left")
dishes_withnan = result[result['ingredient_name_y'].isna()]['recipe_name'].unique()
clean_dishes = result[~result['recipe_name'].isin(dishes_withnan)]['recipe_name'].unique()
print(clean_dishes)


# Expected output: [hotdog]



# task 5. Max score = 25

#  You have a dataset (customer_orders.csv) containing information about customer orders. The dataset has the following columns:

#  OrderID: Unique identifier for each order.
#  CustomerID: Unique identifier for each customer.
#  Product: Name of the product ordered.
#  Quantity: Number of units ordered.
#  Price: Price per unit.

#  Tasks:

#  1)Group the data by CustomerID and filter out customers who have made less than 20 orders.
#  2)Identify customers who have ordered products with an average price per unit greater than $120.
#   
import os
os.chdir("C:\\a62ab832e6d116c5594b4b3659421f\sh\python-homeworks\exam")
import pandas as pd
df = pd.read_csv('customer_orders.csv')
result = (
    df
    .groupby('CustomerID')
    .agg({'Price' : ['count']})
)
result.columns = ['PriceCount']
print(result[result['PriceCount']>=20])
df['Price_per_unit'] = df.apply(lambda x: x['Price'] / x['Quantity'], axis=1)
result2 = (
    df
    .groupby('CustomerID')
    .agg({
        'Price_per_unit' : ['mean']
    })
)
result2.columns = ['PriceCount']
print(result2[result2['PriceCount']>120])