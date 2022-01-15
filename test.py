'''
# 多行注释
第一个注释
第二个注释
第三个注释
'''
"""
print("Hello,Python!!!")

# 缩进不同导致代码报错
if True:
  print("1")
  print("true")
else:
  print("0")
 print("false")

# 数字过长使用分隔符
print(100_100_100)

# 二进制表示
a = 0b10
print(a)

# 浮点型不能直接计算，会得到一个不精确的结果
b = 0.1 + 0.2
print(b)

# 引号指定字符串
s = 'Hello'
print(s) 


# 不同引号之间才能嵌套
s = '子曰："学而时习之，不亦说乎"'
print(s)

# 三引号指定多行字符串
s = '''锄禾日当午，
汗滴禾下土。
谁知盘中餐，
粒粒皆辛苦。'''
print(s)


# 转义符
s = '子曰:"学而时习之，\n不亦说乎"'
print(s)

# 格式化字符串
a = 123
print('a=',a)


# 指定单个占位符
b = 'hello %s'%'孙悟空'
print(b)
# 指定多个占位符
c = 'hello %s 你好 %s'%('tom','孙悟空')
print(c)
# 指定占位符最小字符位数
d = 'hello %3s'%'abcde'
print(d)
# 占位不够最小字符数时空格补位
e = 'hello %5s'%'abc'
print(e)
# 占位字符数区间
f = 'hello %3.5s'%'abcdefg'
print(f)
# 指定占位符最大字符位数
g = 'hello %.3s'%'abcde'
print(g)
# %f指定小数的位数
h = 'hello %.3f'%123.45678
print(h)
# 整数占位符
i = 'hello %d'%123.123
print(i)

# 字符串嵌入变量
a = '123'
b = '六儿'
c = f'hello {a} {b}'
print(f'c= {c}')
print(f'a= {a}')

# 练习：创建变量保存名字，使用四种方式输出，欢迎xxx光临
name = '李4'
#拼串
print('欢迎'+name+'光临!')
#多个参数
print('欢迎',name,'光临！')
#占位符
print('欢迎%s光临!'%name)
#格式化字符串
print(f'欢迎{name}光临!')

#复制字符串
k = 'abc'
k = k*20
print(k)

#布尔值
a = True
print('a = ',a)
#布尔值属于整型
print(1+False)

#空值
c = None
print(c)

#类型检查
a = 123 
b = '123' 
#方式一
type(123)
c  = type(123)
print(c)
#方式二
d = type(a)
print(d)
#方式三
print(type(b))
# 直接查看值的type
print(type(1))
print(type(1.5))
print(type(True))
print(type('hello'))
print(type(None))

# 查找值的id
id(123)
# 变量与对象
a = 123
id(a)
b = a
id(b)

#变量相互独立
a = 10
b = a
print(b)
a = 20
print(a,b)

# 定义一个变量a的类型
a = True
print('a = ',a)
print('a的类型为',type(a))

# 重新赋值a
a = 'True'
# int(a)  若执行结果a仍为bool，不会产生影响
a = int(a) # 重新赋值a
print('a = ',a)
print('a的类型为',type(a))

# 需要字符串和其他类型拼串时
b = 123
print('hello',str(b))

# 加法运算符
a = 10 + 5
print('a =',a) # 计算
b = 'hello' + 'world' # 拼串
print('b =',b)


# 除法运算符
a = 10 / 3
print('a = ',a)
b =10 // 3 # 整除
print('b = ',b)

#幂运算和开方
a = 2**3
print('a = ',a)
b = 16**0.5 # 求开方
print('b = ',b)

#取模
a = 10 % 5
print('a = ',a)
b = 10 % 4
print('b = ',b)
c = 10 % 3
print('c = ',c)
d = 10 % 2
print('d = ',d)

# 关系运算符
10 > 20
print(int('2') > int('11'))

result = 'qqq' is not 'aaa'
print('result = ',result)

#非运算
a = True
a = not a #对a进行非运算
b = 1
b = not b
c = ''
c = not c
print('a = ',a)
print('b = ',b)
print('c = ',c)


# 练习
# 布尔值逻辑运算
a = True
a = not a
b = None
b = not b
print('a = ',a)
print('b = ',b)

result = True and False
print('result = ',result)

result1 = True or False
print('result1 = ',result1)

#非布尔值逻辑运算
c = 10
c = not c
print('c = ',c)

d = 10 and 20
print('d = ',d)
e = 'hello' and 'world'
print('e = ',e)

f = True or 'world'
print('f = ',f)
g = 'hello' or 123
print('g = ',g)


# 非布尔值的逻辑运算
# True and True
result1 = 1 and 2 # 2
# True and False
result2 = 1 and 0 # 0
# False and True
result3 = 0 and 1 # 0
# False and False
result4 = 0 and None # 0
print('result1 = ',result1)
print('result2 = ',result2)
print('result3 = ',result3)
print('result4 = ',result4)

# True or True
result5 = 1 or 2 # 1
# True or False
result6 = 1 or 0 # 1
# False or True
result7 = 0 or 1 # 1
# False or False
result8 = 0 or None # None
print('result5 = ',result5)
print('result6 = ',result6)
print('result7 = ',result7)
print('result8 = ',result8)

# 比较两个值的大小
a = 10
b = 20 
print('a大') if a > b else print('b大')

c = 66
d = 38 
max = c if c > d else d
print('max = ',max)

# 练习
# 三个值的最大值
a = 100
b = 200
c = 300
mid = a if a > b else b
max = mid if mid > c else c
print('三者中最大值是',max)

# 运算符可以用括号控制优先级
a = 1 or 2 and 3
b = (1 or 2) and 3
print(a,b)


# 条件判断语句
num = 20
if num > 10 : print('num比10大') 

# if 后面跟代码块
if True :
 print('123456')
 print('789')
 print('abc')
 print('hello')

# 练习：在命令行让用户输入一个用户名，获取用户输入，并进行判断：
如果用户输入的用户名是admin，则显示欢迎管理员光临；
如果用户输入的是其他用户名，则什么也不做。

str_input = input('\n\n请输入用户名:')
if str_input == 'admin':
  print('欢迎管理员光临')

# input（）函数
a = input()
print('用户输入的内容是：',a)

input('请输入用户名：')



# 练习：用户输入一个年龄，如果年龄大于18岁，则显示你已经成年了。
# age = input('请输入用户的年龄：')
# age = int(age)
# age是字符串不能直接和数字比较,也可以用下面语句：
age = int(input('请输入用户的年龄：'))
if age >= 18:
    print('你已经成年了~~~')

# if-else
username = input('输入用户名：')
if username == 'admin':
    print('欢迎管理员光临！')
else:
    print('欢迎用户光临！')
"""
