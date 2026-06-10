# 第四天任务：读取文件并统计行数、单词数、字符数

filename = "sample.txt"   # 要读取的文件名

try:
    # 打开文件，使用 with 语句自动关闭
    with open(filename, 'r', encoding='utf-8') as file:
        # 读取所有行，存入列表 lines
        lines = file.readlines()

    # 行数 = 列表的长度
    line_count = len(lines)

    word_count = 0   # 单词总数
    char_count = 0   # 字符总数（包含换行符）

    # 遍历每一行
    for line in lines:
        # split() 按空白字符（空格、换行等）切分成单词列表
        words = line.split()
        word_count += len(words)      # 累加这一行的单词数
        char_count += len(line)       # 累加这一行的字符数（包含换行符）

    # 打印统计结果
    print(f"行数：{line_count}")
    print(f"单词数：{word_count}")
    print(f"字符数：{char_count}")

except FileNotFoundError:
    # 如果文件不存在，执行这里的代码
    print("文件不存在")