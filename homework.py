import matplotlib.pyplot as plt
import numpy as np

random_array1 = np.random.rand(5)
print(random_array1)
random_array2 = np.random.rand(5)
print(random_array2)
x = random_array1
y = random_array2
plt.scatter(x,y)
plt.title("Диаграмма рассеяния 2-х наборов случайных чисел")
plt.xlabel("х ось")
plt.ylabel("у ось")
plt.show()


# data = np.random.normal(0, 1, 1000)
# plt.hist(data, bins=3)
# plt.title("Гистограмма случайных чисел")
# plt.xlabel("х ось")
# plt.ylabel("у ось")
# plt.show()

