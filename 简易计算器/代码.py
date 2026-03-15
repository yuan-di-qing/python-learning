def add(a, b):
    """加法运算"""
    return a + b


def subtract(a, b):
    """减法运算"""
    return a - b


def multiply(a, b):
    """乘法运算"""
    return a * b


def divide(a, b):
    """除法运算，处理除零异常"""
    if b == 0:
        raise ZeroDivisionError("除数不能为零！")
    return a / b


def get_valid_number(prompt):
    """获取有效的数字输入，处理输入非数字的情况"""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("❌ 输入错误！请输入有效的数字（如 10、3.14 等）。")


def get_valid_operation():
    """获取有效的运算符输入"""
    valid_ops = ['+', '-', '*', '/', 'q']
    while True:
        op = input("请选择运算类型（+ 加, - 减, * 乘, / 除），输入 q 退出：").strip()
        if op in valid_ops:
            return op
        else:
            print("❌ 输入错误！请输入 +、-、*、/ 中的一个，或输入 q 退出。")


def calculator():
    """主计算器函数"""
    print("=" * 40)
    print("      简易计算器 v1.0")
    print("支持运算：加法(+)、减法(-)、乘法(*)、除法(/)")
    print("输入 q 可随时退出程序")
    print("=" * 40)

    while True:
        # 获取运算符
        operation = get_valid_operation()

        # 退出程序
        if operation == 'q':
            print("\n👋 感谢使用简易计算器，再见！")
            break

        # 获取两个操作数
        num1 = get_valid_number("\n请输入第一个数字：")
        num2 = get_valid_number("请输入第二个数字：")

        # 执行运算并输出结果
        try:
            if operation == '+':
                result = add(num1, num2)
                print(f"\n✅ 计算结果：{num1} + {num2} = {result}")
            elif operation == '-':
                result = subtract(num1, num2)
                print(f"\n✅ 计算结果：{num1} - {num2} = {result}")
            elif operation == '*':
                result = multiply(num1, num2)
                print(f"\n✅ 计算结果：{num1} * {num2} = {result}")
            elif operation == '/':
                result = divide(num1, num2)
                print(f"\n✅ 计算结果：{num1} / {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"\n❌ 计算错误：{e}")

        print("-" * 40)  # 分隔线，提升可读性


# 启动计算器
if __name__ == "__main__":
    calculator()



