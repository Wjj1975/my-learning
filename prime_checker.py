def is_prime(n):
    """判断一个正整数 n 是否为质数"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 17, 18, 97, 100]
    for num in test_numbers:
        print(f"{num} 是质数吗？ {is_prime(num)}")

    while True:
        try:
            user_input = input("\n请输入一个整数（输入 q 退出）：")
            if user_input.lower() == 'q':
                break
            num = int(user_input)
            print(f"{num} {'是' if is_prime(num) else '不是'}质数")
        except ValueError:
            print("请输入有效的整数！")