import matplotlib.pyplot as plt     
import random as rnd

x = [0]
y = [0]

for i in range(1, 1000000):
    random_number = rnd.random()

    if random_number < 0.02:
        x.append(0)
        y.append(0.16 * y[i - 1])
    elif random_number < 0.86:
        x.append(0.85 * x[i - 1] + 0.04 * y[i - 1])
        y.append(-0.04 * x[i - 1] + 0.85 * y[i - 1] + 1.6)
    elif random_number < 0.93:
        x.append(0.2 * x[i - 1] - 0.26 * y[i - 1])
        y.append(0.23 * x[i - 1] + 0.22 * y[i - 1] + 1.6)
    else:
        x.append(-0.15 * x[i - 1] + 0.28 * y[i - 1])
        y.append(0.26 * x[i - 1] + 0.24 * y[i - 1] + 0.44)

plt.figure(figsize=(8, 12))  # zmiana wielkości wykresu dla lepszego widoku
plt.plot(x, y, ',', color='green')  # zmiana koloru na zielony
plt.show()
