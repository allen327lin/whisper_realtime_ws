# import time
# while 1:
#     print(str(int(time.time()*100)))

# path = 'asd/'
# if path[-1:] != '/':
#     path = path + '/'
# print(path)

import numpy as np

a = [1]
b = [2]
c = [3]
d = [[[1,2]],[[3,4]],[[5,6]]]

print(np.concatenate(d, axis=0))

