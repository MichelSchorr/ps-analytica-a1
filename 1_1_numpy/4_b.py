import numpy as np
import math

arr = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])


#media
count = 0
media = 0
for value in arr:
    count += 1
    media +=  value

media = media/count


#desvio padrao
desvio_padrao = 0
for value in arr:
    desvio_padrao += (value - media)**2

desvio_padrao = desvio_padrao/count
desvio_padrao = math.sqrt(desvio_padrao)

print(desvio_padrao)