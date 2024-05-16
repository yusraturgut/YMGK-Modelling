import numpy as np
import matplotlib.pyplot as plt

def baker_map(x, y):
    if x <= 0.5:
        return 2 * x, y / 2
    else:
        return 2 * x - 1, (y + 1) / 2

# Rastgele başlangıç noktaları oluşturalım
num_points = 1000
iterations = 100

# Rastgele başlangıç noktaları oluştur
initial_points = np.random.rand(num_points, 2)

# İterasyonları gerçekleştir
all_points = []

for x, y in initial_points:
    trajectory = [(x, y)]
    for _ in range(iterations):
        x, y = baker_map(x, y)
        trajectory.append((x, y))
    all_points.extend(trajectory)

# Sonuçları çizelim
x_vals, y_vals = zip(*all_points)

plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, 'bo', markersize=0.5)
plt.title("Baker Map")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
