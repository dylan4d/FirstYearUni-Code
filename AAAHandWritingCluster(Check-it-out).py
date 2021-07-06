import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt

from sklearn import datasets
digits = datasets.load_digits()
print(digits.DESCR)
print(digits.data)
print(digits.target)

plt.gray()
plt.matshow(digits.images[100])
plt.show()
print(digits.target[100])

from sklearn.cluster import KMeans
model = KMeans(n_clusters = 10, random_state = 1)
model.fit(digits.data)

fig = plt.figure(figsize = (8, 3))
fig.suptitle('Cluster Center Images')

for i in range(10):
  ax = fig.add_subplot(2, 5, i + 1)

  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap = plt.cm.binary)

plt.show()


new_samples = np.array([
[0.38,7.47,7.26,6.90,7.48,2.75,0.00,0.00,0.53,7.55,5.19,2.03,7.55,4.95,0.00,0.00,0.00,4.36,7.62,7.40,7.09,0.76,0.00,0.00,0.00,1.18,7.24,7.63,7.40,2.59,0.00,0.00,0.00,5.77,7.40,3.13,6.53,7.47,1.22,0.00,0.00,7.62,5.49,0.15,3.34,7.63,2.29,0.00,0.00,5.06,7.63,7.63,7.63,7.02,1.07,0.00,0.00,0.31,3.14,3.85,3.06,0.53,0.00,0.00],
[0.00,3.21,5.80,6.10,6.00,4.30,0.09,0.00,0.00,4.48,6.32,5.18,6.49,7.62,1.92,0.00,0.00,0.00,0.00,3.44,7.40,7.63,1.71,0.00,0.00,0.00,0.00,3.29,6.43,7.62,3.35,0.00,0.00,0.00,1.14,0.36,0.93,7.56,6.03,0.00,0.00,0.00,7.43,7.22,7.40,7.62,4.19,0.00,0.00,0.00,2.29,5.03,4.87,1.92,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.62,5.27,5.34,5.34,4.02,0.00,0.00,0.00,0.62,5.59,6.03,6.80,7.62,0.00,0.00,0.00,0.00,0.00,0.00,4.12,7.62,0.00,0.00,0.00,0.00,2.69,6.49,7.62,6.89,0.00,0.00,0.00,0.00,2.69,5.91,7.22,6.68,0.00,0.00,0.00,2.68,5.34,5.34,6.78,7.62,0.00,0.00,0.00,2.68,5.87,6.03,5.97,3.92,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[2.11,7.62,7.62,7.53,6.86,3.72,0.00,0.00,2.29,7.62,3.29,4.14,4.53,1.89,0.00,0.00,2.29,7.62,6.25,5.19,2.80,0.13,0.00,0.00,0.97,5.05,5.51,7.01,7.63,4.65,0.00,0.00,0.00,0.00,0.00,0.15,5.34,7.63,0.61,0.00,1.20,7.55,5.85,5.72,7.62,6.53,0.31,0.00,0.28,4.40,6.12,6.05,4.17,0.30,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
])

new_labels = model.predict(new_samples)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')
