

from ump import *


a = ump('/Users/Yuriy_IT/Documents')
# print(a)

print(a['multi_path'])

b = level(a['multi_path'], a['project_name'])
print(b)
print(b['project_1']['name'])

print(b['project_1']['family_4']['name'])

