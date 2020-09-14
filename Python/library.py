# itertools
# 数组（列表）全排列、组合实现方法 python —— https://blog.csdn.net/suibianshen2012/article/details/80772905
a = [1,2,3]
b = ['a', 'b', 'c']
for i in range(1, len(a) + 1):
    iter1 = itertools.combinations(a, i)
    iter2 = itertools.combinations(b, i)
    print(list(iter1))
    print(list(iter2))