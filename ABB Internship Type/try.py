import numpy as np


scores = [0.9,0.10,0.5]

scores2 = np.array(scores)

scores3 = np.argsort(scores2)
print(scores3)

scores4 = np.argsort(scores2)[::-1]
print(scores4)
