a = {'aa': [1,2,3], 'b': 2}

print(a)


b = {f'{key}': [] for key in a.keys()}

print(b)

