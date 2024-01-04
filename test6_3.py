#生成城市污染数据
import os
import pandas as pd
from scipy.spatial import cKDTree
folder_path='CN-Reanalysis201812/201812'
new_folder_path='new_data'
df2 = pd.read_csv('new_file3.csv',encoding="GBK")
# 创建 KD 树
tree = cKDTree(df2[['经度', '纬度']].values)
# 读取 CSV 文件
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
for file in csv_files:

    df1= pd.read_csv(os.path.join(folder_path, file))
    # 找到每个 污染值 测量点最近的城市
    dist, idx = tree.query(df1[[' lon', ' lat']].values)

    # 将城市名称添加到 df1
    df1['城市'] = df2.loc[idx, '地市'].values

    # 删除不需要的列
    df1 = df1.drop(columns=[' lon', ' lat',' '])
    # 对同名城市的数据进行均值合并
    df1 = df1.groupby('城市').mean().reset_index()

    df1.to_csv(os.path.join(new_folder_path, 'new_' + file), index=False, encoding="GBK")



