#!python3

import numpy as np

print("-------------------1-----------------------")
a = np.array([1, 2, 3])
print(a)
print('\n')
a = np.array([[1, 2], [3, 4]])
print(a)
print('\n')
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)
print('\n')
a = np.array([1, 2, 3], dtype=complex)
print(a)
print("-------------------2 data type-----------------------")
dt = np.dtype(np.int32)
print(dt)
print('\n')
dt = np.dtype('i4')
print(dt)
print('\n')
dt = np.dtype('<i4')
print(dt)
print('\n')
dt = np.dtype([('age', np.int8)])
print(dt)
print('\n')
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)
print('\n')
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a['age'])
print('\n')
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
print('\n')
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)
print("-------------------3 data shape-----------------------")
a = np.arange(24)
print(a.ndim)  # a 现只有一个维度
print('\n')
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b.ndim)
print('\n')
a = np.array([[1, 2, 3], [4, 5, 6]])  # 2 rows 3 cols
print(a)
print(a.shape)
print('\n')
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)
print(a)
print('\n')
# 数组的 dtype 为 int8（一个字节）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x)
print(x.itemsize)
print('\n')
# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y)
print(y.itemsize)
print('\n')
x = np.array([1, 2, 3, 4, 5])
print(x.flags)
print("-------------------4 create array-----------------------")
x = np.empty([3, 2], dtype=int)
print(x)
# 默认为浮点数
x = np.zeros(5)
print(x)
print('\n')
# 设置类型为整数
y = np.zeros((5,), dtype=np.int)
print(y)
print('\n')
# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)
print('\n')
# 默认为浮点数
x = np.ones(5)
print(x)
print('\n')
# 自定义类型
x = np.ones([2, 2], dtype=int)
print(x)
print('\n')
x = [1, 2, 3]
a = np.asarray(x)
print(a)
print('\n')
x = (1, 2, 3)
a = np.asarray(x)
print(a)
print('\n')
x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
print(a)
print('\n')
x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)
print('\n')
s = b'Hello World'
a = np.frombuffer(s, dtype='S1')
print(a)
print('\n')
# 使用 range 函数创建列表对象
list = range(5)
it = iter(list)
# 使用迭代器创建 ndarray
x = np.fromiter(it, dtype=float)
print(x)
print('\n')
x = np.arange(5)
print(x)
print('\n')
# 设置了 dtype
x = np.arange(5, dtype=float)
print(x)
print('\n')
x = np.arange(10, 20, 2)
print(x)
print('\n')
a = np.linspace(1, 10, 10)
print(a)
print('\n')
a = np.linspace(1, 1, 10)
print(a)
print('\n')
a = np.linspace(10, 20, 5, endpoint=False)
print(a)
print('\n')
a = np.linspace(1, 10, 10, retstep=True)
print(a)
# 拓展例子
b = np.linspace(1, 10, 10).reshape([10, 1])
print(b)
print('\n')
# 默认底数是 10
a = np.logspace(1.0, 2.0, num=10)
print(a)
print('\n')
a = np.logspace(0, 9, 10, base=2)
print(a)
print("-------------------5 index and slice-----------------------")
a = np.arange(10)
s = slice(2, 7, 2)  # 从索引 2 开始到索引 7 停止，间隔为2
print(a[s])
print('\n')
a = np.arange(10)
b = a[2:7:2]  # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)
print('\n')
a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
b = a[5]
print(b)
print('\n')
a = np.arange(10)
print(a[2:])
print('\n')
a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
print(a[2:5])
print('\n')
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)
# 从某个索引处开始切割
print('从数组索引 a[1:] 处开始切割')
print(a[1:])
print('\n')
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a[..., 1])  # 第2列元素
print(a[1, ...])  # 第2行元素
print(a[..., 1:])  # 第2列及剩下的所有元素

print("-------------------6 advanced index-----------------------")

x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)
print('\n')

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')

rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = a[1:3, 1:3]
c = a[1:3, [1, 2]]
d = a[..., 1:]
print(b)
print(c)
print(d)
print('\n')

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')

# 现在我们会打印出大于 5 的元素
print('大于 5 的元素是：')
print(x[x > 5])
print('\n')

a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])
print('\n')

a = np.array([1, 2 + 6j, 5, 3.5 + 5j])
print(a[np.iscomplex(a)])
print('\n')

x = np.arange(32).reshape((8, 4))
print(x[[4, 2, 1, 7]])
print('\n')

x = np.arange(32).reshape((8, 4))
print(x[[-4, -2, -1, -7]])
print('\n')

x = np.arange(32).reshape((8, 4))
print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
print('\n')
print("-------------------7-----------------------")
print("-------------------8-----------------------")
print("-------------------9-----------------------")
print("-------------------10-----------------------")
print("-------------------11-----------------------")
print("-------------------12-----------------------")
print("-------------------13-----------------------")
print("-------------------14-----------------------")
print("-------------------15-----------------------")
print("-------------------16-----------------------")
print("-------------------17-----------------------")
print("-------------------18-----------------------")
print("-------------------19-----------------------")
print("-------------------20-----------------------")
