import random
number = random.randint(1,100)
count = 0
while count < 3:
    guess = int(input("请输入一个1-100数字:"))
    if guess == number:
        print("恭喜你猜对了")
        break

    elif guess > number:
        print("猜大了")
        count += 1
        print("你已猜了",count,"次")

    else:
        print("猜小了")
        count += 1
        print(f"你已猜了{count}次")

    if count == 3:
        print("你已猜了3次，游戏结束")
        print(f"正确答案是{number}")



