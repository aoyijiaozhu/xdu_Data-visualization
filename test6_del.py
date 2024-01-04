import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('new_file3.csv',encoding='GBK')

# 删除包含 '延边' 的行
df = df[df['地市'] != '延边']

# 将结果保存为新的 CSV 文件
df.to_csv('new_file3.csv', index=False,encoding="GBK")
