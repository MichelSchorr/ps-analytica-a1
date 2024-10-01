import numpy as np

arr = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])


count = 0
media = 0
for value in arr:
    count += 1
    media +=  value

media = media/count

print(media)