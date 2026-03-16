def load_things(filename='things.txt'):
    """加载清单项目"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def save_things(things, filename='things.txt'):
    """保存清单项目"""
    with open(filename, 'w', encoding='utf-8') as f:
        for thing in things:
            f.write(thing + '\n')

def add(things):
    """添加"""
    input_str = input('请输入要添加的清单项目（用逗号分隔）：')
    new_items = [item.strip() for item in input_str.split(',') if item.strip()]
    added_count = 0
    for item in new_items:
        if item not in things:
            things.append(item)
            added_count += 1
    if added_count > 0:
        save_things(things)
        print(f'成功添加 {added_count} 个项目')
    else:
        print('没有新增项目（可能已存在）')

def delete(things):
    """删除"""
    input_str = input('请输入要删除的清单项目（用逗号分隔）：')
    items_to_delete = [item.strip() for item in input_str.split(',') if item.strip()]
    deleted_count = 0
    for item in items_to_delete:
        if item in things:
            things.remove(item)
            deleted_count += 1
    if deleted_count > 0:
        save_things(things)
        print(f'成功删除 {deleted_count} 个项目')
    else:
        print('未找到要删除的项目')

def find(things):
    """查找"""
    search_term = input('请输入要查找的清单项目：').strip()
    results = [thing for thing in things if search_term in thing]
    if results:
        print(f'找到 {len(results)} 个匹配项：')
        for i, item in enumerate(results, 1):
            print(f"{i}. {item}")
    else:
        print('未找到匹配项')

def show(things):
    """显示"""
    if not things:
        print('当前清单为空')
        return
    print('当前清单：')
    for index, thing in enumerate(things, 1):
        print(f"{index}. {thing}")

def main():
    print('欢迎来到清单管理系统')
    things = load_things()
    
    while True:
        print('\n1. 添加')
        print('2. 删除')
        print('3. 查找')
        print('4. 显示')
        print('5. 退出')
        
        choice = input('请输入你的选择（1-5）：').strip()
        
        if choice == '1':
            add(things)
        elif choice == '2':
            delete(things)
        elif choice == '3':
            find(things)
        elif choice == '4':
            show(things)
        elif choice == '5':
            print('退出系统')
            break
        else:
            print('无效的选择，请输入 1-5 之间的数字')

if __name__ == '__main__':
    main()


# 总结
# 1.每个方法都创建一个函数 ，函数名与方法名一致
# 2.函数调用时，参数顺序必须与函数定义一致
# 3.文件操作也要写到函数内



