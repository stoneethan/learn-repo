def isHappy(n,seen=None):
    
    if seen is None:
        seen=set()
    if n in seen:
        return False
    if n==1:
        return True
    seen.add(n)
    return isHappy(jisuan(n),seen)

def jisuan(n):
    if n<=9:
        return n**2
    return (n%10)**2+jisuan(n//10)

print(isHappy(2))

# 快乐数问题，使用递归解决
# 递归三步骤
# 1.定义函数，确定函数作用
# 2.写终止条件，就是自己已知的
# 3.将大问题切成小问题：n/2 n-1 n//2 左右子树等等
# 此道题需注意：
# 1.需要两个终止条件
# 2.假的终止条件为递归中出现过原数
# 3.为了False，我们需要一个集合记录并且随着函数传递
# 4.因此 f(n,seen=None)
