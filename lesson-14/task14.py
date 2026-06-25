# Task 1. Write a Python function that converts a temperature from Fahrenheit to Celsius. Use `numpy.vectorize` to apply this function to an array of temperatures: `[32, 68, 100, 212, 77]`. 
#    - Formula: $C = (F - 32) \times \frac{5}{9}$
import numpy as np
@np.vectorize
def far_to_cel(a):
    return (a-32)* 5 / 9
a = np.array([32, 68, 100, 212, 77])
print(far_to_cel(a))
# ---

# Task 2. Create a custom function that takes two arguments: a number and a power. Use `numpy.vectorize` to calculate the power for each pair of numbers in two arrays: `[2, 3, 4, 5]` and `[1, 2, 3, 4]`.
@np.vectorize
def power(a, b):
    return a**b
b = np.array([2, 3, 4, 5])
c = np.array([1, 2, 3, 4])
print(power(b, 3))
print(power(c, 2))
# ---

# Task 3. Solve the system of equations using `numpy`:


# 4x + 5y + 6z = 7 
# 3x - y + z = 4 
# 2x + y - 2z = 5
d = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1 ,-2]
])
e = np.array([7, 4, 5])
f = np.linalg.solve(d, e)
print(f)

# ---

# Task 4. Given the electrical circuit equations below, solve for $I_1, I_2, I_3$ (currents in the branches):

# $$
# \begin{cases}
# 10I_1 - 2I_2 + 3I_3 = 12 \\
# -2I_1 + 8I_2 - I_3 = -5 \\
# 3I_1 - I_2 + 6I_3 = 15
# \end{cases}
# $$

g = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])
h = np.array([12, -5, 15])
i = np.linalg.solve(g, h)
print(i)

# ---

# **Image Manipulation with NumPy and PIL**

# Image file: `images/birds.jpg`. Your task is to perform the following image manipulations using the **NumPy** library while leveraging **PIL** for reading and saving the image.

# **Instructions:**
from PIL import Image
# 1. **Flip the Image**:
#    - Flip the image horizontally and vertically (left-to-right and up-to-down).
def flip(a):
    return a[::-1, ::-1, :]
# 2. **Add Random Noise**:
#    - Add random noise to the image.
def add_noise(a, max_noise=15):
    noise = np.random.normal(0, max_noise, a.shape)
    noisy_image =a + noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)
    
# 3. **Brighten Channels**:
#    - Increase the brightness of the channels (r.g. red channel) by a fixed value (e.g., 40). Clip the values to ensure they stay within the 0 to 255 range.
def brighten(a, chanel = 0, value=40):
        red = a[:, :, chanel].astype(np.float64)
        new = red + value
        a[:, :, chanel] = np.clip(new, 0, 255).astype(np.uint8)
        return a
    
# 4. **Apply a Mask**:
#    - Mask a rectangular region in the image (e.g., a 100x100 area in the center) by setting all pixel values in this region to black (0, 0, 0).
def mask(a):
    h, w, c =a.shape
    c_y = h//2
    c_x = w//2
    start_y = c_y-50
    end_y = c_y+50
    start_x = c_x-50
    end_x = c_x+50
    a[start_y:end_y, start_x:end_x] = 0
    return a


def save_img(arr, name, mode='RGB'):
    img = Image.fromarray(arr, mode)
    img.save(f'{name}.jpg')
# **Requirements:**
# - Use the **PIL** module onyl to:
#   - Read the image.
#   - Convert numpy array to image.
#   - Save the modified image back to a file.
# - Perform all manipulations using NumPy functions. Avoid using image editing functions from PIL or other libraries.
with Image.open('birds.jpg') as img:
    img_arr = np.array(img)
save_img(flip(img_arr), 'flipped') 
save_img(add_noise(img_arr, 50), 'noisy') 
save_img(brighten(img_arr), 'reddy') 
save_img(mask(img_arr), 'masked') 




# **Bonus Challenge**:
# - Create a function for each manipulation (e.g., `flip_image`, `add_noise`, `brighten_channels`, `apply_mask`) to promote modularity and reusability of code.

# ---