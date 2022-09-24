from collections import OrderedDict

print("Este é um dicionário:")
dic = dict()

dic['a'] = 1
dic['b'] = 2
dic['c'] = 3
dic['d'] = 4

for key, value in dic.items():
    print(key, '-', value)
print(dic)

print("Este é um dicionário ordenado:")
dic2 = OrderedDict()

dic2['a'] = 1
dic2['b'] = 2
dic2['c'] = 3
dic2['d'] = 4

for key, value in dic2.items():
    print(key, '-', value)
print(dic2)