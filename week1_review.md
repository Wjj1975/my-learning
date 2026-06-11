步骤3：编写你的第一篇复习笔记
复制下面的模板到 week1_review.md 中，并根据你自己的理解修改和补充（这是你自己的笔记，越个性化越好）。

markdown
# 第1周学习复盘（2026.06.02 - 2026.06.11）

## 一、Day 3：Python 基础复习

### 1. 变量与数据类型
- 整数 `int`、浮点数 `float`、字符串 `str`、布尔值 `bool`
- 动态类型：不需要声明类型，直接赋值

### 2. 循环
- `for` 循环：`for i in range(1, 11):`
- `while` 循环：`while 条件:`

### 3. 函数定义
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
1.类与对象
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def introduce(self):
        print(f"我叫{self.name}，分数{self.score}")
```
二、Day 4：文件读写与异常处理
1. 打开文件
open(文件名, 模式, encoding='utf-8')

模式：'r' 读，'w' 写，'a' 追加

1. 安全读取文件（with 语句）
```python
with open('sample.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
```
with 会自动关闭文件，不用手动 close()。

1. 统计行数、单词数、字符数
len(lines) 行数

line.split() 切分单词

len(line) 字符数

1. 异常处理
```python
try:
    # 可能出错的代码
    pass               
except FileNotFoundError:
    print("文件不存在")
```
三、Day 5：列表合并与排序
1. 合并列表
```python
list1 = [3, 8, 1]
list2 = [5, 2, 9]
merged = list1 + list2   # [3, 8, 1, 5, 2, 9]
```
1. 排序方式对比
方法	是否返回新列表	是否修改原列表
sorted(列表)	是	否
列表.sort()	否	是

示例：

```python
merged = 0  # 定义在69行，这行只是为了消除独立代码块错误，无用。
# 代码要连来看，单看一个代码块，没用。
new_list = sorted(merged)   # 推荐用于临时排序
merged.sort()               # 直接改变 merged
```
1. 用户输入动态列表
```python
input_str = input("请输入数字，空格分隔: ")
numbers = [int(x) for x in input_str.split()]
```
split() 将字符串按空白拆分成字符串列表
列表推导式 [int(x) for x in ...] 逐个转换为整数