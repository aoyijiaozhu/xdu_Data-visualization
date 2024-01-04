import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('全国城市经纬度.csv',encoding='GBK')
print(df.columns)
# 按照 "市" 列进行分组，并计算每个市的经纬度的平均值
df_new = df.groupby('地市')[['经度', '纬度']].mean().reset_index()
df = df.rename(columns={'经度': ' lon', '纬度': ' lat'})
# 将结果保存为新的 CSV 文件
df_new.to_csv('new_file3.csv', index=False,encoding='GBK')
