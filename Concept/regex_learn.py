import re
xx = "guru9,e9ucation is fu9n"
indices_object = re.finditer(pattern='9', string=xx)
print(indices_object)
# for i in indices_object:
#     print(i.start())
indices = [index.start() for index in indices_object]
print(indices)







# import numpy as np
# lst = np.asarray([0,0,0,0,0])
# lst[[2,4]]=99
# print(lst)