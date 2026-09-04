import pandas as pd

df=pd.read_excel(r"E:\user\Downloads\pandas_数据清洗训练题_第1关.xlsx")

print(df.head())
print(df.shape)
df.info()

df.isnull().mean()*100

df["月销售额"]=pd.to_numeric(df["月销售额"],errors="coerce")


df.groupy("部门")["月销售额"].agg(["sum","mean","max","min"])


