import matplotlib.pyplot as plt

x = [0, 1.5, 3, 0.75, 2.25, 3.75, 1.5]
y = [0, 0, 0, 1.3, 1.3, 1.3, 2.6]

f = ['F1', 'F2', 'F3', 'F3', 'F1', 'F2', 'F2']

for i in range(7):
    plt.scatter(x[i], y[i], s=23000, marker='h')
    plt.text(x[i], y[i], f[i], ha='center', va='center')

plt.title("Frequency Reuse")
plt.axis('equal')
plt.axis('off')
plt.show()
