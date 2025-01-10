import numpy as np
import time

# создание массива с numpy и демострация его преимущества

large_list = list(range(1_000_000))
start = time.time()
result_list = [x * 2 for x in large_list]
print("Время выполнения с использованием списка Python:", time.time() - start)

# numpy
large_array = np.arange(1_000_000)
start = time.time()
result_array = large_array * 2
print("Время выполнения с использованием NumPy:", time.time() - start)