# 07 · 第一周 Python 练习（7 天，针对代码薄弱）

> 用法：每天先看教程对应章节（廖雪峰前 15 节），再做当天练习。
> 每题先自己写 15 分钟，写不出来再看答案，**看完答案后要自己再敲一遍**。
> 每天做完 commit 一次到 learn-ai 仓库。

## Day 1 · 变量、字符串、数字（约 1.5 小时）

教程：廖雪峰 1-4 节（数据类型、字符串、格式化）。

1. 打印 `我的名字是XXX，今年23岁`，用 f-string 拼接。
2. 定义 `a = 7`、`b = 3`，打印 `a + b`、`a * b`、`a // b`、`a % b`、`a ** b`，并猜一猜各自结果再运行验证。
3. 把字符串 `" hello world "` 去掉首尾空格并转大写，打印结果。
4. 把字符串 `"3.14"` 转成浮点数，再转成整数，打印两个结果和类型（用 type()）。
5. 用字符串切片取出 `"python"` 的后 3 个字符。

## Day 2 · 列表、元组、字典（约 1.5 小时）

教程：廖雪峰 5-6 节（list、tuple、dict）。

1. 建一个列表 `[5, 2, 9, 1, 7]`，打印：长度、最大值、排序后的列表。
2. 给列表添加 `0` 和 `10`，删除 `1`，再反转，打印结果。
3. 建一个字典存 3 个同学的年龄，打印其中一个人的年龄；用 `.get()` 查一个不存在的名字并返回默认值 `"未找到"`。
4. 把两个列表 `["a","b","c"]` 和 `[1,2,3]` 用 zip 合并成字典，打印。
5. 用 for 循环遍历字典，打印 `名字: 年龄` 格式。

## Day 3 · 条件与循环（约 1.5 小时）

教程：廖雪峰 7-8 节（if、循环）。

1. 写一个函数判断奇偶数（先写 if 版本）。
2. 打印 1-100 中所有能被 3 整除但不能被 5 整除的数，每行 5 个。
3. 用 while 循环打印倒计时 5 到 1，再打印 "发射！"。
4. 写一个"猜数字"：程序随机生成 1-10 的数（`import random; random.randint(1,10)`），让你猜 3 次，猜对打印"中了"，猜错提示"大了/小了"。
5. 打印 99 乘法表（双层 for 循环）。

## Day 4 · 函数（约 1.5 小时）

教程：廖雪峰 9-10 节（函数、参数）。

1. 写函数 `add(a, b)` 返回和；再写 `add_all(*nums)` 接收任意个数求和。
2. 写函数 `is_prime(n)` 判断素数，返回 True/False。
3. 写函数 `count_words(text)` 返回文本里每个单词出现的次数（用 split + dict）。
4. 写函数 `fib(n)` 返回斐波那契数列前 n 项。
5. 写函数 `format_score(score)`：>=90 返回 "A"，>=80 "B"，>=60 "C"，否则 "D"。

## Day 5 · 文件读写（约 1.5 小时）

教程：廖雪峰 12 节（文件读写）。

1. 写一个程序：把 1-100 的平方写入 `squares.txt`（每行一个）。
2. 读回 `squares.txt`，计算总和并打印。
3. 写一个"日志追加器"：每次运行往 `log.txt` 追加一行 `当前时间 - 运行了一次`（用 `datetime` 模块），运行 3 次验证。

## Day 6 · 综合小项目：命令行待办清单（约 2 小时）

> 把前 5 天全部串起来。目标：做一个能在命令行用的待办清单。

功能要求：
- `python todo.py add 写作业` → 添加任务
- `python todo.py list` → 显示所有任务（带序号和完成状态）
- `python todo.py done 1` → 把第 1 个任务标记完成
- `python todo.py remove 2` → 删除第 2 个任务
- 数据存到 `todo.txt`（每行一条，格式：`未完成|写作业`）

提示：用 `sys.argv` 拿命令行参数；用文件读写保存数据。参考答案在文末。

## Day 7 · 复习 + 推 GitHub（约 1 小时）

1. 把 Day 1-6 的所有练习代码整理到 `learn-ai/python-basics/` 目录。
2. 每个文件加一行注释说明功能。
3. 全部 commit 并 push 到 GitHub。
4. 写第一篇"学习记录"放进仓库：这周学会了什么、卡在哪、下周重点。
5. 周日 21:00 做周复盘。

---

## 参考答案（先自己写！）

### Day 1
```python
# 1
name = "小明"
age = 23
print(f"我的名字是{name}，今年{age}岁")

# 2
a, b = 7, 3
print(a + b, a * b, a // b, a % b, a ** b)  # 10 21 2 1 343

# 3
s = " hello world "
print(s.strip().upper())  # HELLO WORLD

# 4
f = float("3.14")
i = int(f)
print(f, type(f), i, type(i))  # 3.14 <class 'float'> 3 <class 'int'>

# 5
print("python"[-3:])  # hon
```

### Day 2
```python
# 1
lst = [5, 2, 9, 1, 7]
print(len(lst), max(lst), sorted(lst))  # 5 9 [1, 2, 5, 7, 9]

# 2
lst.append(0); lst.append(10)
lst.remove(1)
lst.reverse()
print(lst)  # [10, 7, 9, 2, 5, 0]

# 3
ages = {"张三": 20, "李四": 21, "王五": 22}
print(ages["张三"])                # 20
print(ages.get("赵六", "未找到"))   # 未找到

# 4
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = dict(zip(keys, vals))
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# 5
for name, age in ages.items():
    print(f"{name}: {age}")
```

### Day 3
```python
# 1
def even_or_odd(n):
    if n % 2 == 0:
        return "偶数"
    return "奇数"

# 2
count = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i, end=" ")
        count += 1
        if count % 5 == 0:
            print()

# 3
i = 5
while i >= 1:
    print(i)
    i -= 1
print("发射！")

# 4
import random
answer = random.randint(1, 10)
for _ in range(3):
    guess = int(input("猜一个 1-10 的数："))
    if guess == answer:
        print("中了")
        break
    elif guess > answer:
        print("大了")
    else:
        print("小了")
else:
    print(f"答案是{answer}")

# 5
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j}", end="\t")
    print()
```

### Day 4
```python
# 1
def add(a, b):
    return a + b

def add_all(*nums):
    return sum(nums)

# 2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 3
def count_words(text):
    result = {}
    for w in text.split():
        result[w] = result.get(w, 0) + 1
    return result

# 4
def fib(n):
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

# 5
def format_score(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 60:
        return "C"
    return "D"
```

### Day 5
```python
# 1
with open("squares.txt", "w") as f:
    for i in range(1, 101):
        f.write(f"{i*i}\n")

# 2
total = 0
with open("squares.txt") as f:
    for line in f:
        total += int(line.strip())
print(total)  # 338350

# 3
from datetime import datetime
with open("log.txt", "a") as f:
    f.write(f"{datetime.now()} - 运行了一次\n")
```

### Day 6（待办清单）
```python
import sys

FILE = "todo.txt"

def load():
    tasks = []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            for line in f:
                status, text = line.strip().split("|", 1)
                tasks.append([status, text])
    except FileNotFoundError:
        pass
    return tasks

def save(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        for status, text in tasks:
            f.write(f"{status}|{text}\n")

def add(text):
    tasks = load()
    tasks.append(["未完成", text])
    save(tasks)
    print(f"已添加：{text}")

def show():
    tasks = load()
    if not tasks:
        print("暂无任务")
        return
    for i, (status, text) in enumerate(tasks, 1):
        mark = "✔" if status == "完成" else " "
        print(f"{i}. [{mark}] {text}")

def done(idx):
    tasks = load()
    if 1 <= idx <= len(tasks):
        tasks[idx - 1][0] = "完成"
        save(tasks)
        print("已标记完成")

def remove(idx):
    tasks = load()
    if 1 <= idx <= len(tasks):
        tasks.pop(idx - 1)
        save(tasks)
        print("已删除")

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "add":
        add(sys.argv[2])
    elif cmd == "list":
        show()
    elif cmd == "done":
        done(int(sys.argv[2]))
    elif cmd == "remove":
        remove(int(sys.argv[2]))
```
