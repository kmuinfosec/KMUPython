import time
import random

low = 0
high = 1000000

iter = 100000
a = []
for i in range(iter):
    a.append(random.randint(low, high))

start = time.time()
a.sort()
end = time.time()
print("Running sort(%d) takes %s" %(iter, end - start))
