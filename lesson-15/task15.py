# #### **1. Basic Plotting**
# - **Task**: Plot the function $ f(x) = x^2 - 4x + 4 $ for $ x $ values between -10 and 10. Customize the plot with appropriate labels for the axes and a title.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 10000)
def func1(x):
    return x ** 2 -4 * x + 4
y = func1(x)
plt.plot(x, y, label = '$f(x) = x^2 - 4x + 4$')
plt.title('Parabola')
plt.xlabel('X')
plt.ylabel('Y', rotation = 0)
plt.legend()
plt.show()




# ---

# #### **2. Sine and Cosine Plot**
# - **Task**: Plot $ \sin(x) $ and $ \cos(x) $ on the same graph for $ x $ values ranging from 0 to $ 2\pi $. Use different line styles, markers, and colors to distinguish between the two functions. Add a legend.
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, 'b-', label = '$f(x) = sin(x)$')
plt.plot(x, y2, 'r--^', label = '$f(x) = cos(x)$')
plt.xlabel('X')
plt.ylabel('Y', rotation = 0)
plt.legend()
plt.show()

# ---


# #### **3. Subplots**
# - **Task**: Create a 2x2 grid of subplots. In each subplot, plot:
#   - Top-left: $ f(x) = x^3 $
#   - Top-right: $ f(x) = \sin(x) $
#   - Bottom-left: $ f(x) = e^x $
#   - Bottom-right: $ f(x) = \log(x+1) $ (for $ x \geq 0 $)

#   Customize each plot with titles, axis labels, and different colors.
x1 = np.linspace(-10, 10, 1000)
y1 = x1 ** 3
x2 = np.linspace(- 2 * np.pi, 2 * np.pi, 1000)
y2 = np.sin(x2)
x3 = np.linspace(-10, 10, 1000)
y3 = np.e ** x3
x4 = np.linspace(0, 10, 1000)
y4 = np.log(x4 + 1)
plt.subplot(2, 2, 1)
plt.plot(x1, y1, 'r')
plt.title('$ f(x) = x^3 $')
plt.xlabel('X')
plt.ylabel('Y', rotation = 0)

plt.subplot(2, 2, 2)
plt.plot(x2, y2, 'y')
plt.title('$ f(x) = \sin(x) $')
plt.xlabel('X')
plt.ylabel('Y', rotation = 0)

plt.subplot(2, 2, 3)
plt.plot(x3, y3, 'g')
plt.title('$ f(x) = e^x $')
plt.xlabel('X')
plt.ylabel('Y', rotation = 0)

plt.subplot(2, 2, 4)
plt.plot(x4, y4, 'k')
plt.title('$ f(x) = \log(x+1) $ (for $ x \geq 0 $')
plt.xlabel('X')
plt.ylabel('Y', rotation = 0)

plt.show()



# ---

# #### **4. Scatter Plot**
# - **Task**: Create a scatter plot of 100 random points in a 2D space. The x and y values should be randomly generated from a uniform distribution between 0 and 10. Use different colors and markers for the points. Add a title, axis labels, and a grid.
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.scatter(x, y, c = x * y, cmap = 'cool', marker= '*')
plt.title('Scatter plot.')
plt.xlabel('X')
plt.ylabel('Y', rotation = 0)
plt.grid(True)
plt.show()

# ---

# #### **5. Histogram**
# - **Task**: Generate a random dataset of 1000 values sampled from a normal distribution (mean=0, std=1). Plot a histogram of the data with 30 bins. Add a title and axis labels. Adjust the transparency of the bars using the `alpha` parameter.
dataset = np.random.normal(loc=0.0, scale=1.0, size=1000)
plt.hist(dataset, bins= 30, color='b', edgecolor = 'r', alpha = 0.8)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# ---

# #### **6. 3D Plotting**
# - **Task**: Create a 3D surface plot for the function $ f(x, y) = \cos(x^2 + y^2) $ over the range of $ x $ and $ y $ values from -5 to 5. Use a suitable colormap and add a colorbar. Set appropriate labels for the axes and title.
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
xx, yy = np.meshgrid(x, y)
zz = np.cos(xx ** 2 + yy ** 2)
plt.figure()
ax = plt.axes(projection = '3d')
surf = ax.plot_surface(xx, yy, zz, cmap='viridis', edgecolor='none')
plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='f(x, y) qiymati')
ax.set_title(r'$f(x, y) = \cos(x^2 + y^2)$ 3D Surface Plot', fontsize=14)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()


# ---

# #### **7. Bar Chart**
# - **Task**: Create a vertical bar chart displaying the sales data for five different products: `['Product A', 'Product B', 'Product C', 'Product D', 'Product E']`. The sales values for each product are `[200, 150, 250, 175, 225]`. Customize the chart with a title, axis labels, and different bar colors.
products = ['A', 'B', 'C', 'D', 'E']
sales = [200, 150, 250, 175, 225]
colors = ['skyblue', 'y', 'g', 'b', 'r']
plt.bar(products, sales, color = colors)
plt.title('Sales Data')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()

# ---

# #### **8. Stacked Bar Chart**
# - **Task**: Create a stacked bar chart that shows the contribution of three different categories (`'Category A'`, `'Category B'`, and `'Category C'`) over four time periods (`'T1'`, `'T2'`, `'T3'`, `'T4'`). Use sample data for each category at each time period. Customize the chart with a title, axis labels, and a legend.

categories = ['A', 'B', 'C']
T1 = np.array([5, 3, 1])
T2 = np.array([2, 5, 4])
T3 = np.array([5, 3, 3])
T4 = np.array([3, 3, 3])

plt.bar(categories, T1, label = '1st time period', color = 'skyblue')
plt.bar(categories, T2, bottom = T1, label = '2nd time period', color = 'r')
plt.bar(categories, T3, bottom = T1 + T2, label = '3rd time period', color = 'g')
plt.bar(categories, T4, bottom = T1 + T2 + T3, label = '4th time period', color = 'b')

plt.title('Stacked Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.show()