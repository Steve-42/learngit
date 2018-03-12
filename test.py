import numpy as np

s = np.random.hypergeometric(100,2,10,10000)
print (sum(s<=9)/10000)
