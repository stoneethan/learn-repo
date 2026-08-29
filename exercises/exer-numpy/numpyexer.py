import numpy as np


# 模拟模型输出的预测概率 (5个样本)
probs = np.array([0.15, 0.88, 0.42, 0.95, 0.60])

print(probs[probs>0.5])