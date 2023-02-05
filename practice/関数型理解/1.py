# even_list = []
# for i in range(200):
#     if (i % 2 == 0):
#         even_list.append(i)

# print(*even_list)

# def test():
#     return 1

# print(f'{test()}')
# print(type(test))

def fun1(fun, text):
    fun(text)

def fun2(text):
    print('fun2 ' + text)

fun1(fun2, 'hello')