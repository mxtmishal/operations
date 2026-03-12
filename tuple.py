# immutable
# heterogenous
# 
# allow duplicates
# indexed
# ordered

#                          -4  -3 -2 -1
my_tuple1 = (12,65,98,12,96,87,12,56,12)
my_tuple2 = 45,64,34,78
# my_tuple1[1] = 96 #error
print(my_tuple1[1])
# print(type(my_tuple2))
print(len(my_tuple1))

print(my_tuple1.count(12))
print(my_tuple1.index(56))
print(my_tuple1[2:6])
print(my_tuple1[-4:-1])

my_list1 = list(my_tuple1)
my_list1.remove(96)
my_tuple1=tuple(my_list1)
print(my_tuple1)

fruits = ('mango','orange','banana','grapes','berry')
a,b,c,d,e = fruits
x,*y,z = fruits

print(a)
print(b)
print(c)
print(x)
print(y)
print(z)


