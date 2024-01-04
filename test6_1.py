#根据经纬度匹配城市

import pandas as pd
from scipy.spatial import cKDTree

# 读取 CSV 文件
df1 = pd.read_csv('CN-Reanalysis-daily-2018120100.csv')
df2 = pd.read_csv('new_file3.csv',encoding="GBK")

# 创建 KD 树
tree = cKDTree(df2[['经度', '纬度']].values)

# 找到每个 PM2.5 测量点最近的城市
dist, idx = tree.query(df1[[' lon', ' lat']].values)

# 将城市名称添加到 df1
df1['城市'] = df2.loc[idx, '地市'].values

# 按照 "城市" 列进行分组，并计算每个城市的 PM2.5 的平均值
df_new = df1.groupby('城市')['PM2.5(微克每立方米)'].mean().reset_index()
df_new = df1.groupby('城市')[' PM10(微克每立方米)'].mean().reset_index()
df_new = df1.groupby('城市')[' SO2(微克每立方米)'].mean().reset_index()
df_new = df1.groupby('城市')[' NO2(微克每立方米)'].mean().reset_index()
df_new = df1.groupby('城市')[' CO(毫克每立方米)'].mean().reset_index()
df_new = df1.groupby('城市')[' O3(微克每立方米)'].mean().reset_index()
df_new = df1.groupby('城市')[' U(m/s)'].mean().reset_index()
df_new = df1.groupby('城市')[' V(m/s)'].mean().reset_index()
df_new = df1.groupby('城市')[' TEMP(K)'].mean().reset_index()
df_new = df1.groupby('城市')[' PSFC(Pa)'].mean().reset_index()
# 将结果保存为新的 CSV 文件
df_new.to_csv('城市文件.csv', index=False,encoding='GBK')
