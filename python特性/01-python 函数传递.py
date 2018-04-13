#例子1
a = "1"
def fun(a):
    print(a)
    a = 2
    print(a)
fun(a)
print(a)

'''
a = 1  a 是个numbers对象， numbers对象内存地址不可变
def fun（a）,传递过来的a ，a=1
打印a a是1的引用，即a=1
a= 2 ，a是2的引用，此时的a与上面的a 是两个不同的内存地址，一个是numbers 1 的引用，一个是numbers 2的引用
print（a） 即结果为2
fun(a)函数执行不会对 a 是 1 number 类型对象，即 最后打印print（a） a = 1

python 中 numbers，strings，tuples类型不可变
'''


#例子2
a = []

def fun(a):
    a.append(2)

fun(a)

print(a)
'''
a是列表 ，可变对象
fun（a）执行，a列表添加了一个元素即 a=[2】
打印a的值，即a = [2]

python中list，dict ，set 是可变对象
'''




#例子3

a = 1
print(id(a))
def fun(a):
    print("fun_in",id(a))

    a = 2
    print("re-point",id(a),id(2))
fun(a)

print('fun-out',id(a),id(1))

print(a)



'''
通过对象的内存地址的变化可以看出，对象在内存中的变化
'''