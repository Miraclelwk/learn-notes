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

# 列表截取(切片)
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums[2:7])  # 30,40,50,60,70
print(nums[1:-2])  # 20,30,40,50,60

# 列表长度
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print('列表长度为： ', len(nums))
# 练习：在列表中保存5个名字，通过索引获取每个名字。
names = ['小a', '小b', '小c', '小d', '小e']
print(names[0])
print(names[1])
print(names[2])
print(names[-2])
print(names[-1])

# 列表单个元素修改
list3 = ['如果可以作弊', '我会想你念你', 1, 2, 3]
list3[2] = '到最后的荼蘼'
print(list3)
# 列表切片修改
list3 = ['如果可以作弊', '我会想你念你', 1, 2, 3]
list3[2:] = ['到最后的荼蘼','如果回忆容易', '我会想你念你']
print(list3)
# 设置步长修改列表
list3 = [1, '如果可以作弊', 2, '我会想你念你', 3]
list3[::2] = ['到最后的荼蘼', '如果回忆容易', '我会想你念你']
print(list3)

# 列表添加和删除
list3 = ['如果可以作弊', '我会想你念你', 1, 2, 3]
list3.append('到最后的荼蘼')
del list3[3]
print(list3)
# 通过切片删除列表元素
casual_list = [1, 123, 213, 12321, 3242213, 223, 123, 423, 324, 32133]
del casual_list[0:2]
print(casual_list)
del casual_list[::2]
print(casual_list)

# 列表拼接和重复
squares = [1, 2, 3]
squares += [7, 8, 9]
print(squares)
print(squares * 3)

# 列表函数&方法
# 函数
# in & not in
casual_list = [1, 123, 213, 12321, 3242213]
print(123 in casual_list)
print('hello' not in casual_list)
# len() & min() & max()
casual_list = [1, 123, 213, 12321, 3242213]
print(len(casual_list))
print(min(casual_list))
print(max(casual_list))
# 方法
# index（）
casual_list = [1, 123, 213, 123, 3242213]
print(casual_list.index(213))
print(casual_list.index(213, 1))  # 第二个参数表示查找的起始位置
print(casual_list.index(213, 1, 3))  # 第三个参数表示查找的终点位置

# count()
casual_list = [1, 123, 213, 123, 3242213]
print(casual_list.count(123))
print(casual_list.count(213))
print(casual_list.count(111))

# 列表的方法
# insert
stus = ['孙悟空', '猪八戒', '牛魔王', '白骨精']
print('原列表：', stus)
stus.insert(2, '唐僧')
print('新列表：', stus)

# extend
stus = ['孙悟空', '猪八戒', '牛魔王', '白骨精']
print('原列表：', stus)
stus.extend(['dddd', '唐僧'])
print('新列表：', stus)

# clear
stus = ['孙悟空', '猪八戒', '牛魔王', '白骨精']
stus.clear()
print(stus)

# pop
stus = ['孙悟空', '猪八戒', '牛魔王', '白骨精']
result = stus.pop(2)
print('返回值：', result)

# remove
stus = ['孙悟空', '猪八戒', '牛魔王', '白骨精', '猪八戒']
stus.remove('猪八戒')
print(stus)

# reverse
casual_list = [1, 123, 213, 12321, 3242213]
casual_list.reverse()
print(casual_list)

# sort
casual_list = [1, 123, 213, 12321, 3242213]
casual_list.sort()
print(casual_list)
casual_list.sort(reverse=True)
print(casual_list)


# 遍历列表
# while循环
stus = ['孙悟空', '猪八戒', '牛魔王', '白骨精', '猪八戒']
i = 0
while i < 4:
    print(stus[i])
    i += 1

# for循环
stus = ['孙悟空', '猪八戒', '牛魔王', '白骨精', '猪八戒']
for s in stus:
    print(s)


# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
list = [a, n]
print(list)
# 索引子表
print(list[0])  # ['a', 'b', 'c']
# 索引子表的元素
print(list[0][1])  # b


# 列表练习
# EMS（Employee Manager System 员工管理系统）
# 显示系统欢迎信息
print('-'*20, '欢迎进入员工管理系统', '-'*20)
# 创建列表,保存员工信息，字符串形式
emps = ['\t孙悟空\t16', '\t猪八戒\t15']
# 创建死循环
while True:
    # 显示用户选项
    print('-' * 60)
    print('请选择你要进行的操作：')
    print('\t1.查询员工\t')
    print('\t2.添加员工\t')
    print('\t3.删除员工\t')
    print('\t4.退出\t')
    user_code = input('请选择1-4：\n')
    print('-'*60)
    if user_code == '1':  # 查询员工
        # 创建变量
        print('\t序号\t\t姓名\t\t年龄')
        # 创建变量表示序号
        n = 1
        for emp in emps:
            print(f'\t{n}\t{emp}')
            n += 1
    elif user_code == '2':  # 添加员工
        # 获取员工信息
        emp_name = input('请输入员工姓名:')
        emp_age = input('请输入员工年龄:')
        emp = f'\t{emp_name}\t\t{emp_age}'
        print('-' * 60)
        # 提示
        print('员工：', emp, '将被添加到系统中')
        user_confirm = input('是否继续添加[Y/N]：')
        print('-' * 60)
        if user_confirm == 'Y':
            emps.append(emp)
            print('插入成功')
        elif user_confirm == 'N':
            print('取消成功')
            pass
    # 删除员工
    elif user_code == '3':
        del_num = int(input('请输入删除员工序号：'))
        if 0 < del_num <= len(emps):
            del_index = del_num - 1
        else:
            print('输入有误')
        print('员工：', emps[del_index], '将被删除')
        print('\t序号\t姓名\t\t年龄')
        print(f'\t{del_num}\t{emps[del_index]}')
        user_confirm = input('是否继续删除[Y/N]：')
        if user_confirm == 'Y':
            del emps[del_index]
            print('删除成功')
        elif user_confirm == 'N':
            print('操作取消')
            pass
    elif user_code == '4':
        input('欢迎使用，点击回车键退出')
        break
    else:
        print('您的输入有误请重新输入')

# range





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

# 元组解包
# 利用解包交换变量的值
tup1 = (10, 20, 30, 40)
a, b, c, d = tup1
print(a, b, c, d)
a, b = b, a
print(a, b)
# 利用解包分配元素给相对位置的变量
tup1 = (10, 20, 30, 40, 50)
a, b, *c = tup1
print(a, b, c)
a, *b, c = tup1
print(a, b, c)
*a, b, c = tup1
print(a, b, c)



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

# rang
r = range(5)  # 生成一个序列【0，1，2，3，4】
s = range(3, 10, 2)
print(list(r))
print(list(s))
# 通过range可以创建一个指定次数的for循环
# for循环除了创建方式以外，其余和while一样，包括break、continue都可以在for循环中使用。
for i in range(30):
    print(i)


# 可变对象
a = [1, 2, 3]
print('修改前：', a, id(a))
# 通过索引改变对象[1,2,3]的值,不会改变变量所指向的对象
a[0] = 10
print('修改后：', a, id(a))

# 修改对象的值时，如果有其他变量也指向该对象，则修改也会在其他的变量中体现
a = [1, 2, 3]
print('修改前：', a, id(a))
b = a
a[0] = 10
print('修改后：', a, id(a))
print('修改后：', b, id(b))


# 为变量重新赋值，改变变量所指向的对象
a = [1, 2, 3]
print('修改前：', a, id(a))
a = [4, 5, 6]
print('修改后：', a, id(a))

# dict函数创建字典
d = dict(name='孙悟空', age='8')
print(d, type(d))
# 双值子序列转换为字典
e = dict([('name', '孙悟饭'), ('age', 18)])
print(e, type(e))

# 获取字典的长度
d = dict(name='孙悟空', age='8')
print(len(d))

# in & not in
d = {'name': '孙悟空', 'age': 18}
print('name' in d)

# get(key,[default])获取指定键的值
e = dict([('name', '孙悟饭'), ('age', 18)])
print(d.get('name'))
print(d.get('abc'))
print(d.get('hello', '返回默认值'))
print(d)


# setdefault(key,[, default])添加字典的值
d = {'name': '孙悟空', 'age': 18}
result = d.setdefault('name')
result1 = d.setdefault('abc')
result2 = d.setdefault('address', '花果山')
print(result, result1, result2)
print(d)

# update()
d = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5, 'f': 6, 'a': 8}
d.update(d2)
print(d)

# popitem删除字典的键值对
d = {'a': 1, 'b': 2, 'c': 3}
result = d.popitem()
print(result)
print(d)
e = {}
print(e.popitem())

# pop删除字典的键值对
d = {'a': 1, 'b': 2, 'c': 3}
result1 = d.pop('c')
result2 = d.pop('e', '返回默认值')
print('result1=', result1)
print('result2= ', result2)
print(d)

# copy()字典浅复制
d = {'a': 1, 'b': 2, 'c': 3, 'e': {'name': '孙悟空', 'age': 18}}
d2 = d.copy()
print(d, id(d))
print(d2, id(d2))
d2['e']['name'] = '猪八戒'  # 修改可变对象时，原对象也会改变
print(d, id(d))
print(d2, id(d2))

# 字典遍历
# keys（）
d = {'name': '孙悟空', 'age': 18, 'address': '花果山'}
for k in d.keys():
    print(k)
# values()
d = {'name': '孙悟空', 'age': 18, 'address': '花果山'}
for v in d.values():
    print(v)
# items()
d = {'name': '孙悟空', 'age': 18, 'address': '花果山'}
for k, v in d.items():
    print(k, '=', v)

# 创建集合
s = {1, 2, 3, 4, 5, 6, 7, 8}
print(s)
p = {1, 1, 1, 1, 1, 2, 2, 2, 10, 20, 30}
print(p)
q = set('hello')  # 字符串转换为集合
t = set({'a': 1, 'b': 2, 'c': 3})  # 字典转换为集合
print(q)
print(t)

# in & not in
s = {1, 2, 3, 4, 5, 6, 7, 8}
print(1 in s)
print('hello' not in s)

# len()
s = {1, 2, 3, 4, 5, 6, 7, 8}
print(len(s))


# 集合添加元素
# add（）
s = {1, 2, 3, 4, 5, 6, 7, 8}
s.add(10)
print(s)

# update（）
s = {1, 2, 3, 4, 5, 6, 7, 8}
s2 = set('hello')
print(s)
s.update((10, 20, 30))
print(s)
s.update({'a': 1, 'b': 2, 'c': 3})  # update字典类型只会插入键
print(s)

# 删除集合元素
# pop（）
s = {1, 2, 3, 4, 5, 6, 7, 8}
result = s.pop()
print(result, s)

# remove()
s = {1, 2, 3, 4, 5, 6, 7, 8}
s.remove(7)
print(s)

# clear()
s = {1, 2, 3, 4, 5, 6, 7, 8}
s.clear()
print(s)

# copy()
s = {1, 2, 3, 4, 5, 6, 7, 8}
s2 = s.copy()
print(s, id(s))
print(s2, id(s2))

# 集合的运算
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7, 8, 9}
# & 交集运算
result1 = s1 & s2
print(result1)
# | 并集运算
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7, 8, 9}
result2 = s1 | s2
print(result2)
# - 差集运算
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7, 8, 9}
result3 = s1 - s2
print(result3)
# ^ 异或集运算
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7, 8, 9}
result4 = s1 ^ s2
print(result4)
# <= 检查一个集合是否为另一个的子集
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5, 6}
result = s1 <= s2
print(result)
# < 检查一个集合是否为另一个的真子集
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5, 6}
result = s1 <= s2
print(result)
# >= 检查一个集合是否为另一个的超集
s1 = {1, 2, 3}
s2 = {1, 2, 3}
s3 = {123, 213}
result1 = s1 >= s2
result2 = s1 >= s3
print('result1=', result1)
print('result2=', result2)
# > 检查一个集合是否为另一个的真超集
s1 = {1, 2, 3}
s2 = {1, 2, 3}
s3 = {1, 2}
result1 = s1 > s2
result2 = s1 > s3
print('result1=', result1)
print('result2=', result2)



# 函数
# 定义函数
def fun():
    print('这是我的第一个函数')
    print('hello')
    print('world')


fun()
print(type(fun))
print(id(fun))


# 函数的参数
def add_sum(a, b):  # 形参相当于在函数内写上：a = None b = None
    print(a, '+', b, '=', a+b)


add_sum(10, 20)
add_sum(123, 233)
add_sum(12, 21)


# 定义函数练习1：定义一个函数，可以用来求任意三个数的乘积
def product(a, b, c):
    print(a, '*', b, '*', c, '=', a*b*c)


product(10, 20, 30)
product(123, 345, 789)


# 定义函数练习2：定义一个函数，可以根据不同的用户名显示不同的欢迎信息
def welcome(a):
    print('欢迎', a, '光临')


welcome('孙悟空')

# 实参的类型


def fn():
    print('这是我的第一个函数')
    print('hello')
    print('world')


def fn2(a):
    print('a = ', a)


b = 123
c = True
d = 'hello'
e = [1, 2, 3]
fn2(b)
fn2(c)
fn2(d)
fn2(e)
fn2(fn)


# 形参重新赋值对其他变量不产生影响
def fn3(a):
    a = 20
    print('a = ', a)


c = 10
fn3(c)
print('c = ', c)


# 修改形参指向的对象会对其他变量产生影响
def fn4(a):
    a[0] = 10
    print('a = ', a, id(a))


c = [1, 2, 3]
fn4(c)
print('c = ', c, id(c))

# 不定长参数


def fn(*a):
    print('a= ', a, type(a))


fn(123, 213, 323)

# 定义一个函数可以令任意数字相加


def fun(*nums):
    result = 0
    for n in nums:
        result += n
    print('sum=', result)


fun(123456, 123, 123123, 123123, 12)

# 可变参数的使用


def fn(a, b, *c):
    print('a= ', a)
    print('b= ', b)
    print('c= ', c)


fn(1, 2, 3, 4, 5)


# 可变参数后的参数必须关键字传参
def fn2(a, *b, c):
    print('a= ', a)
    print('b= ', b)
    print('c= ', c)


fn2(1, 2, 3, 4, 5, c=6)


# 全部参数以关键字传参
def fn2(*, a, b, c):
    print('a= ', a)
    print('b= ', b)
    print('c= ', c)


fn2(a=1, b=2, c=3)


# **形参
def fn2(b, c, **a):
    print('a= ', a, type(a))
    print('b= ', b)
    print('c= ', c)


fn2(b=2, c=3, d=1, e=5, f=6)


# 参数解包
# 对序列解包
def fn2(a, b, c):
    print('a= ', a)
    print('b= ', b)
    print('c= ', c)


# 创建一个元组或者列表
t = (1, 2, 3)
# 传统方式传参： fn2(t[0], t[1], t[2])
fn2(*t)


# 对字典解包
def fn2(a, b, c):
    print('a= ', a)
    print('b= ', b)
    print('c= ', c)


# 创建一个字典
t = {'a': 1, 'b': 2, 'c': 3}
# 传统方式传参： fn2(t[0], t[1], t[2])
fn2(**t)


# 返回值
def fn():
    def fn2():
        print('hello world')
    return fn2()
    # return 100
    # return 'hello'
    # return [1,2,3]


fn()
print(fn())


def fun(*nums):
    result = 0
    for n in nums:
        result += n
    return result


r = fun(123, 123)
print(r)


# 函数后加不加（）的区别
def fn5():
    return 10


print(fn5)
print(fn5())


# 文档字符串
# help()函数
help(print)


# 文档字符串
def fn():
    '''
    这是一个文档字符串的示例
    函数的作用:.....
    函数的参数：
        a:作用，类型，默认值......
        b:作用，类型，默认值......
        c:作用，类型，默认值......
    '''
    return 10


# 说明参数和返回值类型
def fn(a: int, b: bool, c: str = 10) -> int:
    # 此处说明参数a为int，b为bool，c为str，返回值为int
    return 10


# 作用域
# 全局作用域
b = 20


def fn():
    a = 10
    print('函数内a：', a)
    print('函数外b:', b)


fn()


# 函数作用域
a = 20


def fn():
    a = 10
    print('函数内a：', a)


fn()
print('函数外a：', a)

# 变量的查找

a = 10


def fn():
    global a
    a = 20
    print('修改后的a:', a)


fn()
print('全局变量的a：', a)


# 命名空间
scope = locals()  # 获得当前命名空间
print(scope, type(scope))  # 返回一个字典
scope['c'] = 10  # 向字典中添加一个key-value相当于创建一个全局变量（一般不建议这么做）
print('c=', c)


def fn():
    a = 10
    scope = locals()  # 获得当前函数命名空间
    print(scope, type(scope))  # 返回一个字典
    scope['b'] = 20  # 通过操作函数的命名空间（一般不建议这么做）
    print('b = ', b)


fn()


# globals（）查看全局命名空间
b = 10


def fn():
    global_scope = globals()  # 获得全局命名空间
    print(global_scope)  # 查看全局命名空间
    global_scope['b'] = 20  # 修改全局变量
    print('b = ', b)


fn()
print('函数外b：', b)

# 递归
# 创建一个函数求10！


def factorial():
    n = 10
    for i in range(1, 10):
        n = n * i
    print(n)


factorial()


# 创建一个函数求任意数的阶乘
def factorial2(n):
    '''
    这是一个求任意数阶乘的函数
    参数 n：求阶乘的数字
    '''
    # 创建一个变量保存结果
    result = n
    for i in range(1, n):
        result = result * i
        return result
    print(n, '的阶乘为：', result)


factorial2(5)

# 递归例子：求任意数的阶乘
# 10! = 10 *9!
# 9! = 9 * 8!
# 8! = 8 *7!
...
# 1!= 1


def factorial2(n):
    '''
    这是一个求任意数阶乘的函数
    参数 n：求阶乘的数字
    '''
    # 基线条件：判断n是否为1，如果为1则不再继续
    if n == 1:
        # 1的阶乘就是1，直接返回1
        return 1
    # 递归条件 return n*(n-1)
    return n * factorial2(n-1)


print(factorial2(10))

# 递归练习
# 练习1：创建一个函数power来求任意数字做幂运算 n ** i


def power(n, i):
    '''
    这是一个power函数，为任意函数做幂运算
    参数 n：幂运算数字
    i:幂运算次数
    '''
    # 基线条件：1次幂
    if i == 1:
        return n
    # 递归条件
    return n * power(n, i-1)


# print(n, '的', i, '次幂为：', power(10, 3))
print(power(10, 3))


# 练习2:创建一个函数，用来检查一个任意字符串是否是回文字符串，如果是返回True，否则返回False
def pal(pal_str):
    '''
    该函数用来检查字符串是否为回文字符串，是返回True，否返回False
    '''
    # abcdedcba
    # 先判断第一个和最后一个字符是否相等，如果相等判断bcdedcb是否回文
    # 判断bcdedcb是否回文
    # 判断cdedc是否回文
    # 判断ded是否回文
    # 判断e是否回文
    # 基线条件：字符串的长度小于2是回文字符串
    #         字符串第一个不等于最后一个不是回文字符串
    if len(pal_str) < 2:
        return True
    elif pal_str[0] != pal_str[-1]:
        return False
    # 递归条件
    return pal(pal_str[1:-1])


print(pal('abcdedcba'))


# 高阶函数
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = []


def fn2(i):
    if i % 2 == 0:
        return True
    return False


def fn(func, lst):
    '''
    该函数用于将指定的元素输出到新的列表中
    参数 lst：用来保存新表


    '''
    for n in lst:
        if func(n):
            l2.append(n)
    return l2


print(fn(fn2, l1))


# 匿名函数
# filter
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = []


def fn2(i):
    if i % 2 == 0:
        return True
    return False


def fn(func, lst):
    '''
    该函数用于将指定的元素输出到新的列表中
    参数 lst：用来保存新表


    '''
    for n in lst:
        if func(n):
            l2.append(n)
    return l2


r = filter(fn2, l1)
print(list(r))

# def fn(a, b):
# 	return a+b
# 等价于:
lambda a, b: a + b
print(lambda a, b: a + b)
print((lambda a, b: a + b)(10, 20))

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = []


# 匿名函数


def fn(func, lst):
    '''
    该函数用于将指定的元素输出到新的列表中
    参数 lst：用来保存新表


    '''
    for n in lst:
        if func(n):
            l2.append(n)
    return l2


r = filter(lambda i: i % 2 == 0, l1)
print(list(r))

# map（）
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = map(lambda i: i + 1, l1)
print(r)
print(list(r))


# sort()方法
l3 = ['kkk', 'cc', 'aa', 'hhh']
l3.sort()
print(l3)
l3 = ['kkk', 'c', 'aa', 'hhhhh']
l3.sort(key=len)
print(l3)
l3 = [5, '1', 3, 8, 6]
l3.sort(key=int)
print(l3)


# 闭包
a = 20


def fn():
    # 在函数内部定义一个变量
    a  = 10
    # 在函数fn（）内部定义一个函数fn2（）
    def fn2():
        print('我是fn2', a)

    # 将函数fn2（）作为返回值返回
    return fn2()

# r是调用fn（）后返回的函数，在函数内部定义，并不是全局函数
# 因此外部无法访问到函数fn（）内部的变量，r能访问到内部变量
r = fn()
r
print(a)


# 求平均值
nums = []


# 创建一个函数来计算平均值
def averager(n):
    # 将n添加到列表中
    nums.append(n)
    # 计算平均值
    return sum(nums)/len(nums)


print(averager(10))
print(averager(20))
print(averager(30))


# 平均数优化
def make_averager():
    nums = []

    # 创建一个函数来计算平均值
    def averager(n):
        # 将n添加到列表中
        nums.append(n)
        # 计算平均值
        return sum(nums)/len(nums)

    return averager


averager = make_averager()
print(averager(10))
print(averager(20))
print(averager(20))
print(averager(20))




# 装饰器引入
# 新需求：在函数执行前后增加提示
# 直接修改原函数较为麻烦且违反ocp原则
def add(a, b):
    '''
    求两个数的和
    '''
    r = a + b
    return r


def mul(a , b):
    '''
    求两个数的乘积
    '''
    r = a * b
    return r


# 可根据现有函数创建一个新的函数
def new_add(a, b):
    print('加法开始计算~~~')
    c = add(a, b)
    print('加法计算完成~~~')
    return c


r = new_add(10, 20)
print(r)


# 装饰器使用
def begin_end(old):
    '''
    用来对其他函数进行扩展
    参数：
        old 要扩展的函数对象
    '''
    # 创建一个新的函数，扩展被调用的函数
    # 参数采用不定长参数，可以根据被调用函数的参数数量自动接收
    def new_function(*args, **kwargs):
        print('程序开始执行')
        # 调用被扩展的函数
        result = old(*args, **kwargs)
        print('程序执行完毕')
        # 返回函数的执行结果
        return result

    # 返回新函数
    return new_function


f1 = begin_end(add)
f2 = begin_end(mul)
r = f1(2, 3)
p = f2(5, 6)
print(r)
print(p)


def fn3(old):
    '''
    用来对其他函数进行扩展
    参数：
        old 要扩展的函数对象
    '''
    # 创建一个新的函数，扩展被调用的函数
    # 参数采用不定长参数，可以根据被调用函数的参数数量自动接收
    def new_function(*args, **kwargs):
        print('这里是fn3装饰器~~~')
        # 调用被扩展的函数
        result = old(*args, **kwargs)
        print('这里是fn3装饰器~~~')
        # 返回函数的执行结果
        return result

    # 返回新函数
    return new_function


@begin_end
@fn3
def say_helllo():
    print('hello')


say_helllo()






# 类与对象


# 类
class MyClass:
    pass


print(MyClass)
# 使用类来创建对象，就像调用一个函数
mc1 = MyClass()  # mc就是通过MyClass创建的对象，也是MyClass的实例
mc2 = MyClass()
mc3 = MyClass()

print(mc1, type(mc1))


# 对象创建流程
class MyClass:
    pass


mc = MyClass()
mc.name = '孙悟空'  # 对象属性赋值为“孙悟空”
print(mc.name)  # 输出对象属性与变量类似


# 类的定义
class Person:
    # 在类的代码块中，可以定义变量和函数
    # 在类中所定义的变量，将会成为所有实例的公共属性，所有实例都可以访问这些变量
    name = '孙悟空'  # 公共属性，所有实例都可以访问

    # 在类中定义的函数称为方法，这些方法可以通过该类所有实例来访问
    def say_hello(a):
        print('你好')


# 创建Person类的实例
p1 = Person()
p2 = Person()

print(p1.name)
print(p2.name)

# 方法和函数调用的区别：
# 如果是函数调用，则调用时传几个参数，就会由几个实参；
# 但如果是方法调用，默认传递一个参数，所以方法中至少要定义一个形参。
p1.say_hello()
p2.say_hello()


# 属性和方法
class Person:
    name = '孙悟空'

    def say_hello(a):
        print('你好')


p1 = Person()
p2 = Person()
print(p1.name)  # 孙悟空
# 修改p1的name属性
p1.name = '猪八戒'
# 实例化对象p1中原来没有name属性，查找到类person中的name属性
# 修改p1name属性后，在对象p1的内存中添加name属性
print(p1.name)  # 猪八戒
print(p2.name)  # 孙悟空


# self
class Person:
    name = '孙悟空'

    def say_hello(self):
        # say_hello()方法实现如下格式：你好，我是xxx
        # 在方法中不能直接调用类中的属性如：print('你好，我是%s'% name)
        # 第一个参数就是调用方法的对象本身
        # 如果是p1调用，则第一个参数就是p1对象
        # 如果是p2调用，则第一个参数就是p2对象
        # 一般将这个参数命名为self。
        print('你好,我是%s' % self.name)


p1 = Person()
p2 = Person()
p1.name = '孙悟空'
p2.name = '猪八戒'
p1.say_hello()  # 你好,我是孙悟空
p2.say_hello()  # 你好,我是猪八戒


# 对象初始化
class Person:
    def say_hello(self):
        print('你好,我是%s' % self.name)

# 目前来讲，对于Person类来说name属性是必须的，而且每个对象的name属性都是不同的
# 而现在是定义对象之后，手动将name属性添加到对象中，这种方式容易被忽略或出现错误
# 我们希望在创建对象时，必须设置name属性，如果不设置对象将无法创建
# 属性的创建应该是自动完成的，而不是创建对象后手动添加

    def __init__(self, name):
        # 通过self向新建的对象中初始化属性
        # 每调用一次init方法就会复制实例化对象一个name属性
        self.name = name


# 调用一个Person相当于调用init，传参到init中
p1 = Person('孙悟空')
p2 = Person('猪八戒')

p1.say_hello()
p2.say_hello()




# 练习：自定义一个表示狗的类（Dog）
# 属性：name,age,gender,height
# 方法：call(),bite(),run()
class Dog:

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def call(self):
        print('狗在叫')

    def bite(self):
        print('狗在咬')

    def run(self):
        print('狗在跑')


d1 = Dog('小5', 23, '男', 167)
d1.call()
d1.bite()
d1.run()




# 封装
class Dog:

    def __init__(self, name):
        # 没有一种方法可以完全隐藏属性，封装仅仅是将属性名设置为不常用的，防君子不防小人。
        self.hidden_name = name

    def say_hello(self):
        print('hello, 这里是狗%s' % self.hidden_name)

    def get_name(self):
        '''
        函数用来获取属性
        '''
        # 获取属性的同时进行其他操作
        print('用户属性已经被获取')
        return self.hidden_name

    def set_name(self, name):
        '''
        函数用来修改属性
        '''
        print('用户属性已经被修改')
        self.hidden_name = name


d1 = Dog('小5')
d1.say_hello()



# getter和setter方法
class Person:

    def __init__(self, name):
        self._name = name

    # getter方法装饰器
    @property
    def name(self):
        print('getter方法执行了')
        return self._name

    # setter方法装饰器: @属性名(???).setter
    # 属性名还是getter的方法名
    @name.setter
    def set_name(self, name):
        print('setter方法执行了')
        self._name = name


# 此处可将方法像属性一样调用： 实例化对象.方法
p1 = Person('孙悟空')
p1.set_name = '猪八戒'
print(p1.name)




# 继承
# 定义一个类Animal，这个类需要两个方法:run() sleep()、
class Animal:
    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物会睡觉~~~')

# 定义一个类Dog，这个类需要三个方法:run() sleep() bark()
# 有一个类能实现大部分功能，但是不能实现全部功能
# 如何让这个类实现全部功能？
#   1.直接修改这个类，在这个类中添加需要的功能  --修改麻烦并且违反OCP原则
#   2.直接创建一个新的类 --创建比较麻烦，需要复制粘贴，会出现大量的重复性代码
#   3.直接从Animal类中继承属性和方法


class Dog(Animal):
    def bark(self):
        print('狗会嚎叫~~~')


d = Dog()
d.run()
d.sleep()
d.bark()

# isinstance检查一个对象是否一个类的实例，如果这个类是这个对象的父类，也会返回True
print(isinstance(d, Dog))
print(isinstance(d, Animal))

# 所有的对象都是object的实例
print(isinstance(d, object))

# 检查一个类是否为一个类的子类

print(issubclass(Dog, Animal))
print(issubclass(Dog, object))
print(issubclass(Animal, object))
print(issubclass(print, object))


# 方法的重写
class A(object):
    def AA(self):
        print('AAA')


class B(A):
    def AA(self):
        print('bbb')


class C(B):
    def AA(self):
        print('ccc')


c = C()
c.AA()



# super()
class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物会睡觉~~~')


# 父类中的所有方法都会被子类继承，包括特殊方法，也可以重写特殊方法。
class Dog(Animal):
    def __init__(self, name, age):
        # 希望可以直接调用父类的__init__来初始化父类中定义的属性
        super().__init__(name)
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


d = Dog('小5', 23)
print(d.name)
print(d.age)



# 多重继承


class A(object):
    def test(self):
        print('AAA')


class B(object):
    def test2(self):
        print('BBB')


class C(A, B):
    pass


c = C()
c.test()
c.test2()

print(A.__bases__)
print(B.__bases__)
print(C.__bases__)


class A(object):
    def test(self):
        print('AAA')


class B(object):
    def test2(self):
        print('BBB')


class C(A, B):
    pass


c = C()
c.test()




# 多重继承的复杂性
class A(object):
    def test(self):
        print('这是A的test方法')


class B(object):
    def test(self):
        print('这是B的test方法')


class C(A, B):
    pass


c = C()
c.test()




# 多态
class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class C:
    pass


a = A('孙悟空')
b = B('猪八戒')


# 对于函数say_hello（）来说，只要对象中含有name属性，就可以作为参数传递
# 这个函数不会考虑对象的类型，只要有name属性即可
def say_hello(obj):
    print('hello,我是%s' % obj.name)


say_hello(a)
say_hello(b)


# 在say_hello2（）中做了一个类型检查，也就是只有obj是A类型的对象时，才可以正常使用
# 其他类型的对象都无法使用该函数，这个函数就违反了多态
# 违反了多态的函数，只适用于一种类型的对象，无法处理其他类型对象，这样导致函数的适应性非常差
def say_hello2(obj):
    # 类型检查
    # 注意：像isinstance（）这种函数在开发中一般不会使用，因为这意味着函数可能违反了多态
    if isinstance(obj, A):
        print('hello,我是%s' % obj.name)
    else:
        print('此类型对象无法使用该函数')


say_hello2(a)
say_hello2(b)




# 类和方法总结
# 定义一个类
class A:
    # 类属性，直接在类中定义的属性是类属性
    # 类属性可以通过类或类的实例化对象访问
    # 但类属性只能通过类对象修改，无法通过实例化对象修改
    count = 0


a = A()
print(a.count)
print(A.count)
a.count = 100
A.count = 10
print(a.count)
print(A.count)


class B:
    # 实例属性，通过实例化对象添加的属性属于实例属性
    # 实例属性只能通过实例对象来访问和修改，类对象无法访问修改
    def __init__(self):
        self.name = '孙悟空'


b = B()
# print('B,', B.name)  # 报错
print('b:', b.name)


class C:
    # 实例方法：在类中定义，以第一个参数的方法都是实例方法
    # 实例方法在调用时，Python会将调用对象作为self传入
    # 实例方法可以通过实例和类调用。当通过实例调用时，会自动将当前对象作为self传入
    # 当通过类调用时，不会自动传递self，此时需要手动传递self
    def test(self):
        print('这是test方法~~~')


c = C()
c.test()
# 类调用方法时,需要手动传入实例化对象
C.test(c)  # 等价于c.test()


# 类方法
class D:
    @classmethod
    def test(cls):
        print('这是一个类方法~~~')
        print('类方法', cls)


d = D()
D.test()
d.test()


# 静态方法
class E:
    @staticmethod
    def test():
        print('这是一个静态方法~~~')


e = E()
E.test()
e.test()

"""





