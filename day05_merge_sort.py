# ========== 第五天任务：合并两个列表并排序 ==========
# 作者：你的名字
# 日期：2026-06-10

# ---------- 1. 定义两个列表 ----------
# 列表1：包含几个整数
list1 = [3, 8, 1, 6]
# 列表2：包含几个整数
list2 = [5, 2, 9, 4, 7]

# print() 是输出函数，可以把内容显示在控制台
print("原始列表1:", list1)   # 输出 -> 原始列表1: [3, 8, 1, 6]
print("原始列表2:", list2)   # 输出 -> 原始列表2: [5, 2, 9, 4, 7]

# ---------- 2. 合并列表 ----------
# 使用 + 运算符将两个列表拼接成一个新列表
# 注意：+ 不会修改原来的 list1 和 list2，而是产生一个新的列表
merged_list = list1 + list2

# 打印合并后的结果
print("合并后的列表（未排序）:", merged_list)
# 输出 -> 合并后的列表（未排序）: [3, 8, 1, 6, 5, 2, 9, 4, 7]

# ---------- 3. 使用 sorted() 函数进行升序排序 ----------
# sorted() 是 Python 内置函数，它接收一个可迭代对象（比如列表），返回一个新的已排序列表
# 原列表 merged_list 保持不变
sorted_list = sorted(merged_list)

# 打印排序后的列表
print("升序排序后的列表（使用sorted）:", sorted_list)
# 输出 -> 升序排序后的列表（使用sorted）: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ---------- 4. 降序排序（给 sorted() 传入 reverse=True 参数）----------
# reverse=True 表示降序（从大到小），默认 reverse=False 是升序
sorted_desc = sorted(merged_list, reverse=True)
print("降序排序后的列表:", sorted_desc)
# 输出 -> 降序排序后的列表: [9, 8, 7, 6, 5, 4, 3, 2, 1]

# ---------- 5. 演示列表自带的 sort() 方法（原地排序）----------
# 创建一个临时列表用于演示
demo_list = [9, 1, 5, 3]
print("\n--- 演示 sort() 方法 ---")
print("调用 sort() 之前的 demo_list:", demo_list)

# sort() 是列表的方法，直接修改原列表，不返回新列表
demo_list.sort()   # 注意：这一行没有赋值，因为 demo_list 自己被改变了

print("调用 sort() 之后的 demo_list:", demo_list)
# 输出 -> [1, 3, 5, 9]

# ---------- 6. 对比总结 ----------
print("\n--- 总结区别 ---")
print("sorted(列表) : 返回新列表，原列表不变")
print("列表.sort()  : 直接修改原列表，返回 None")
# ========== 进阶：用户输入两个列表 ==========
print("\n--- 进阶：用户自定义列表 ---")

# 1. 获取用户输入
# input() 会等待用户输入一段文字，按回车后返回字符串
input_str1 = input("请输入第一组数字，用空格分隔（例如 3 8 1 6）: ")
input_str2 = input("请输入第二组数字，用空格分隔: ")

# 2. 将字符串转换成整数列表
# .split() 方法按空白字符（空格、换行等）将字符串拆分成列表，例如 "3 8 1" -> ["3", "8", "1"]
# 列表推导式 [int(x) for x in ...] 意思是：对于 ... 中的每一个元素 x，把它转换成整数 int(x)，组成新列表
list1_user = [int(x) for x in input_str1.split()]
list2_user = [int(x) for x in input_str2.split()]

# 3. 合并并排序
merged_user = list1_user + list2_user
sorted_user = sorted(merged_user)

# 4. 输出结果
print("你输入的第一个列表:", list1_user)
print("你输入的第二个列表:", list2_user)
print("合并后升序排序的结果:", sorted_user)