import pandas as pd
import numpy as np

# 准备数据
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '部门': ['技术部', '市场部', '技术部', '人事部'],
    '基本工资': [8500, 12000, 9500, 6000]
}
df = pd.DataFrame(data)

# 方式一：直接用广播运算（整列自动加 500）
df['津贴'] = 500
df['应发工资'] = df['基本工资'] + df['津贴']
df['扣除']=122
df['实发工资']=df['应发工资']-df['扣除']
df['薪资等级']=np.where(df['基本工资']>9000,'高薪','底薪')

print("--- 1. 新增津贴与应发工资 ---")
print(df)

# 1. 先写一个 Python 自定义函数
def get_bonus(row):
    dept = row['部门']
    salary = row['基本工资']
    
    if dept == '市场部':
        return salary * 0.15  # 市场部 15% 奖金
    elif dept == '技术部':
        return salary * 0.10  # 技术部 10% 奖金
    else:
        return salary * 0.05  # 其他部门 5% 奖金

# 2. 用 apply 逐行应用这个函数
df['绩效奖金'] = df.apply(get_bonus, axis=1)

print("\n--- 3. 根据部门计算复杂奖金 ---")
print(df)