import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)

plt.scatter(x, y)
plt.title('wykres punktowy')
plt.xlabel('Wartości X')
plt.ylabel('Wartości Y')

plt.show()