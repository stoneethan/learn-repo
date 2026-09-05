# 数据清洗

这里为你整理一份结合真实业务场景（电商订单数据）的 Pandas 数据清洗指南，以及 SQL 窗口函数核心复习要点。

---

## 一、Pandas 数据清洗（使用电商订单模拟真实数据）

下面我们构建一份包含异常值、缺失值、重复项和数据类型错乱的电商订单数据集，展示实操代码：

```python
import pandas as pd
import numpy as np

# 构造模拟的真实业务数据
raw_data = {
    'order_id': ['1001', '1002', '1003', '1003', '1004', '1005'],
    'user_id': ['U01', 'U02', 'U01', 'U01', 'U03', 'U04'],
    'order_date': ['2026-03-01', '2026-03-01', '2026-03-02', '2026-03-02', '2026-03-03', None],
    'amount': ['$120.50', '$85.00', '$200.00', '$200.00', 'None', '$50.00'],
    'category': ['Electronics', 'Clothing', 'Electronics', 'Electronics', 'Home', 'Clothing'],
    'refund_flag': [0, 1, 0, 0, np.nan, 0]
}

df = pd.DataFrame(raw_data)

```

---

### 1. 缺失值处理 (Missing Values)

首先识别出空值与异常字符串（如字符串 `'None'`），然后进行填充或剔除。

```python
# 将字符串 'None' 转换为真实的 NaN 缺失值
df['amount'] = df['amount'].replace('None', np.nan)

# 查看缺失值分布
print(df.isnull().sum())

# 策略 1：删除关键缺失项（如没有订单日期的记录）
df = df.dropna(subset=['order_date'])

# 策略 2：对分类数据或标记列填充默认值
df['refund_flag'] = df['refund_flag'].fillna(0)

```

---

### 2. 去重 (Duplicates)

业务数据中常因为接口重试或日志重复打印出现完全相同的记录。

```python
# 检查是否存在重复行
print("重复行数：", df.duplicated().sum())

# 按订单号和用户 ID 去重，保留第一条记录
df = df.drop_duplicates(subset=['order_id', 'user_id'], keep='first')

```

---

### 3. 数据类型转换 (Type Conversion)

将带有货币符号的字符串转化为浮点数，将文本日期转换为 Pandas 的 Datetime 格式，以便后续按时间维度统计。

```python
# 清洗字符并转换为 float
df['amount'] = df['amount'].str.replace('$', '', regex=False).astype(float)

# 对金额缺失值使用该类目的均值/中位数填充
df['amount'] = df['amount'].fillna(df['amount'].mean())

# 转换为 datetime 格式
df['order_date'] = pd.to_datetime(df['order_date'])

# 将退款标志转换为 bool 类型
df['refund_flag'] = df['refund_flag'].astype(bool)

# 查看转化后的字段类型
print(df.dtypes)

```

---

### 4. 分组聚合 (Grouping & Aggregation)

清洗完成后，使用 `groupby` 提取多维度业务指标（如各品类的订单数、总成交额及平均订单金额）。

```python
category_summary = df.groupby('category').agg(
    total_orders=('order_id', 'count'),
    total_revenue=('amount', 'sum'),
    avg_order_value=('amount', 'mean')
).reset_index()

print(category_summary)

```

---

## 二、SQL 窗口函数复习

窗口函数可以在保留原表每行记录的同时，计算基于该行所在“窗口”的聚合或排序结果。

语法结构：


$$\text{FUNCTION\_NAME}() \text{ OVER } (\text{PARTITION BY } \dots \text{ ORDER BY } \dots)$$

### 1. 排序函数：`ROW_NUMBER()` vs `RANK()` vs `DENSE_RANK()`

用于根据某个指标排序并编号（如按地区/品类计算排名）。

* **`ROW_NUMBER()`**：连续编号，遇到相同值不会并列（1, 2, 3, 4）。
* **`RANK()`**：跳跃排序，遇到相同值会并列，并跳过后续名次（1, 2, 2, 4）。
* **`DENSE_RANK()`**：紧凑排序，遇到相同值会并列，但不跳过名次（1, 2, 2, 3）。

**经典场景：查询各个类目下消费金额最高的前 2 名用户（Top N）**

```sql
WITH RankedOrders AS (
    SELECT 
        user_id,
        category,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY category 
            ORDER BY amount DESC
        ) AS rank_num
    FROM orders
)
SELECT 
    user_id, 
    category, 
    amount 
FROM RankedOrders 
WHERE rank_num <= 2;

```

---

### 2. 累计聚合函数：`SUM() OVER`

用来计算累计总和（Running Total）或移动平均。

**经典场景：计算每个用户按时间顺序发生的累计消费金额**

```sql
SELECT 
    order_id,
    user_id,
    order_date,
    amount,
    -- 按照用户分组，时间升序，计算截止到当前行的累计消费金额
    SUM(amount) OVER (
        PARTITION BY user_id 
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_amount
FROM orders;

```

> **提示**：如果省略 `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`，在带有 `ORDER BY` 时，`SUM() OVER` 默认就是计算从第一行到当前行的累计和。