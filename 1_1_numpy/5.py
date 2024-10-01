import numpy as np
from numpy import random

import math



arr = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])

#a
arr.sort()
print("a(ordenar): ", arr)

#b
print("b(tamanho): ", arr.shape)

#c
media = arr.mean()
print("c(media): ", media)

#d
max = arr.max()
min = arr.min()
dp = arr.std()
print("d: ")
print("max: ", max)
print("min: ", min)
print("dp: ", dp)


#e
random_array = random.uniform(low=0.0, high=10.0, size=(100))
print("e: ")
print("media: ", random_array.mean())
print("dp: ", random_array.std())
print("max: ", random_array.max())
print("min: ", random_array.min())
