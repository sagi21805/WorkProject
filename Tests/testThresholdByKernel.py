import numpy as np

def test(stop):
    i=0
    while i < stop:
        yield i 
        i+=1

for i in range(10):
    print(test(10))
