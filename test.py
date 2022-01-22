"""
# 多行注释
第一个注释
第二个注释
第三个注释
"""
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
else :
  print('欢迎用户光临！')

# if-elif-else
age = int(input('输入年龄：'))
if age <= 20:
    print('青年')
elif age <= 30:
    print('青年')
elif age <= 60:
    print('老年')
else:
    print('小孩')

# if语句练习
1.获取用户输入的整数，判断数字的奇偶性
num = int(input('输入一个整数:'))
if num % 2 == 1:
    print('这个数是奇数')
else:
    print('这个数是偶数')

# 2.编写一个程序判断年份是否为闰年。如果年份可以不能被100整除或者可以被400整除，那么年份为闰年
year = int(input('输入年份判断是否为闰年：'))
if year % 100 != 0 or year % 400 == 0:
    print('闰年')
else:
    print('平年')
# 3.狗的前两年每一年相当于人的10.5岁，之后每增加一年就增加4岁。编写一个程序，获取用户输入的狗的年龄，显示其相当于人类的年龄。
dog_age = int(input('输入狗的年龄：'))
if dog_age < 0:
    if dog_age <= 2:
        print('狗的年龄相当于人的：', dog_age * 10.5,'岁')
    else:
        print('狗的年龄相当于人的：', (dog_age - 2) * 4 + 21, '岁')
else:
    print(请输入合法的数字：)

4.从键盘输入小明的期末成绩：
  当成绩为10时，’奖励一辆BMW‘；
  当成绩为[80-99]时，’奖励一台iphone‘；
  当成绩为[60-79]时，’奖励一本参考书‘；
  其他时什么奖励都没有


def customFun():
    acheviementReport = int(input('请输入你的成绩:\n'))
    if acheviementReport==10:
        print('奖励一辆BMW')
    elif 80 <= acheviementReport <= 90:
        print('奖励一台iphone')
    elif 60 <= acheviementReport < 80:
        print('奖励一本参考书')
    else:
        print("什么都没有")
    customFun()
customFun()


# 5.女方家长嫁女儿的条件： 高：180cm以上；富：1000以上；帅：500以上；
#   如果三个条件同时满足，则'我一定要嫁给他'；
#   如果三个条件有为真的情况，则'嫁吧，比上不足比下有余'
#   如果三个条件都不满足，则'不嫁'

high = int(input('身高：\n'))
price = int(input('请输入家产:\n'))
handsome = int(input('请输入颜值:\n'))
if high >= 180 and price >= 1000 and handsome >= 500:
    print('我一定要嫁给他！')
elif high >= 180 or price >= 1000 or handsome >= 500:
    print('嫁吧，比上不足比下有余')
else:
    print('不嫁')
  
  
# while循环语句
i = 0  # 初始化表达式
while i < 10:  # 初始化表达式
    i += 1  # 更新表达式
    print('hello')

# while语句练习
# 1.求100以内所有的奇数之和
# 获取100内所有的数
i = 0
# 创建一个变量保存结果
result = 0
while i < 100:
    i += 1
    if i % 2 == 1:
        result += i
print('100内所有奇数之和为：', result)

# 获取100以内所有的奇数
i = 1
while i < 100:
    print(i)
    i += 1


# 2.求100以内所有7的倍数之和以及个数
i = 0
num = 0
result = 0
while i < 100:
    i += 1
    if i % 7 == 0:
        num += 1
        result += i
print('100以内所有7的倍数之和为：\n', result)
print('100以内所有7的倍数的个数：\n', num)


# 3.水仙花数是指一个n位数（n>=3），它的每个位上的数字的n次幂之和等于它本身
#  （例如1**3 + 5**3 + 3**3 = 153） 求1000以内所有的水仙花数

i = 100
while i < 1000:
    # 设a为i的百位数
    a = i // 100
    # 设b为i的十位数
    b = i // 10 % 10  # b = i - a * 100 // 10
    # 设c为i的个位数
    c = i % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
    i += 1

# 4.获取用户输入的任意数，判断其是否为质数
i = 2
num = int(input('输入任意整数：'))
flag = True
while i < num:
    if num % i == 0:
        flag = False
    i += 1
if flag:
    print(num, '是质数')
else:
    print(num, '不是质数')

# 步骤：
# 获取用户输入的任意数
      num = int(input('输入任意整数：'))
# 举例有可能成为9的因数的数- 2、3、4、5、6、7、8
# 获取所有可能整除num的整数
#     i = 2  # 不包含1
#     flag = True  # 传递判断结果
#     while i < num:  # 不包含自身
#         # 判断num能否被i整除
#         # if num % i != 0: i还没递增，num不能被一个i整除，不能判断为质数
#         # 逆向思维num能被i整除，num不是质数
#         if num % i == 0:
#             flag = False  # num不是质数则结果输出为False
#         i += 1

#  循环嵌套练习
#  1.打印99乘法表
i = 0
while i < 9:
    j = 0
    while j < i + 1:
        a = i + 1
        b = j + 1
        c = a * b
        print(a, '*', b, '=', c, '', end='')
        j += 1
    print('')
    i += 1

i = 0
while i < 9:
    j = 0
    while j < i + 1:
        print('*', end='')
        j += 1
    print('')
    i += 1

#  2.求100以内所有质数
    i = 2
        # j = 2 # j没有放进循环不会重置，j应从2开始
        # result = True #result没有放进循环不会重置，result应该默认为True开始
    while i <= 100:
        j = 2
        result = True
        while j < i:
            if i % j == 0:
                result = False
            j += 1
        if result:
            print(i)
        i += 1

#创建循环求1-100
i = 2
while i <= 100:
    # print(i)
    # 创建一个变量，记录i的状态，默认i是质数
    flag = True
    # 判断i是否质数
    # 获取所有可能是i的因数
    j = 2
    while j < i:
        # 判断i能否被j整除
        if i % j == 0:
            flag = False
        j += 1
    # 验证结果并输出
    if flag:
        print(i)
    i += 1


# 3.倒三角形
i = 0
while i < 9:
    j = 9
    while j > i:
        print('*', end='')
        j -= 1
    i += 1
    print('')

# break
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print('hello')

# continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print('hello')


# 质数练习优化
from time import *
begin = time()
i = 2
while i <= 10000:
    j = 2
    result = True
    # while j < i:
    while j <= i ** 0.5:
        if i % j == 0:
            result = False
            break
        j += 1
    if result:
        # print(i)
        pass
    i += 1
end = time()
print('程序执行花费了：', end - begin, '秒')


# 综合练习
# 小游戏《唐僧大战白骨精》
# 1. 身份选择
# - 显示提示信息：欢迎来到《xxx》
# - 请选择你的身份：1. xxx  2. xxx
# - 根据用户选择来分配身份（显示不同提示信息）：你已经选择唐僧，恭喜你将以唐僧的身份进行游戏！
# - 你居然选择白骨精，太不要脸了。系统已为你自动分配角色为唐僧
# -  选项错误，系统已自动为你分配角色为唐僧。
#
# 2. 游戏进行
#    - 显示玩家基本信息（攻击力、生命值）
#    - 显示玩家可以进行的操作（练级 打boss 逃跑）
#    - 练级：提升玩家攻击力和生命值
#    - 打boss：玩家攻击boss，boss反击，计算boss是否被玩家消灭，计算玩家是否已经被boss消灭。

# 身份选择
# 欢迎语
print('='*15, '欢迎来到20年前的小游戏', '='*15)
# 游戏身份选择
identity = int(input('请选择你的身份：\n 1.唐僧\n 2.白骨精\n'))
# 打印分割线
print('-'*50)
if identity == 1:
    print('你已经选择->唐僧<-，恭喜你将以->唐僧<-的身份进行游戏！')
elif identity == 2:
    print('你居然选择白骨精，太不要脸了。系统已为你自动分配角色为->唐僧<-')
else:
    print(' 选项错误，系统已自动为你分配角色为唐僧。')

# 进入游戏
# 显示玩家信息
# print('******当前角色是：唐僧\t 生命值：100\t  攻击力：20******')

# 创建变量保存信息
# operation = int(input('请选择下一步操作:\n 1.练级\n 2.打boss\n 3.睡大觉'))
play_life = 100  # 生命值
play_attack = 20  # 攻击力
play_grade = 1  # 等级
boss_life = 1000
boss_attack = 200
print('*' * 10, f'当前角色是：唐僧\t 生命值：{play_life}\t', f'攻击力：{play_attack}\t', f'等级： {play_grade}\t', '*' * 10)
# 游戏选项需要反复出现，写到死循环中
while True:
    operation = int(input('请选择下一步操作:\n 1.练级\n 2.打boss\n 3.逃跑\n'))
    # 增加玩家生命值和攻击力
    if operation == 1:
        play_life += 50
        play_attack += 100
        play_grade += 1
        print('*'*20, '练级成功！当前等级为：', play_grade, '当前生命值为：', play_life, '当前攻击力为：', play_attack, '*'*20)
    # 玩家攻击boss，boss减去的生命值等于玩家攻击力
    elif operation == 2:
        # 玩家攻击boss，boss减去的生命值等于玩家攻击力
        boss_life -= play_attack

        print('->唐僧<- 攻击了 ->白骨精<-')
        # 检查玩家是否赢了,赢则游戏结束，没赢则受到反击
        if boss_life <= 0:
            print(f'->白骨精<-受到了{play_attack}点伤害，打败boss，->唐僧<-赢得对局')
            break
        else:
            # boss反击，唐僧受到boss攻击力等额伤害
            play_life -= boss_attack
            print(' ->白骨精<-攻击了->唐僧<- ')
            if play_life <= 0:
                print(f'->唐僧<-受到了{ boss_attack } 点伤害，挑战失败')
                break
    # 逃跑，退出游戏
    elif operation == 3:
        print('->唐僧<-扭头撒腿就跑！game over')
        break
    else:
        break
        print('选项错误，退出游戏')

"""
# 字符串截取
a = 'hello world'
print(a[0:6])  # 截取第一个到第六个字符：hello （空格也算）
print(a[2:-2])  # 截取第三个到倒数第三个字符：hello wor
print(a[0])  # 截取第一个字符：h
print(a[1:])  # 截取第二个后的全部字符：ello world

# 列表创建
list1 = ['如果可以作弊', '我会想你念你', 1, 2, 3]
print(list1)
list2 = ['我', '曾将', '青春', '翻涌', '成', '她']
print(list2[1])  # 曾将
print(list2[-1])  # 成

# 列表截取
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums[2:7])  # 30,40,50,60,70
print(nums[1:-2])  # 20,30,40,50,60

# 列表修改
list3 = ['如果可以作弊', '我会想你念你', 1, 2, 3]
list3[2] = '到最后的荼蘼'
print(list3)

# 列表添加和删除
list3 = ['如果可以作弊', '我会想你念你', 1, 2, 3]
list3.append('到最后的荼蘼')
del list3[3]
print(list3)

# 列表拼接
squares = [1, 2, 3]
squares += [7, 8, 9]
print(squares)

# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
list = [a, n]
print(list)
# 索引子表
print(list[0])  # ['a', 'b', 'c']
# 索引子表的元素
print(list[0][1])  # b

# 创建元组
tuple = ('Google', 'Runoob', 1997, 2000)
tup1 = (1, 2, 3, 4, 5)
tup2 = 3, 5, 6  # 不用小括号也可以
tup3 = ()
print(type(tuple))
print(type(tup1))
print(type(tup2))
print(tup1)
print(tup2)
print(tup3)

# 元组只有单个元素，加逗号
tup1 = (50)
tup2 = (50,)
print(type(tup1))
print(type(tup2))

# 元组索引
tup1 = (10, 20, 30, 40, 50, 60)
print(tup1[0])  # 10
print(tup1[1:5])  # (20, 30, 40 ,50)
print(tup1[2:-1])  # ( 30, 40, 50)

# 元组拼接
tup1 = ('a', 'b', 'c')
tup2 = (1, 2, 3)
tup3 = tup1 + tup2
print(tup3)

# 元组的删除
tup1 = (1, 2, 3)
del tup1
print(tup1)

# 元组不可变
tup1 = (1, 2, 3)
print(id(tup1))
tup1 = ('a', 'b', 'c')
print(id(tup1))

# 创建字典
tinydict = {'a': 1, 'b': 2, 'c': 3}
emptydict = {}
print(tinydict)
print(emptydict)
print('length=', len(tinydict))
print('length=', len(emptydict))
print(type(tinydict))

# 访问字典
tinydict = {'Name': '大傻春', 'Age': 2, 'Class': '你要干什么'}
print(tinydict['Name'])
print(tinydict['Class'])

# 字典新增、修改
tinydict = {'Name': '大傻春', 'Age': 2, 'Class': '你要干什么'}
tinydict['Age'] = '你个大傻子'
tinydict['Word'] = '滚就滚'
print(tinydict['Word'])
print(tinydict)

# 删除字典元素
tinydict = {'Name': '大傻春', 'Age': 2, 'Class': '你要干什么', 'Word': '滚就滚'}
del(tinydict['Age'], tinydict['Word'])
print(tinydict)
tinydict.clear()
print(tinydict)

# 删除一个字典
tinydict = {'a': 1, 'b': 2, 'c': 3}
del tinydict
print(tinydict)

# 字典键不允许被赋值两次
tinydict = {'a': 1, 'b': 2, 'c': 3}
tinydict['b'] = 30
print(tinydict)

# 字典键不允许用可变的数据类型
tinydict = {[a]: 1, 'b': 2, 'c': 3}
print(tinydict)
