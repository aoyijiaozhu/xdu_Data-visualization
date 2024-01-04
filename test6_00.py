import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('CN-Reanalysis201812/201812/CN-Reanalysis-daily-2018120100.csv')
print(df.columns)